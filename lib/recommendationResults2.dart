import 'package:flutter/material.dart';
import 'universityList.dart';
import 'universityDetails.dart';

class recommendationResults2 extends StatefulWidget {
  const recommendationResults2({super.key});

  @override
  State<recommendationResults2> createState() => _recommendationResults2State();
}

class _recommendationResults2State extends State<recommendationResults2> {
  Map allUniversityInfo =
      {}; //so we dont have to run db again fro the search page

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          automaticallyImplyLeading: false,
          elevation: 0,
          backgroundColor: const Color.fromRGBO(129, 155, 218, 1.0),
          toolbarHeight: 100,
          title: ListView(
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
                  'Recommendation results',
                  style: TextStyle(color: Colors.white),
                ),
              )
            ],
          ),
        ),
        body: SingleChildScrollView(
          child:Column(
            children:[
              Padding(
                padding: const EdgeInsets.all(10.0),
                child: Container(
                  child:Text("Based on your impressive academic and extracurricular achievements, here are 20 universities that offer strong programs in computer science and mathematics, are located in or near cities, and are relatively affordable state schools:")),
              ),

              Container(
              child: Padding(
                        padding: EdgeInsets.all(8),
                        child: Center(
                            child: Card(
                            child: ListTile(
                          title: Text("University of California, Berkeley"),
                          trailing: IconButton(
                            onPressed: () {
                              Navigator.push(
                                  context,
                                  MaterialPageRoute(
                                      builder: (BuildContext context) =>
                                          universityDetails(
                                              universityInfo:
                                                  allUniversityInfo,
                                              universityName: "university")));
                            },
                            icon: Icon(Icons.arrow_forward),
                          ),
                            )
                        )
                            )
                        )
    ),
            Padding(
              padding: const EdgeInsets.all(10.0),
              child: Container(
                color: Color.fromRGBO(129, 155, 218, 1.0),
                child: Padding(
                  padding: const EdgeInsets.all(8.0),
                  child: Text("Location: Berkeley, CA \n \n Description: Known for its prestigious computer science and mathematics programs. Located near Silicon Valley, it offers numerous opportunities for internships and networking."),
                )
              ),
            ),
            Container(
                child: Padding(
                  padding: const EdgeInsets.all(8.0),
    child: Center(
    child: Card(
                child: ListTile(
                  title: Text("University of Illinois at Urbana-Champaign (UIUC)"),
                  trailing: IconButton(
                    onPressed: () {
                      Navigator.push(
                          context,
                          MaterialPageRoute(
                              builder: (BuildContext context) =>
                                  universityDetails(
                                      universityInfo:
                                      allUniversityInfo,
                                      universityName: "university")));
                    },
                    icon: Icon(Icons.arrow_forward),
                  ),
    )
                  )
                  )

        )
                  ),
              Padding(
                padding: const EdgeInsets.all(10.0),
                child: Container(
                    color: Color.fromRGBO(129, 155, 218, 1.0),
                    child: Padding(
                      padding: const EdgeInsets.all(8.0),
                      child: Text("Location: Urbana-Champaign, IL \n \n Description: Highly ranked for computer science and engineering. The campus is located in a vibrant college town with strong connections to tech companies."),
                    )
                ),
              ),
              Container(
                  child: Padding(
                      padding: const EdgeInsets.all(8.0),
                      child: Center(
                          child: Card(
                              child: ListTile(
                                title: Text("University of Texas at Austin (UT Austin)"),
                                trailing: IconButton(
                                  onPressed: () {
                                    Navigator.push(
                                        context,
                                        MaterialPageRoute(
                                            builder: (BuildContext context) =>
                                                universityDetails(
                                                    universityInfo:
                                                    allUniversityInfo,
                                                    universityName: "university")));
                                  },
                                  icon: Icon(Icons.arrow_forward),
                                ),
                              )
                          )
                      )

                  )
              ),
              Padding(
                padding: const EdgeInsets.all(10.0),
                child: Container(
                    color: Color.fromRGBO(129, 155, 218, 1.0),
                    child: Padding(
                      padding: const EdgeInsets.all(8.0),
                      child: Text("Location: Austin, TX \n \n Description: Offers a top-tier computer science program. Austin is a booming tech hub, providing ample opportunities for internships and jobs."),
                    )
                ),
              ),
              Container(
                  child: Padding(
                      padding: const EdgeInsets.all(8.0),
                      child: Center(
                          child: Card(
                              child: ListTile(
                                title: Text("Georgia Institute of Technology (Georgia Tech)"),
                                trailing: IconButton(
                                  onPressed: () {
                                    Navigator.push(
                                        context,
                                        MaterialPageRoute(
                                            builder: (BuildContext context) =>
                                                universityDetails(
                                                    universityInfo:
                                                    allUniversityInfo,
                                                    universityName: "university")));
                                  },
                                  icon: Icon(Icons.arrow_forward),
                                ),
                              )
                          )
                      )

                  )
              ),
              Padding(
                padding: const EdgeInsets.all(10.0),
                child: Container(
                    color: Color.fromRGBO(129, 155, 218, 1.0),
                    child: Padding(
                      padding: const EdgeInsets.all(8.0),
                      child: Text("Location: Atlanta, GA \n \n Description: Renowned for its rigorous computer science and engineering programs. Located in Atlanta, a major metropolitan area with a growing tech industry."),
                    )
                ),
              ),
              Container(
                  child: Padding(
                      padding: const EdgeInsets.all(8.0),
                      child: Center(
                          child: Card(
                              child: ListTile(
                                title: Text("University of Washington (UW)"),
                                trailing: IconButton(
                                  onPressed: () {
                                    Navigator.push(
                                        context,
                                        MaterialPageRoute(
                                            builder: (BuildContext context) =>
                                                universityDetails(
                                                    universityInfo:
                                                    allUniversityInfo,
                                                    universityName: "university")));
                                  },
                                  icon: Icon(Icons.arrow_forward),
                                ),
                              )
                          )
                      )

                  )
              ),
              Padding(
                padding: const EdgeInsets.all(10.0),
                child: Container(
                    color: Color.fromRGBO(129, 155, 218, 1.0),
                    child: Padding(
                      padding: const EdgeInsets.all(8.0),
                      child: Text("Location: Seattle, WA \n \n Description: Offers a strong computer science program with close ties to major tech companies like Microsoft and Amazon, both headquartered in Seattle."),
                    )
                ),
              ),
    ]

        ))
    );
    /*isLoading
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
    );*/
  }
}
