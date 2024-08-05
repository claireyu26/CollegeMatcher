import 'package:shared_preferences/shared_preferences.dart';

Future<Set> seenPlace(key) async {
  SharedPreferences prefs = await SharedPreferences.getInstance();
  List tempSeen = prefs.getStringList(key) ?? [];
  return tempSeen.toSet();
}

Future<void> setSeen(Set seen, String key) async {
  SharedPreferences prefs = await SharedPreferences.getInstance();
  List<String> tempSeen = [];
  for (var element in seen) {
    tempSeen.add(element);
  }
  prefs.setStringList(key, tempSeen);
}
