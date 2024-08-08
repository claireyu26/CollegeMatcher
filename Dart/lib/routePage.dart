import 'package:flutter/material.dart';

import 'favorites.dart';
import 'homePage.dart';
import 'recommendationPage.dart';

class routePage extends StatefulWidget {
  final Function(ThemeMode) onThemeChanged;

  const routePage({super.key, required this.onThemeChanged});

  @override
  State<routePage> createState() => _routePageState();
}

class _routePageState extends State<routePage> {
  int selectedIndex = 0;
  List<Widget>? widgetOptions;
  List<String> titles = ['Home', 'Favorites','Recommendations'];

  @override
  void initState() {
    super.initState();
    widgetOptions = [
      const homePage(),
      const FavoritePage(),
      //AllUniversityList(),
      recommendationPage(),
    ];
  }

  void widgetPressed(int index) {
    setState(() {
      selectedIndex = index;
    });
  }

  void _toggleTheme() {
    if (Theme.of(context).brightness == Brightness.dark) {
      widget.onThemeChanged(ThemeMode.light);
    } else {
      widget.onThemeChanged(ThemeMode.dark);
    }
  }

  @override
  Widget build(BuildContext context) {
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
                'images/CollegeMatcher_logo.png',
                fit: BoxFit.fitHeight,
              ),
            ),
            Padding(
              padding: EdgeInsets.only(top: 8.0),
              child: Text(
                titles[selectedIndex],
                style: TextStyle(color: Colors.white),
              ),
            )
          ],
        ),
        actions: [
          IconButton(
            icon: Icon(Theme.of(context).brightness == Brightness.dark
                ? Icons.brightness_7
                : Icons.brightness_2),
            onPressed: _toggleTheme,
          ),
        ],
      ),
      body: Center(
        child: widgetOptions!.elementAt(selectedIndex),
      ),
      bottomNavigationBar: BottomNavigationBar(
        backgroundColor: Color.fromRGBO(183, 188, 203, 1),
        type: BottomNavigationBarType.fixed,
        items: const [
          BottomNavigationBarItem(icon: Icon(Icons.home), label: "Home"),
          BottomNavigationBarItem(
              icon: Icon(Icons.favorite), label: "Favorites"),
        //  BottomNavigationBarItem(
             // icon: Icon(Icons.search), label: "Search"),
          BottomNavigationBarItem(
              icon: Icon(Icons.school), label: "Recommendations")
        ],
        currentIndex: selectedIndex,
        selectedItemColor: const Color.fromRGBO(255, 255, 255, 1),
        onTap: widgetPressed,
      ),
    );
  }
}
