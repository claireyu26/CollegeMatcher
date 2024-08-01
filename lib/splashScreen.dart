import 'package:flutter/material.dart';
import 'package:university_project/routePage.dart';

class splashScreen extends StatefulWidget {
  const splashScreen({super.key});

  @override
  State<splashScreen> createState() => _splashScreenState();
}

class _splashScreenState extends State<splashScreen> {
  @override //overriding other function
  void initState() { //always runs at the very beginning of app opening
    //starter code when the code that first runs when we first open app
    super.initState(); // still run the code that was originally in initstate, the normal code before overridden
    init(); //the below function
  }//

  Future<void> init() async { //use future when we want to wait a function
    await Future.delayed(Duration(seconds:2)).then((value) { //wait 2 secs then run
      Navigator.pop(context); //context for going to a new page
      Navigator.push(context, MaterialPageRoute(builder: (BuildContext context) => routePage())); //remove current page and go to new page"~
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Image.asset(
        'images/university_logo.png', //images are not const
        height: 300.0,
      ),
      ),
    );
  }
}
