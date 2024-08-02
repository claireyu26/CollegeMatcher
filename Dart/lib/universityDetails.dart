import 'package:flutter/material.dart';
import 'buildingImage.dart';
import 'schoolImages.dart';


class universityDetails extends StatefulWidget {
  const universityDetails(
      {Key? key, required this.universityInfo, required this.universityName})
      : super(
            key:
                key); //Key? is always required and usually passed in already, this.info is a variable to pass in,

  final Map universityInfo;
  final String universityName;

  @override
  State<universityDetails> createState() => _universityDetailsState();
}

class _universityDetailsState extends State<universityDetails> {
  @override
  Widget build(BuildContext context) {
    double height = MediaQuery.of(context).size.height;
    double width = MediaQuery.of(context).size.width;

    return Scaffold(
        appBar: AppBar(
          title: Text(widget.universityName, style: TextStyle(fontSize: 30, color: Color.fromRGBO(255, 255, 255, 1.0))),
          backgroundColor: Color.fromRGBO(129, 155, 218, 1.0),
        ),
        body: Center(
            child: SingleChildScrollView(
                child: Padding(
          padding: EdgeInsets.all(8),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Padding(
                padding: const EdgeInsets.all(8.0),
                child: Text(widget.universityInfo["desc"]),
              ),
              Padding(
                padding: const EdgeInsets.all(8.0),
                child:
                    Text(widget.universityInfo["images"]["formatted_address"]),
              ),
              Container(
                  color: Color.fromRGBO(129, 155, 218, 1.0),
                  //possibly copy starting here
                  height: height * 0.3,
                  width: width * 0.9,
                  child: Padding(
                    padding: const EdgeInsets.symmetric(
                        horizontal: 8.0, vertical: 8.0),
                    child: ListView(
                      physics: ClampingScrollPhysics(),
                      shrinkWrap: true,
                      children: [
                        Text("Buildings"),
                        Container(height: 5),
                        ListView.builder(
                            physics: ClampingScrollPhysics(),
                            shrinkWrap: true,
                            itemCount: widget.universityInfo["school_images"]
                                .length, //change!!
                            itemBuilder: (context, index) {
                              String buildingName = widget
                                  .universityInfo["school_images"].keys
                                  .elementAt(index); //change location
                              List url = widget.universityInfo["school_images"]
                                  [buildingName]; // change
                              return Padding(
                                  padding: EdgeInsets.all(8),
                                  child: Card(
                                      child: ListTile(
                                          title: Text(buildingName),
                                          trailing: IconButton(
                                            onPressed: () {
                                              Navigator.push(
                                                  context,
                                                  MaterialPageRoute(
                                                      builder: (BuildContext
                                                              context) =>
                                                          schoolImages(
                                                              buildingName:
                                                                  buildingName,
                                                              university: widget
                                                                  .universityName,
                                                              images: url)));
                                            },
                                            icon: Icon(Icons.arrow_forward),
                                          ))));
                            }),
                      ],
                    ),
                  )),
              SizedBox(
                height: height * 0.5,
                child: Padding(
                  padding: const EdgeInsets.all(8.0),
                  child: ListView(
                    shrinkWrap: true,
                    children: [
                      Text("Nearby places"),
                      ListView.builder(
                          physics: ClampingScrollPhysics(),
                          shrinkWrap: true,
                          itemCount: widget
                              .universityInfo["images"]["buildings"]
                              .length, //change!!
                          itemBuilder: (context, index) {
                            String university = widget.universityInfo["images"]
                                ["buildings"][index]["name"]; //change location
                            String url = widget.universityInfo["images"]
                                ["buildings"][index]["photoUrl"]??"There are no images available."; // change
                            return Padding(
                                padding: EdgeInsets.all(8),
                                child: Card(
                                    child: ListTile(
                                        title: Text(university),
                                        trailing: IconButton(
                                          onPressed: () {
                                            Navigator.push(
                                                context,
                                                MaterialPageRoute(
                                                    builder: (BuildContext
                                                            context) =>
                                                        buildingImage(
                                                            buildingName:
                                                                university,
                                                            university:
                                                                widget.universityName,
                                                            images: url)));
                                          },
                                          icon: Icon(Icons.arrow_forward),
                                        ))));
                          }),
                    ],
                  ),
                ),
              ),
            ],
          ),
        ))));
  }
}
