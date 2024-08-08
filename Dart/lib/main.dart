import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/material.dart';
import 'package:flutter_dotenv/flutter_dotenv.dart';
import 'package:shared_preferences/shared_preferences.dart';

import 'splashScreen.dart';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized(); //added 5/26/24 w Patrick
  await Firebase.initializeApp();
  await dotenv.load(fileName: "images/.env");

  WidgetsFlutterBinding.ensureInitialized();
  final ThemeMode themeMode = await loadThemeFromPreferences();
  runApp(MyApp(initialThemeMode: themeMode));
}

Future<ThemeMode> loadThemeFromPreferences() async {
  final SharedPreferences prefs = await SharedPreferences.getInstance();
  final String? theme = prefs.getString('themeMode');
  switch (theme) {
    case 'light':
      return ThemeMode.light;
    case 'dark':
      return ThemeMode.dark;
    default:
      return ThemeMode.system;
  }
}
class MyApp extends StatefulWidget {
  final ThemeMode initialThemeMode;

  MyApp({required this.initialThemeMode});

  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  ThemeMode _themeMode;

  _MyAppState() : _themeMode = ThemeMode.system;

  @override
  void initState() {
    super.initState();
    _themeMode = widget.initialThemeMode;
  }

  void _saveThemeMode(ThemeMode themeMode) async {
    final SharedPreferences prefs = await SharedPreferences.getInstance();
    String theme = 'system';
    if (themeMode == ThemeMode.light) {
      theme = 'light';
    } else if (themeMode == ThemeMode.dark) {
      theme = 'dark';
    }
    prefs.setString('themeMode', theme);
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'CollegeMatcher',
      theme: ThemeData.light(),
      darkTheme: ThemeData.dark(),
      themeMode: _themeMode,
      home: splashScreen(
        onThemeChanged: (ThemeMode themeMode) {
          setState(() {
            _themeMode = themeMode;
            _saveThemeMode(themeMode);
          });
        },
      ),
    );
  }
}