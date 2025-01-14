import 'dart:convert';

import 'package:chat_gpt_sdk/chat_gpt_sdk.dart';
import 'package:flutter/material.dart';
import 'package:flutter_dotenv/flutter_dotenv.dart';
import 'package:university_project/db.dart';
import 'package:university_project/universityDetails.dart';

//import 'package:chatgpt_client/models/chat_message.dart';

class recommendationResults extends StatefulWidget {
  const recommendationResults({Key? key, required this.info})
      : super(
            key:
                key); //Key? is always required and usually passed in already, this.info is a variable to pass in,
  final String info; //final=no changing;

  @override
  State<recommendationResults> createState() => _recommendationResultsState();
}

class _recommendationResultsState extends State<recommendationResults> {
  late final OpenAI
      _openAI; //late=we're gonna give the variable a value later on, that's why its created wo equal to
  List _result = [];
  bool isLoading = true; //once get response, is loading will be false
  Map allUniversityInfo =
      {}; //so we dont have to run db again fro the search page

  @override
  void initState() {
    univData();
    super.initState(); //runs the normal function
    _openAI = OpenAI.instance.build(
        token: dotenv.env['OpenAI-key'],
        baseOption: HttpSetup(
            receiveTimeout: Duration(
                seconds:
                    30))); //timeout if it takes longer than 30 sec to receive anwser
    chatGPTCall();
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
                      Navigator.of(context).pop();
                    },
                    //first .pop gets out of alert dialogue, second goes back to stats
                    child: Text("OK"))
              ],
            ));
  }

  void chatGPTCall() async {
    print("======chatGPTCall============");
    //async=wait for answer to come back
    int num_universities = 20;
    try {
      String instructionPrompt =
          "Please recommend $num_universities universities based on ${widget.info}, providing a"
          " brief description for each. Ensure that your recommendations are "
          "only from the following list: ${allUniversityInfo.keys}. The university names "
          "must match exactly as they appear in the list, including uppercase "
          "and lowercase letters. DO NOT RECOMMEND Universities that are not on"
          " the list of universities. Return your response "
          "as a JSON object in the following format: "
          '[{"name": "University Name", "description": "University Description"}].'
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
      print(response!.choices.first.message!.content);
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
    return Scaffold(
      appBar: AppBar(
        leading: IconButton(
          icon: Icon(Icons.arrow_back_ios_new_rounded, color: Colors.white),
          onPressed: () {
            Navigator.pop(context);
          },
        ),
        automaticallyImplyLeading: false,
        elevation: 0,
        backgroundColor: const Color.fromRGBO(129, 155, 218, 1.0),
        toolbarHeight: 100,
        title: Column(
          children: [
            SizedBox(
              height: 60,
              width: double.infinity,
              child: Image.asset(
                'images/university_logo.png',
                fit: BoxFit.fitHeight,
              ),
            ),
            const Padding(
              padding: EdgeInsets.only(top: 8.0),
              child: Text(
                'Recommendation',
                style: TextStyle(color: Colors.white),
              ),
            )
          ],
        ),
      ),
      body: isLoading
          ? Center(
              child: CircularProgressIndicator()) //? means isLoading is true
          : ListView.builder(
              itemCount: _result.length,
              itemBuilder: (context, index) {
                String universityName = _result[index]['name'];
                if (allUniversityInfo[universityName] == null)
                  return Container();
                return Padding(
                  padding: const EdgeInsets.all(8.0),
                  child: Card(
                    color: const Color.fromRGBO(217, 229, 229, 1.0),
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
                      subtitle: Text(_result[index]['description']),
                      trailing: const Icon(
                        Icons.arrow_forward_ios_rounded,
                        color: Colors.black,
                      ),
                    ),
                  ),
                );
              },
            ),
    );
  }
}
