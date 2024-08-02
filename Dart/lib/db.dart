//for database
import 'package:cloud_firestore/cloud_firestore.dart';

Future<Map> getData() async {  //map is dictionary in python, Future = we have to wait for firebase to return answers
  var data={};
  await FirebaseFirestore.instance.collection("Universities").get().then((queriesSnapshot){//what we get is all the information in the db
    for (var DocSnapshot in queriesSnapshot.docs) {//docsnapshot is every university/doc
      data[DocSnapshot.id]=DocSnapshot.data();//id is the document/university name, and data is eveyrthing inside
    }
  });
  return data;
}