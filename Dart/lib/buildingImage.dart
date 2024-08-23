import 'package:flutter/material.dart';
import 'package:google_maps_flutter/google_maps_flutter.dart';

class buildingImage extends StatefulWidget {
  const buildingImage(
      {Key? key,
      required this.university,
      required this.buildingName,
      required this.images,
      required this.latitude,
      required this.longitude})
      : super(key: key);

  final String buildingName;
  final String images;
  final String university;
  final double latitude;
  final double longitude;

  @override
  State<buildingImage> createState() => _buildingImageState();
}

class _buildingImageState extends State<buildingImage> {
  late GoogleMapController mapController;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.buildingName, style: TextStyle(fontSize: 30)),
      ),
      body: Column(
        children: [
          widget.images != "There are no images available."
              ? Expanded(
                  child: Padding(
                    padding: const EdgeInsets.all(8.0),
                    child: Image.network(widget.images, height: 200),
                  ),
                )
              : Expanded(
                  child: Padding(
                    padding: const EdgeInsets.all(8.0),
                    child: SizedBox(
                        height: 200,
                        child: Card(
                            color: Color.fromRGBO(107, 153, 222, 1.0),
                            child: Padding(
                              padding: const EdgeInsets.all(8.0),
                              child: Text("There are no images available."),
                            ))),
                  ),
                ),
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: Text(
              widget.buildingName + " from " + widget.university,
              style: TextStyle(fontSize: 25),
            ),
          ),
          Expanded(
            flex: 2,
            child: Padding(
              padding: const EdgeInsets.all(8.0),
              child: GoogleMap(
                initialCameraPosition: CameraPosition(
                  target: LatLng(widget.latitude, widget.longitude),
                  zoom: 15.0,
                ),
                markers: {
                  Marker(
                    markerId: MarkerId(widget.buildingName),
                    position: LatLng(widget.latitude, widget.longitude),
                    infoWindow: InfoWindow(
                      title: widget.buildingName,
                      snippet: widget.university,
                    ),
                  ),
                },
                onMapCreated: (GoogleMapController controller) {
                  mapController = controller;
                },
              ),
            ),
          ),
        ],
      ),
    );
  }
}
