import firebase_admin
from firebase_admin import credentials, storage, firestore
from descriptions import getInfo
from universities import school_list
from universityGoogleAPI import getNearbyBuildings

#Firebase Storage Setup and Usage with Python
class StorageManager:
  def __init__(self):
      project_id = 'university-fc3d9' 
      self.bucket_name = f'{project_id}.appspot.com'
      self.fb_cred_path = 'university-fc3d9-firebase-adminsdk-yddzw-c0c390286f.json'

      # Initialize Firebase Admin SDK
      cred = credentials.Certificate(self.fb_cred_path)
      firebase_admin.initialize_app(cred, {
          'storageBucket': self.bucket_name
      })
      self.db=firestore.client()
      
  def exists_on_cloud(self, file_name):
      bucket = storage.bucket()
      blob = bucket.blob(file_name)
      if blob.exists():
         return blob.public_url
      else:
         return False
      
    #.exists() returns true or false
#.public_url reutrns link to image if exists

  def upload_file(self, file_name, firebase_path): #whats the point of this
    bucket = storage.bucket()
    blob = bucket.blob(file_name)#reference to a file 
    blob.upload_from_filename(firebase_path)
    print('This file is uploaded to cloud.')
    blob.make_public()
    return blob.public_url

  #puts every school's description information that was gathered in descriptions.py into the database
  def updateData(self):
    for i in school_list:
        doc=self.db.collection(i).document("descriptions")
        doc.create({
           "desc": getInfo(i)
        })

#   def updateSchool(self,university):
#      doc=self.db.collection(university).document("descriptions")
#      doc.create({
#         "desc": getInfo(university)
#      })
  def updateSchool(self,university):
     doc=self.db.collection("Universities").document(university)
     doc.update({
        "desc": getInfo(university)
     })

  def delete(self):#whats the point of this delete
     for i in school_list:
        toDelete=self.db.collection(i).document("descriptions")
        toDelete.delete()
        #first do doc.create to set it up in firestore, then can change it to update afterwards   
        
#updated 3/9/24
#   def setUniversityImages(self, university, data):
#     collection=self.db.collection(university).document("buildings")
#     collection.set(data, merge=True) #.set() = if theres already a collection or document then add to it
  def setUniversityImages(self, university, data):
    collection=self.db.collection("Universities").document(university)
    collection.set({"school_images":data}) #.set() = if theres already a collection or document then add to it

    #for all the schools, just comment out for now
data=StorageManager()

if __name__=='__main__': 
   # for i in school_list:
   #   print(i)
   #   data.setUniversityImages(i, getNearbyBuildings(i))
   for i in school_list:
     print(i)
     data.setUniversityImages(i, getNearbyBuildings(i))
     data.updateSchool(i)
   

   

# data.updateSchool("Virginia Tech")

