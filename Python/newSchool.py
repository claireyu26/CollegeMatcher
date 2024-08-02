#file to update and get all the necessary information for a new school that is not already in the list that we want to add
from database import *
#from getImages import *
from universityGoogleAPI import *

#* means import everything

newSchool="Saint Joseph's University - Hawk Hill Campus"

schoolInfo=getNearbyBuildings(newSchool)

#shouldn't need to add to json

#data=StorageManager()
data.updateSchool(newSchool)
data.setUniversityImages(newSchool, schoolInfo)

