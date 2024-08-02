import 'package:flutter/material.dart';
import 'package:flutter/cupertino.dart';
import 'recommendationResults.dart';
import 'recommendationResults2.dart';

class recommendationPage extends StatefulWidget {
  const recommendationPage({super.key});

  @override
  State<recommendationPage> createState() => _recommendationPageState();
}

class _recommendationPageState extends State<recommendationPage> {
  //initialize the contorllers
  List<TextEditingController> statsControllers = [];
  List<TextEditingController> awardsControllers = [];
  List<TextEditingController> extracurricularControllers = [];
  List<TextEditingController> majorControllers = [];
  List<TextEditingController> otherControllers = [];
  List<TextEditingController> rangeControllers = [];

  @override//override bc we're doing more for init
  void initState(){
    super.initState();
    statsControllers.add(TextEditingController());
    awardsControllers.add(TextEditingController());
    extracurricularControllers.add(TextEditingController());
    majorControllers.add(TextEditingController());
    otherControllers.add(TextEditingController());
    rangeControllers.add(TextEditingController());
  }
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      //app bar
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
                'images/CollegeMatcher_logo.png',
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
      body: Padding(
          padding:EdgeInsets.all(16),
        child: ListView(
          children:[
            buildSection("Stats:", statsControllers),
            buildSection("Awards:", awardsControllers),
            buildSection("Extracurriculars:", extracurricularControllers),
            buildSection("Aspiring major:", majorControllers),
            buildSection("Range of schools:", rangeControllers),
            buildSection("Other:", otherControllers),
            ElevatedButton(onPressed: (){
              String data=getAllData();
              Navigator.push(context, MaterialPageRoute(builder: (BuildContext context) => recommendationResults(info:data))); //remove current page and go to new page"~
              //in
            }, child: Text("Next"))
          ]
        )
      ),
    );

  }

  Widget buildSection(String title, List<TextEditingController> controllers) {
    //controllers= way for users to type in smth
    return Card(
      color: Color.fromRGBO(183, 188, 203, 1),
      child: Padding(padding: EdgeInsets.all(8.0),
        child: Column(
            children: [
              Text(title),
              SizedBox(height: 10),
              Column( //stacked column of the controllers/input boxes
                  children: controllers.map((
                      controller) { //like a for loop, loop through list controllers| controller=item / what user inputs, controllers=list
                    return Card( //this is going to happen for each controller
                        child: Padding(padding: EdgeInsets.all(8.0),
                            child: TextField(maxLines: 3,
                                controller: controller, //the text
                                decoration: InputDecoration(
                                  contentPadding: EdgeInsets.symmetric(
                                      horizontal: 8),
                                  border: InputBorder.none,
                                  hintText: "Enter text",
                                )
                            )

                        )
                    );
                  }
                  )
                      .toList() //we need to change it to a list bc of children always needs a list and controllers.map(controller) is not list
              ),
              Align(
                  alignment: Alignment.centerRight,
                  child: IconButton(
                    onPressed: () {
                      setState(() { //set state bc we are updating screen when plus button pressed
                        controllers.add(TextEditingController());
                      });
                    },
                    icon: Icon(Icons.add_box_outlined),
                  )
              )
            ]
        ),
      ),
    );
  }
  String getData(controllers){//getting the user's entered text from the controllers
    String data="";
    for (TextEditingController controller in controllers){
      data+=" - ${controller.text}\n";
    }
    return data;

  }
  void disposeControllers(controllers){
    String data="";//to be safe have this (?)
    for (TextEditingController controller in controllers){ //disposing the controllers on the 'memory' and the screen
      controller.dispose();
    }
  }
  String getAllData(){
    String data="";
    data+=getData(statsControllers);
    data+=getData(awardsControllers);
    data+=getData(extracurricularControllers);
    data+=getData(majorControllers);
    data+=getData(otherControllers);
    data+=getData(rangeControllers);
    return data;
  }
  @override //overrides the dispose function
  void dispose(){
    disposeControllers(statsControllers);//goes through each controller and disposes them
    disposeControllers(awardsControllers);
    disposeControllers(extracurricularControllers);
    disposeControllers(majorControllers);
    disposeControllers(otherControllers);
    disposeControllers(rangeControllers);
    super.dispose(); //runs the usual dispose function, has to do with memory leaks, dispose is usually automatically ran to prevent memory leaks
  }

}
