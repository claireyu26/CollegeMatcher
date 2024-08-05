import 'package:flutter/material.dart';
import 'package:university_project/universityList.dart';
import 'universityDetails.dart';

class AllUniversityList extends StatefulWidget {
  const AllUniversityList({Key? key,required this.universities}): super(key: key);//Key? is always required and usually passed in already, this.info is a variable to pass in,

  final Map universities;

  @override
  State<AllUniversityList> createState() => _AllUniversityListState();
}

class _AllUniversityListState extends State<AllUniversityList> {
  Map duplicateUniversities={}; //static variables vs setting variable equal to another variable //can't set it equal to unviersities here bc it doesn't exist yet


  @override

  Widget build(BuildContext context) {
    double height=MediaQuery.of(context).size.height;
    double width=MediaQuery.of(context).size.width;

    return Scaffold(
        appBar: AppBar(
          leading: IconButton(
            icon: Icon(Icons.arrow_back_ios_new_rounded, color: Colors.white),
            onPressed: (){
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
                  'Search',
                  style: TextStyle(color: Colors.white),
                ),
              )
            ],
          ),
        ),

        body: universityList(universities: widget.universities)
    );

  }
}
