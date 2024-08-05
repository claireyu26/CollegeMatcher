import 'package:flutter/material.dart';
import 'package:university_project/seenPlaces.dart';

import 'universityDetails.dart';

class universityList extends StatefulWidget {
  const universityList({Key? key, required this.universities})
      : super(
            key:
                key); //Key? is always required and usually passed in already, this.info is a variable to pass in,

  final Map universities;

  @override
  State<universityList> createState() => _universityListState();
}

class _universityListState extends State<universityList> {
  Map duplicateUniversities =
      {}; //static variables vs setting variable equal to another variable //can't set it equal to unviersities here bc it doesn't exist yet

  Set seen = {};
  String keySharePref = "seen";

  @override //overriding other function
  void initState() {
    //always runs at the very beginning of app opening
    //starter code when the code that first runs when we first open app
    super
        .initState(); // still run the code that was originally in initstate, the normal code before overridden
    duplicateUniversities =
        widget.universities; //loophole around it, bc this is done "last"
    seenPlace(keySharePref).then((value) {
      setState(() {
        seen = value;
      });
    });
  }

  void filterSearchResults(query) {
    duplicateUniversities =
        {}; //reset this duplicate map //list of matched universities based on input
    setState(() {
      //change
      widget.universities.forEach((university, value) {
        if (university.toLowerCase().contains(query.toLowerCase())) {
          //if the lowercased university contains the lowercase input
          duplicateUniversities[university] = value;
        }
      });
    });
  }

  @override
  Widget build(BuildContext context) {
    double height = MediaQuery.of(context).size.height;
    double width = MediaQuery.of(context).size.width;

    return Container(
        child: Center(
      child: Column(
        children: [
          Padding(
              padding: EdgeInsets.all(8),
              child: TextField(
                //textfield=user can type in
                onChanged: (value) {
                  //value refers to whatever the user types in/query to pass in to filterSearch
                  filterSearchResults(
                      value); //SEMICOLON= STATEMENT,FUNCTION,RETURNING (RETURN SCAFFOLD)
                },
                decoration: InputDecoration(
                    labelText: "Search",
                    //COMMA BECAUSE THERE ARE SEVERAL ITEMS
                    hintText: "Search",
                    //the greyed out text
                    border: OutlineInputBorder(
                      borderRadius: BorderRadius.all(Radius.circular(25)),
                    )),
              )),
          Expanded(
              child: ListView.builder(
                  physics: ClampingScrollPhysics(),
                  itemCount: duplicateUniversities.length,
                  itemBuilder: (context, index) {
                    String universities =
                        duplicateUniversities.keys.elementAt(index);
                    return Padding(
                        padding: EdgeInsets.all(8),
                        child: Card(
                            child: ListTile(
                                title: Text(
                                  universities,
                                  style: seen.contains(universities)
                                      ? TextStyle(color: Colors.blue)
                                      : TextStyle(),
                                ),
                                trailing: IconButton(
                                  onPressed: () {
                                    setState(() {
                                      seen.add(universities);
                                    });

                                    setSeen(seen, keySharePref);
                                    Navigator.push(
                                        context,
                                        MaterialPageRoute(
                                            builder: (BuildContext context) =>
                                                universityDetails(
                                                    universityInfo:
                                                        duplicateUniversities[
                                                            universities],
                                                    universityName:
                                                        universities)));
                                  },
                                  icon: Icon(Icons.arrow_forward),
                                ))));
                  }))
        ],
      ),
    ));
  }
}
