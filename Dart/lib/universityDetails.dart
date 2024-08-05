import 'package:flutter/material.dart';
import 'package:university_project/seenPlaces.dart';

import 'buildingImage.dart';
import 'favotiteManager.dart';
import 'schoolImages.dart';

class universityDetails extends StatefulWidget {
  const universityDetails(
      {Key? key, required this.universityInfo, required this.universityName})
      : super(key: key);

  final Map universityInfo;
  final String universityName;

  @override
  State<universityDetails> createState() => _universityDetailsState();
}

class _universityDetailsState extends State<universityDetails> {
  late FavoritesManager _favoritesManager;
  String nearbySharePref = "nearby";
  String buildingSharePref = "building";
  Set nearby = {};
  Set building = {};

  @override
  void initState() {
    super.initState();
    _favoritesManager = FavoritesManager();
    _favoritesManager.addListener(_updateState);
    seenPlace(nearbySharePref).then((value) {
      setState(() {
        nearby = value;
      });
    });
    seenPlace(buildingSharePref).then((value) {
      setState(() {
        building = value;
      });
    });
  }

  @override
  void dispose() {
    super.dispose();
  }

  void _updateState() {
    setState(() {});
  }

  @override
  Widget build(BuildContext context) {
    double height = MediaQuery.of(context).size.height;
    double width = MediaQuery.of(context).size.width;
    bool isFavorite = _favoritesManager.isFavorite(widget.universityName);

    return Scaffold(
        appBar: AppBar(
          leading: IconButton(
            icon: const Icon(Icons.arrow_back_ios_new_rounded,
                color: Colors.white),
            onPressed: () {
              Navigator.pop(context, isFavorite); // Return the favorite state
            },
          ),
          automaticallyImplyLeading: false,
          title: Text(widget.universityName,
              style: const TextStyle(
                  fontSize: 30, color: Color.fromRGBO(255, 255, 255, 1.0))),
          backgroundColor: const Color.fromRGBO(129, 155, 218, 1.0),
          actions: [
            IconButton(
              icon: isFavorite
                  ? const Icon(Icons.favorite, color: Colors.white)
                  : const Icon(Icons.favorite_border, color: Colors.white),
              onPressed: () {
                if (isFavorite) {
                  _favoritesManager.removeFavorite(widget.universityName);
                } else {
                  _favoritesManager.addFavorite(widget.universityName);
                }
              },
            ),
          ],
        ),
        body: Center(
            child: SingleChildScrollView(
                child: Padding(
          padding: const EdgeInsets.all(8),
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
                  color: const Color.fromRGBO(129, 155, 218, 1.0),
                  height: height * 0.3,
                  width: width * 0.9,
                  child: Padding(
                    padding: const EdgeInsets.symmetric(
                        horizontal: 8.0, vertical: 8.0),
                    child: ListView(
                      physics: const ClampingScrollPhysics(),
                      shrinkWrap: true,
                      children: [
                        const Text("Buildings"),
                        Container(height: 5),
                        widget.universityInfo.containsKey('school_images')
                            ? ListView.builder(
                                physics: const ClampingScrollPhysics(),
                                shrinkWrap: true,
                                itemCount: widget
                                    .universityInfo["school_images"].length,
                                itemBuilder: (context, index) {
                                  String buildingName = widget
                                      .universityInfo["school_images"].keys
                                      .elementAt(index);
                                  List url =
                                      widget.universityInfo["school_images"]
                                          [buildingName];
                                  return Padding(
                                      padding: const EdgeInsets.all(8),
                                      child: Card(
                                          child: ListTile(
                                              title: Text(buildingName,
                                                  style: building.contains(
                                                          buildingName)
                                                      ? const TextStyle(
                                                          color: Colors.blue)
                                                      : const TextStyle()),
                                              trailing: IconButton(
                                                onPressed: () {
                                                  setState(() {
                                                    building.add(buildingName);
                                                  });
                                                  setSeen(building,
                                                      buildingSharePref);
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
                                                                  images:
                                                                      url)));
                                                },
                                                icon: const Icon(
                                                    Icons.arrow_forward),
                                              ))));
                                })
                            : Column(
                                children: [
                                  SizedBox(
                                    height: height * 0.05,
                                  ),
                                  const Center(
                                    child: Text('No images available',
                                        style: TextStyle(
                                            fontSize: 20,
                                            fontStyle: FontStyle.italic)),
                                  ),
                                ],
                              ),
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
                      const Text("Nearby places"),
                      ListView.builder(
                          physics: const ClampingScrollPhysics(),
                          shrinkWrap: true,
                          itemCount: widget
                              .universityInfo["images"]["buildings"].length,
                          itemBuilder: (context, index) {
                            String university = widget.universityInfo["images"]
                                ["buildings"][index]["name"];
                            String url = widget.universityInfo["images"]
                                    ["buildings"][index]["photoUrl"] ??
                                "There are no images available.";
                            return Padding(
                                padding: const EdgeInsets.all(8),
                                child: Card(
                                    child: ListTile(
                                        title: Text(university,
                                            style: nearby.contains(university)
                                                ? const TextStyle(
                                                    color: Colors.blue)
                                                : const TextStyle()),
                                        trailing: IconButton(
                                          onPressed: () {
                                            setState(() {
                                              nearby.add(university);
                                            });
                                            setSeen(nearby, nearbySharePref);
                                            Navigator.push(
                                                context,
                                                MaterialPageRoute(
                                                    builder: (BuildContext context) => buildingImage(
                                                        latitude: widget.universityInfo["images"]
                                                                ["buildings"]
                                                            [index]["lat"],
                                                        longitude:
                                                            widget.universityInfo[
                                                                        "images"]
                                                                    ["buildings"]
                                                                [index]["lng"],
                                                        buildingName:
                                                            university,
                                                        university:
                                                            widget.universityName,
                                                        images: url)));
                                          },
                                          icon: const Icon(Icons.arrow_forward),
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
