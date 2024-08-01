import 'package:flutter/material.dart';

import 'package:chat_gpt_sdk/chat_gpt_sdk.dart';
import 'package:flutter_dotenv/flutter_dotenv.dart';

//import 'package:chatgpt_client/models/chat_message.dart';

class recommendationResults extends StatefulWidget {
  const recommendationResults({Key? key,required this.info}): super(key: key);//Key? is always required and usually passed in already, this.info is a variable to pass in,
  final String info; //final=no changing;


  @override
  State<recommendationResults> createState() => _recommendationResultsState();
}

class _recommendationResultsState extends State<recommendationResults> {
  late final OpenAI _openAI; //late=we're gonna give the variable a value later on, that's why its created wo equal to
  String result="";
  bool isLoading=true; //once get response, is loading will be false
  Map allUniversityInfo={}; //so we dont have to run db again fro the search page


  @override
  void initState(){
    super.initState(); //runs the normal function
    _openAI=OpenAI.instance.build(
      token: dotenv.env['OPENAI_API_KEY'],
        baseOption: HttpSetup(receiveTimeout: Duration(seconds:30))
    ); //timeout if it takes longer than 30 sec to receive anwser
    chatGPTCall();
  }

  Future<dynamic> showDialogueError(){
    return showDialog(
        context: context,
        builder: (context)=>AlertDialog(
            title: Text("Error"),
            content:Text("An error occurred while we were generating your schools. Please try again."),
            actions: [
              TextButton(
                  onPressed: (){
                    Navigator.of(context).pop(); //pop = go back to previous page
                    Navigator.of(context).pop();
                    }, //first .pop gets out of alert dialogue, second goes back to stats
                  child: Text("OK"))
            ],
        )
    );
  }

  void chatGPTCall() async{ //async=wait for answer to come back
    //try{
      String instructionPrompt =
          "Please give me a recommendation of 20 universities based on "
          "${widget.info} with some description of each university  "; //widget.info=information from previous page thats passed in
      //could just ask up there for it to return list
      //COUPLE POSSIBLE ISSUES:
      //what happens if they recommend a school that we don't have in the database?
      //spelling matters (shorthand for ex)
      //like a feature update
      //marisabel
      final request=ChatCompleteText(
        messages: [Map.of({"role": "user", "content": instructionPrompt})],

        maxToken: 2500,
        //token=each individual character --> less than 2500 char
        model: GptTurbo0631Model()
      );
      ChatCTResponse? response=await _openAI.onChatCompletion(request:request); //? means it CAN be empty
      setState(() {//tells the screen to change based on changes
        result=response!.choices.first.message!.content.trim().replaceAll('"', ''); //! means it CANNOT be empty, must have value
        isLoading=false; //two different scenarios, 1) when we actually get a response 2) error
      });
   // } //catch(e){
  //     setState(() {
  //       isLoading=false;
  //     });
  //     showDialogueError(); //widget with error message
  //   }
   }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
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
            ? Center(child:CircularProgressIndicator()) //? means isLoading is true
            : SingleChildScrollView(
            child: Column(
                children:[
                  Padding(
                      padding: EdgeInsets.all(8),
                      child: Text(result)
                  ),
                ]
            )
        )
    );
  }
}
            // SingleChildScrollView(
            //     child: Column(
            //       children: [
            //         Card(
            //             child:SizedBox(
            //                 // height: height*0.6,
            //                 // width:width*0.9,
            //                 child: ListView(
            //                   physics:ClampingScrollPhysics(),//scrolling
            //                   children: [
            //                     Padding(
            //                       padding: EdgeInsets.all(8),
            //                       child: Text("Recommended Universities",style: TextStyle(fontSize: 22, color: Color.fromRGBO(129, 155, 218, 1.0)), ),
            //
            //                     ),//Widget(modifier:...),
            //                     Container(
            //                       height:5,
            //                     ),
            //                     ListView.builder(
            //                       physics:ClampingScrollPhysics(),
            //                       shrinkWrap: true,
            //                       itemCount: 20,
            //
            //                       itemBuilder: (context,index){ //index goes up to itemCount, itemBuilder="for loop", for loop doesn't make widgets but itemBuilder does
            //                         String university = .keys.elementAt(index);
            //                         return Padding(
            //                             padding:EdgeInsets.all(8),
            //                             child:Card(
            //                                 child: ListTile(
            //                                   title: Text(university),
            //                                   trailing: IconButton(
            //                                     onPressed: (){
            //                                       Navigator.push(context, MaterialPageRoute(builder: (BuildContext context) => universityDetails(universityInfo: recommendations[index], universityName: university)));
            //                                     },
            //                                     icon: Icon(Icons.arrow_forward),
            //                                   ),
            //                                 )
            //                             )
            //                         );
            //                       }, //index is something to refer to like a for loop
            //                     ),
            //                   ],
            //                 )
            //             )
            //         ),
            //
            //         ElevatedButton(
            //           onPressed: (){
            //             Navigator.push(context, MaterialPageRoute(builder: (BuildContext context) => universityList(universities:allUniversityInfo)));
            //           },
            //           child: Text("Find all universities",style: TextStyle(fontSize: 20),),
            //         )
            //       ],
            //     )
            // )

