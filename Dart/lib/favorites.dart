import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:university_project/universityDetails.dart';

import 'db.dart';

class FavoritePage extends StatefulWidget {
  const FavoritePage({super.key});

  @override
  State<FavoritePage> createState() => _FavoritePageState();
}

class _FavoritePageState extends State<FavoritePage> {
  Map _favoriteUniversityInfo = {};
  bool isLoading = true;
  String keySharePref = "seen";
  Map allUniversities =
      {}; //static variables vs setting variable equal to another variable //can't set it equal to unviersities here bc it doesn't exist yet

  @override
  void initState() {
    //to get/connect to once opened up
    getUniversities();

    //always runs at the very beginning of app opening
    //starter code when the code that first runs when we first open app
    super
        .initState(); // still run the code that was originally in initstate, the normal code before overridden
  }


  void filterSearchResults(query) {
    _favoriteUniversityInfo =
        {}; //reset this duplicate map //list of matched universities based on input
    setState(() {
      //change
      allUniversities.forEach((university, value) {
        if (university.toLowerCase().contains(query.toLowerCase())) {
          //if the lowercased university contains the lowercase input
          _favoriteUniversityInfo[university] = value;
        }
      });
    });
  }

  Future<List<String>> loadFavorites() async {
    SharedPreferences _prefs = await SharedPreferences.getInstance();
    List<String> favorites = _prefs?.getStringList('favorites') ?? [];

    return favorites;
  }

  Future<void> getUniversities() async {
    getData().then((value) {
      allUniversities = value;
      setFavorites();
    });
  }

  Future<void> setFavorites() async {
    print('setting favorites');
    List<String> favorites = await loadFavorites();
    Map favoriteUniversities = {};
    for (String university in favorites) {
      favoriteUniversities[university] = allUniversities[university];
    }
    setState(() {
      _favoriteUniversityInfo = favoriteUniversities;
      isLoading = false;
    });
  }

  buildUniversityList() {
    return Container(
        child: Center(
      child: Column(
        children: [
          Padding(
              padding: const EdgeInsets.all(8),
              child: TextField(
                //textfield=user can type in
                onChanged: (value) {
                  //value refers to whatever the user types in/query to pass in to filterSearch
                  filterSearchResults(
                      value); //SEMICOLON= STATEMENT,FUNCTION,RETURNING (RETURN SCAFFOLD)
                },
                decoration: const InputDecoration(
                    labelText: "Search",
                    //COMMA BECAUSE THERE ARE SEVERAL ITEMS
                    hintText: "Search",
                    //the greyed out text
                    border: OutlineInputBorder(
                      borderRadius: BorderRadius.all(Radius.circular(25)),
                    )),
              )),
          Expanded(
              child: ListView.builder(
                  physics: const ClampingScrollPhysics(),
                  itemCount: _favoriteUniversityInfo.length,
                  itemBuilder: (context, index) {
                    String universities =
                        _favoriteUniversityInfo.keys.elementAt(index);
                    return Padding(
                        padding: const EdgeInsets.all(8),
                        child: Card(
                            child: ListTile(
                                title: Text(universities),
                                trailing: IconButton(
                                  onPressed: () {
                                    Navigator.push(
                                      context,
                                      MaterialPageRoute(
                                        builder: (BuildContext context) =>
                                            universityDetails(
                                          universityInfo:
                                              _favoriteUniversityInfo[
                                                  universities],
                                          universityName: universities,
                                        ),
                                      ),
                                    ).then((value) {
                                      if (value != null && value == false) {
                                        setState(() {
                                          _favoriteUniversityInfo
                                              .remove(universities);
                                        });
                                      }
                                    });
                                  },
                                  icon: const Icon(Icons.arrow_forward),
                                ))));
                  }))
        ],
      ),
    ));
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
          child:
              isLoading //?=if isLoading is true OR :means if isLoading is false
                  ? const Center(
                      child: Column(
                          mainAxisAlignment: MainAxisAlignment.center,
                          children: [CircularProgressIndicator()]))
                  : _favoriteUniversityInfo.isEmpty
                      ? const Center(
                          child: Text(
                            'No favorites yet!',
                            style: TextStyle(fontSize: 20),
                          ),
                        )
                      : buildUniversityList()),
    );
  }
}
