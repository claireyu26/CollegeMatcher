import 'package:flutter/material.dart';
import 'db.dart';
import 'universityList.dart';
import 'universityDetails.dart';

//5/19/24

//started with main.dart which runs splashscreen that goes into routePage
//routePage is the bottom part of the app that the other half, homepage, completes the screen
//homePage gets all universities and puts them into scrolling thing, clickable
//has trending unis, two buttons: 1 for list of universities and 2 for all schools trending (aka 2 diff pages that hoemPage leads to)
//universityListScreens,-->specifically to universityDetails (from universityList, and 2 inside of homePage then clicked on trending schools)

//could universityDetails also come from clickable reccomendations
class homePage extends StatefulWidget {
  const homePage({super.key});

  @override
  State<homePage> createState() => _homePageState();
}

class _homePageState extends State<homePage> {

  List trendingUniversities=["Alliant International University","American Jewish University","American University","Andrews University","ArtCenter College of Design","Bard College"]; //add more later
  Map trendingUniversityInfo={}; //a dictionary
  Map allUniversityInfo={}; //so we dont have to run db again fro the search page
  bool isLoading=true;

  @override
  void initState() {//to get/connect to once opened up
    super.initState();
    getUniversities();
  }

  void getUniversities(){
    getData().then((value){ //.then says wait for getData to get values then do the after things
      for (String university in trendingUniversities){
        trendingUniversityInfo[university]=value[university];//puts the db info into a map
      }
      setState(() {
        allUniversityInfo=value;
        isLoading=false;
      });
    });
  }

  @override
  Widget build(BuildContext context) {
    double height=MediaQuery.of(context).size.height;
    double width=MediaQuery.of(context).size.width;

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
                  'Home',
                  style: TextStyle(color: Colors.white),
                ),
              )
            ],
          ),
        ),

      body: Center(
        child: isLoading //?=if isLoading is true OR :means if isLoading is false
            ?Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children:[
              CircularProgressIndicator()
            ]
          )
        )
            :SingleChildScrollView(
          child: Column(
            children: [
              Card(
                child:SizedBox(
                  height: height*0.6,
                  width:width*0.9,
                  child: ListView(
                    physics:ClampingScrollPhysics(),//scrolling
                    children: [
                      Padding(
                          padding: EdgeInsets.all(8),
                        child: Text("Trending Universities",style: TextStyle(fontSize: 22, color: Color.fromRGBO(129, 155, 218, 1.0)), ),

                      ),//Widget(modifier:...),
                      Container(
                        height:5,
                      ),
                      ListView.builder(
                        physics:ClampingScrollPhysics(),
                        shrinkWrap: true,
                        itemCount: trendingUniversities.length,
                        itemBuilder: (context,index){ //index goes up to itemCount, itemBuilder="for loop", for loop doesn't make widgets but itemBuilder does
                          String university = trendingUniversityInfo.keys.elementAt(index);
                          return Padding(
                              padding:EdgeInsets.all(8),
                            child:Card(
                              child: ListTile(
                                title: Text(university),
                                trailing: IconButton(
                                    onPressed: (){
                                      Navigator.push(context, MaterialPageRoute(builder: (BuildContext context) => universityDetails(universityInfo: trendingUniversityInfo[university], universityName: university)));
                                },
                                    icon: Icon(Icons.arrow_forward),
                                ),
                              )
                            )
                          );
                        }, //index is something to refer to like a for loop
                      ),
                    ],
                  )
                )
              ),
              ElevatedButton(
                  onPressed: (){
                    Navigator.push(context, MaterialPageRoute(builder: (BuildContext context) => universityList(universities:allUniversityInfo)));
                  },
                  child: Text("Find all universities",style: TextStyle(fontSize: 20),),
              )
            ],
          )
        )
      ),
    );
  }

}
