import 'package:flutter/material.dart';

class schoolImages extends StatefulWidget {
  const schoolImages({Key? key,required this.university,required this.buildingName,required this.images}): super(key: key);//Key? is always required and usually passed in already, this.info is a variable to pass in,

  final String buildingName;
  final List images;
  final String university;

  @override
  State<schoolImages> createState() => _schoolImagesState();
}

class _schoolImagesState extends State<schoolImages> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text(widget.university, style: TextStyle(fontSize: 30, color: Color.fromRGBO(255, 255, 255, 1.0))),
          backgroundColor: Color.fromRGBO(129, 155, 218, 1.0),
        ),
        body: SingleChildScrollView(
          child: Column(
              children:[
                Text(widget.buildingName,
                    style: TextStyle(fontSize: 30)
                ),
                ListView.builder(
                  physics: ClampingScrollPhysics(),
                  shrinkWrap: true,
                  itemCount: widget.images.length,
                  itemBuilder: (context,index){
                    return Padding(
                        padding: EdgeInsets.all(8),
                        child: Card(
                          child: Image.network(widget.images[index],height: 200),
                        )
                    );
                  },
                )
              ]
          ),
        )

    );
  }

}
