import 'package:flutter/material.dart';
import 'homePage.dart';
import 'recommendationPage.dart';

//route page= bottom navigational
class routePage extends StatefulWidget {//nothing much done here
  const routePage({super.key});

  @override
  State<routePage> createState() => _routePageState();
}

class _routePageState extends State<routePage> {
  int selectedIndex=0; //0=home, 1=recommendation page
  List<Widget>? widgetOptions;

  @override //overriding other function
  void initState() {
    //always runs at the very beginning of app opening
    //starter code when the code that first runs when we first open app
    super.initState(); // still run the code that was originally in initstate, the normal code before overridden
    widgetOptions=[homePage(),recommendationPage()]; //create the home and rec widgets asap, so that theyre on the phone screen
  }

  void widgetPressed(int index){ //void bc we're not returning anything, change selectedIndex to inputted index
    setState(() { //"we made a change so update screen pls"
      selectedIndex=index;
    });
  }

  @override
  Widget build(BuildContext context) {
    return  Scaffold(
      body:Center(//sort of like we are staying on routepage 'forever' by having the nav bar there forever and only changing the top part of the screen
        child: widgetOptions!.elementAt(selectedIndex), //goes into widgetOptions list and takes the selected index value (home or rec) just like widgetoptions[0]
      //switches screen to the value of widgetoptions, ie home or rec
      ),
      bottomNavigationBar: BottomNavigationBar( //generally anything after colon is capitalized
        backgroundColor: Color.fromRGBO(183, 188, 203, 1),
        type: BottomNavigationBarType.fixed, //stay constant, no scrolling
        items: [
          BottomNavigationBarItem(icon: Icon(Icons.home), label:"Home"),
          BottomNavigationBarItem(icon: Icon(Icons.school), label:"Recommendations")
        ],
        currentIndex: selectedIndex,
        selectedItemColor: Color.fromRGBO(74, 76, 82, 1),
        onTap: widgetPressed,//function but no (), supposedly the above selectedIndex
    ),
    );
  }
}
