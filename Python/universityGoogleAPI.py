#2/25/24
#3/2/24
import requests
from universities import school_list
import json

#api_key="AIzaSyASybuNbMls86eHzVd4JVSraLVgK1Yvxgg"
api_key="AIzaSyC6soeX4oFhvfw4wiC1LhtDk-pr7nDf6QI" #new api key made 5/18 with marisabel

def getNearbyBuildings(university):
    return(getSchoolInfo(university))
def getSchoolInfo(university):
    #uses google apis to put all of the school information into our own dictionary called location
#    url=f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?key=AIzaSyASybuNbMls86eHzVd4JVSraLVgK1Yvxgg&input={university}&inputtype=textquery&fields=name,formatted_address,geometry"

    url=f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?key={api_key}&input={university}&inputtype=textquery&fields=name,formatted_address,geometry"

    result=requests.get(url)
    result=json.loads(result.text)

    print(result)

    result=result["candidates"]

    correctCandidate=""
    #for loop and if is checking if it exists and finding the right location 
    for candidate in result:
        #print(candidate.keys())
        if candidate["name"]==university:
            correctCandidate=candidate
            
    if correctCandidate=="":
        #print(result)
        correctCandidate=result[0]
    location={}
    location["name"]=correctCandidate["name"] #school name
    location["formatted_address"]=correctCandidate["formatted_address"] #school address
    #print(correctCandidate.keys())
    location["coordinates"]=correctCandidate["geometry"]["location"]
    location["buildings"]=nearbyPlaces(location)
    return(location)

def nearbyPlaces(location):
    lat=location["coordinates"]["lat"] #these are lat and lng of SCHOOL, not individual buildings 
    lng=location["coordinates"]["lng"]
#this url ranks the lat and lng by distance
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lng}&rankby=distance&key={api_key}"
    results=requests.get(url) # comes in as a well response, its own type
    results=json.loads(results.text)#.text makes it string, .loads turns a string dicitonary into an acutal dictionary
    #results is list of top 20 results
    buildings=[]

    #each of these results is its own separate building
    for building in results["results"]:
       # print(getPhotoReference(result["place_id"]))
        #print(result["photo_reference"])
        if "photos" in building.keys():
            photoUrl=(getPhotos(building["photos"][0]["photo_reference"]))
        else:
            photoUrl=None #places that don't have a picture

        buildings.append({"photoUrl":photoUrl, "lat":building["geometry"]["location"]["lat"], "lng":building["geometry"]["location"]["lng"], "name": building["name"], "placeId":building["place_id"]})
    return buildings
        
#this code got cut out because for result in results["results"] shortens it
            
# def getPhotoReference(place_id):
#     url=f"https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&key={api_key}"
#     result=requests.get(url) 
#     result=json.loads(result.text)
#     #print(result)
#     photos=result.get("result", {}).get("photos",[])
#     if photos!=[]:
#         return(getPhotos(photos[0]["photo_reference"]))
#     return None

def getPhotos(photoReference):
    url=f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference={photoReference}&key={api_key}"
    return url

if __name__=="__main__": 
    x=0
    schoolInfoDict={}
    for i in school_list:
        schoolInfo=getNearbyBuildings(i)
        schoolInfoDict[i]=schoolInfo
        x+=1
        print(x)

    with open("schoolInfo.json", "w") as outputFile:
        json.dump(schoolInfoDict, outputFile)


