import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';

class FavoritesManager with ChangeNotifier {
  List<String> _favorites = [];
  SharedPreferences? _prefs;

  FavoritesManager() {
    loadFavorites();
  }

  List<String> get favorites => _favorites;

  Future<void> loadFavorites() async {
    _prefs = await SharedPreferences.getInstance();
    _favorites = _prefs?.getStringList('favorites') ?? [];
    print(_favorites);
    notifyListeners();
  }

  Future<void> addFavorite(String universityName) async {
    if (!_favorites.contains(universityName)) {
      _favorites.add(universityName);
      await _prefs?.setStringList('favorites', _favorites);
      notifyListeners();
    }
  }

  Future<void> removeFavorite(String universityName) async {
    if (_favorites.contains(universityName)) {
      _favorites.remove(universityName);
      await _prefs?.setStringList('favorites', _favorites);
      notifyListeners();
    }
  }

  bool isFavorite(String universityName) {
    return _favorites.contains(universityName);
  }
}
