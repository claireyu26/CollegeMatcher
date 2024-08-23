import 'dart:convert';

import 'package:chat_gpt_sdk/chat_gpt_sdk.dart';
import 'package:flutter/material.dart';
import 'package:flutter_dotenv/flutter_dotenv.dart';
import 'package:university_project/db.dart';
import 'package:university_project/seenPlaces.dart';
import 'package:university_project/universityDetails.dart';

//import 'package:chatgpt_client/models/chat_message.dart';

class YourRecommendation extends StatefulWidget {
  const YourRecommendation({Key? key})
      : super(
            key:
                key); //Key? is always required and usually passed in already, this.info is a variable to pass in,

  @override
  State<YourRecommendation> createState() => _YourRecommendationState();
}

class _YourRecommendationState extends State<YourRecommendation> {
  late final OpenAI
      _openAI; //late=we're gonna give the variable a value later on, that's why its created wo equal to
  List _result = [];
  bool isLoading = true; //once get response, is loading will be false
  Map allUniversityInfo =
      {}; //so we dont have to run db again fro the search page
  String keySharePref = "seen";

  @override
  @override
  void initState() {
    super.initState(); //runs the normal function
    _openAI = OpenAI.instance.build(
        token: dotenv.env['OpenAI-key'],
        baseOption: HttpSetup(
            receiveTimeout: Duration(
                seconds:
                    30))); //timeout if it takes longer than 30 sec to receive anwser
    univData().then((value) {
      seenPlace(keySharePref).then((universities) {
        if (universities.isEmpty) {
          //Randomly pick 10 universities from the list
          // print(allUniversityInfo);
          List tempUniversities = allUniversityInfo.keys.toList()..shuffle();
          // print(allUniversityInfo.keys);
          tempUniversities = tempUniversities.sublist(0, 10);
          for (String university in tempUniversities) {
            _result.add({
              "name": university,
            });
          }
        }
        chatGPTCall(universities);
      });
    });
  }

  univData() async {
    allUniversityInfo = await getData();
  }

  Future<dynamic> showDialogueError() {
    return showDialog(
        context: context,
        builder: (context) => AlertDialog(
              title: Text("Error"),
              content: Text(
                  "An error occurred while we were generating your schools. Please try again."),
              actions: [
                TextButton(
                    onPressed: () {
                      Navigator.of(context)
                          .pop(); //pop = go back to previous page

                    },
                    //first .pop gets out of alert dialogue, second goes back to stats
                    child: Text("OK"))
              ],
            ));
  }

  void chatGPTCall(universities) async {
    print("======chatGPTCall============");
    //async=wait for answer to come back
    int numUniversities = 20;
    // print(universities);
    try {
      String instructionPrompt =
          "Based on the universities I've already explored: $universities, "
          "I would like you to recommend $numUniversities similar universities "
          "that align with my academic interests and campus preferences."
          " For instance, if I've looked at UC Berkeley, I'd like to see"
          " recommendations like UCLA and other UC schools. "
          "Ensure that your recommendations are "
          "only from the following list: ${allUniversityInfo.keys}. The university names "
          "must match exactly as they appear in the list, including uppercase "
          "and lowercase letters. DO NOT RECOMMEND Universities that are not on"
          " the list of universities. Return your response "
          "as a JSON object in the following format: "
          '[{"name": "University Name"}].'
          " Do not include any information outside the JSON object.";
      //widget.info=information from previous page thats passed in
      //could just ask up there for it to return list
      //COUPLE POSSIBLE ISSUES:
      //what happens if they recommend a school that we don't have in the database?
      //spelling matters (shorthand for ex)
      //like a feature update
      //marisabel
      final request = ChatCompleteText(
        messages: [
          Map.of({"role": "user", "content": instructionPrompt})
        ],
        maxToken: 2500,
        model: GptTurbo0631Model(),
      );

      ChatCTResponse? response =
          await _openAI.onChatCompletion(request: request);

      setState(() {
        _result = jsonDecode(response!.choices.first.message!.content);
        isLoading = false;
      });
    } catch (e) {
      print(e);
      setState(() {
        isLoading = false;
      });
      showDialogueError();
    }
  }

  @override
  Widget build(BuildContext context) {
    // print(_result);
    return isLoading
        ? Center(
            child: Column(
            children: [
              SizedBox(
                height: 100,
              ),
              CircularProgressIndicator(),
            ],
          )) //? means isLoading is true
        : ListView.builder(
            shrinkWrap: true,
            physics: const ClampingScrollPhysics(),
            itemCount: _result.length,
            itemBuilder: (context, index) {
              String universityName = _result[index]['name'];
              if (allUniversityInfo[universityName] == null) return Container();
              return Padding(
                padding: const EdgeInsets.all(8.0),
                child: Card(
                  child: ListTile(
                    onTap: () {
                      Navigator.push(
                          context,
                          MaterialPageRoute(
                              builder: (BuildContext context) =>
                                  universityDetails(
                                    universityInfo:
                                        allUniversityInfo[universityName],
                                    universityName: _result[index]['name'],
                                  )));
                    },
                    title: Text(universityName),
                    trailing: const Icon(
                      Icons.arrow_forward_ios_rounded,
                      // color: Colors.black,
                    ),
                  ),
                ),
              );
            },
          );
  }
}
