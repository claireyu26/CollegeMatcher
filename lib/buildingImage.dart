import 'package:flutter/material.dart';

class buildingImage extends StatefulWidget {
  const buildingImage({Key? key,required this.university, required this.buildingName,required this.images}): super(key: key);//Key? is always required and usually passed in already, this.info is a variable to pass in,

  final String buildingName;
  final String images;
  final String university;

  @override
  State<buildingImage> createState() => _buildingImageState();
}

class _buildingImageState extends State<buildingImage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar:AppBar(
        title:Text(widget.buildingName,
            style: TextStyle(fontSize: 30)
        ),
      ),
      body: Column(
        children:[
          widget.images!="There are no images available."?
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: Image.network(widget.images,height: 200),
          ):Padding(
            padding: const EdgeInsets.all(8.0),
            child: SizedBox(height:200,
            child:Card(color:Color.fromRGBO(107, 153, 222, 1.0), child: Padding(
              padding: const EdgeInsets.all(8.0),
              child: Text("There are no images available."),
            ))),
          ),
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: Text(widget.buildingName +" from " +widget.university,style:TextStyle(fontSize: 25)),
          )
        ]
      )

    );
  }

}
