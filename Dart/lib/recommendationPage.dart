import 'package:flutter/material.dart';

import 'recommendationResults.dart';

class recommendationPage extends StatefulWidget {
  @override
  _recommendationPageState createState() => _recommendationPageState();
}

class _recommendationPageState extends State<recommendationPage> {
  List<List<TextEditingController>> allControllers = [];
  int currentIndex = 0;

  @override
  void initState() {
    super.initState();
    // Initialize controllers for each section
    allControllers.add([TextEditingController()]); // Stats
    allControllers.add([TextEditingController()]); // Extracurriculars
    allControllers.add([TextEditingController()]); // Major
    allControllers.add([TextEditingController()]); // Awards
    allControllers.add([TextEditingController()]); // Specified Range Schools
    allControllers.add([TextEditingController()]); // Others
  }

  @override
  void dispose() {
    for (var controllers in allControllers) {
      for (var controller in controllers) {
        controller.dispose();
      }
    }
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: SingleChildScrollView(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(
                'Provide the details below to receive personalized university recommendations:',
                style: const TextStyle(
                    fontSize: 20,
                    fontWeight: FontWeight.bold,
                    fontStyle: FontStyle.italic),
              ),
              const SizedBox(height: 20),
              buildCurrentSection(),
              const SizedBox(height: 20),
              Center(
                child: Text(
                  ' ${currentIndex + 1} of ${allControllers.length}',
                  style: const TextStyle(
                      fontSize: 16, fontWeight: FontWeight.bold),
                ),
              ),
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  ElevatedButton(
                    style: TextButton.styleFrom(
                        backgroundColor: currentIndex == 0
                            ? Colors.grey
                            : const Color.fromRGBO(183, 188, 203, 1)),
                    onPressed: currentIndex == 0
                        ? null
                        : () {
                            setState(() {
                              currentIndex--;
                            });
                          },
                    child: const Text(
                      'Previous',
                      style: TextStyle(color: Colors.black54),
                    ),
                  ),
                  ElevatedButton(
                    style: TextButton.styleFrom(
                        backgroundColor:
                            currentIndex < allControllers.length - 1
                                ? const Color.fromRGBO(183, 188, 203, 1)
                                : Colors.grey),
                    onPressed: currentIndex < allControllers.length - 1
                        ? () {
                            setState(() {
                              currentIndex++;
                            });
                          }
                        : null,
                    child: const Text(
                      'Next',
                      style: TextStyle(color: Colors.black54),
                    ),
                  ),
                ],
              ),
              Center(
                child: ElevatedButton(
                  style: TextButton.styleFrom(
                      backgroundColor: const Color.fromRGBO(183, 188, 203, 1)),
                  onPressed: () {
                    // Save data and navigate to next screen
                    // For simplicity, just print the entered data here
                    String data = getAllData();
                    Navigator.push(
                        context,
                        MaterialPageRoute(
                            builder: (BuildContext context) =>
                                recommendationResults(info: data)));
                  },
                  child: const Text(
                    'Submit',
                    style: TextStyle(color: Colors.black54),
                  ),
                ),
              )
            ],
          ),
        ),
      ),
    );
  }

  Widget buildCurrentSection() {
    String title;
    List<TextEditingController> controllers;

    switch (currentIndex) {
      case 0:
        title = 'Stats:';
        controllers = allControllers[currentIndex];
        break;
      case 1:
        title = 'Extracurriculars:';
        controllers = allControllers[currentIndex];
        break;
      case 2:
        title = 'Aspiring Major:';
        controllers = allControllers[currentIndex];
        break;
      case 3:
        title = 'Awards:';
        controllers = allControllers[currentIndex];
        break;
      case 4:
        title = 'Specified Range Schools:';
        controllers = allControllers[currentIndex];
        break;
      case 5:
        title = 'Others:';
        controllers = allControllers[currentIndex];
        break;
      default:
        title = '';
        controllers = [];
    }

    return buildSection(title, controllers);
  }

  Widget buildSection(String title, List<TextEditingController> controllers) {
    return Card(
      color: const Color.fromRGBO(183, 188, 203, 1),
      child: Padding(
        padding: const EdgeInsets.all(8.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              title,
              style: const TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
            ),
            const SizedBox(height: 10),
            Column(
              children: controllers.map((controller) {
                return Card(
                  child: Padding(
                    padding: const EdgeInsets.symmetric(vertical: 8.0),
                    child: TextField(
                      maxLines: 3,
                      controller: controller,
                      decoration: const InputDecoration(
                        contentPadding: EdgeInsets.symmetric(horizontal: 10.0),
                        border: InputBorder.none,
                        hintText: 'Enter Text',
                      ),
                    ),
                  ),
                );
              }).toList(),
            ),
            Align(
              alignment: Alignment.centerRight,
              child: IconButton(
                onPressed: () {
                  setState(() {
                    controllers.add(TextEditingController());
                  });
                },
                icon: const Icon(Icons.add_box_outlined),
              ),
            ),
            const SizedBox(height: 20),
          ],
        ),
      ),
    );
  }

  String getAllData() {
    String data = '';
    for (var controllers in allControllers) {
      for (var controller in controllers) {
        data += controller.text + '\n';
      }
    }
    return data;
  }
}
