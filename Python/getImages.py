#3/9/24
import os
import requests
from bs4 import BeautifulSoup
import re
# import regular expression
import urllib.request
from universities import school_list
from database import data
from buildings import getUniversityBuildings
import certifi
import ssl

#default variable= if you don't put an argument for function paramaters, will default to default variable
#=5 is default variable
def getOriginalImages(query,maximages=10):
    makeDir("Images")
    headers = {
        "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36"
    }
    params={"q":query, "tbm":"isch", "hl":"en", "gl":"us", "ijn":"0"
            }
    #ijn is using the 0st page
    #query is what you're searching
    #hl is english language, gl is country searching from

    certifi_context = ssl.create_default_context(cafile=certifi.where()) #added 5/26

    url= requests.get("https://www.google.com/search", params=params, headers=headers,timeout=30, verify=certifi_context) #verify=certifi_context added 5/26/24 sunday 1 hr class w Patrick
    #if it doesn't work in 30 sec, then timeout/stop
    soup=BeautifulSoup(url.text, "lxml")
    #lxml is specific webpage format
    googleImages=[]#list of every image
    # print(soup.select("script"))
#3/16/24
    images = extractFullImages(soup.select("script"),maximages)

    for i in range(len(images)):
        #try and except
        try:
            #url lib is library
            #urlretrieve takes first parameter and saves it as the second parameter (location)
            urllib.request.urlretrieve(images[i],f'Images/{query}_{i}.jpg')#IT IS local_path in database.py (or elsewhere)!!!! like Images/'file name'
            googleImages.append(f'Images/{query}_{i}.jpg')
        except Exception as e:
            #e is the error that can be accessed
            print(e)
    return (googleImages[0:maximages])#googleImages is a list of the local paths of all the imagesa


#make directory
def makeDir(path):
    if not os.path.exists(path):
        os.mkdir(path)

def extractFullImages(scriptTag, maximages):
    matched_images_data = "".join(
        re.findall(r"AF_initDataCallback\(([^<]+)\);", str(scriptTag)))
    #REGULAR EXPRESSION
    #any expression that has AF_initDataCallback^ < (or a combo or single of ^ <) inside scriptTag
    #[a-z]+ vs [a-z] -- the first is a can look for combination of letters vs the second is just a single letter
    #re.findall returns a list bc it can empty or have multiple matches
    #.join takes every string in a list and turns it into string
    #the "" before the join is the separator between the strings in the list 

    #r is used for regx = regular expression 
    #the 'r' means the the following is a "raw string", ie. backslash characters are treated literally instead of signifying special treatment of the following character.

    matched_google_image_data = re.findall(r'\"b-GRID_STATE0\"(.*)sideChannel:\s?{}}', matched_images_data)
    #sub = substitute
    removed_matched_google_images_thumbnails = re.sub(
        r'\[\"(https\:\/\/encrypted-tbn0\.gstatic\.com\/images\?.*?)\",\d+,\d+\]',
        "", str(matched_google_image_data))
    #removes the (lower quality ones?)/the copies for sure with ""
    matched_google_full_resolution_images = re.findall(
        r"(?:'|,),\[\"(https:|http.*?)\",\d+,\d+\]",
        removed_matched_google_images_thumbnails)
    #d+ means digits (0-9)
    full_res_images = [
        bytes(bytes(img, "ascii").decode("unicode-escape"),
              "ascii").decode("unicode-escape")
        for img in matched_google_full_resolution_images
    ]
    #LIST COMPREHENSION  x=[5,10,15] newList = [i+5 for i in x] newList = [10,15,20]
    #i+5 is the operation
    #shortened version
    #another example x=["5","10","15"] y=[int(i) for i in x]
    # print(full_res_images[:max_images])
    return (full_res_images) 

def saveImages(buildings,university):
    listUrl=[]
    for i in buildings:
        images=getOriginalImages(query=f"{i} building - {university}", maximages=4) #, maximages=4 added 5/18/24 1:45pm
        print(images)
        for local_path in images:
            url=data.upload_file(local_path,firebase_path=f'{university}/building_pictures/{local_path[7:]}') #indexing from 7 to the end of the local_path variable gets rid of Images/ so that firebase does not make a new collection of Images
            #url for each picture
            listUrl.append(url)
    return listUrl
#name of university/ building_pictures/ url
#currently, this is not used in firebase
if __name__=='__main__': 
    # for i in school_list:
    #     allBuildings=getUniversityBuildings(i)
    #     if allBuildings[0]==1:
    #         saveImages(allBuildings[1],i)
    #     else:
    #         allBuildingsCombined=[]
    #         for x in allBuildings[1]:
    #             allBuildingsCombined+=x #this works
    #         saveImages(allBuildingsCombined,i)

    #5/18/24 2:19 pm with Mrs. Marisabel - Trying to create a new thing under 'buildings' in firebase for each school that holds 4 images of each building of the school (like multiple angles)
    
    #edited 5/26

    #schoolList=['Virginia Tech']
    for i in school_list:
        allBuildings=getUniversityBuildings(i)
        print(allBuildings)
        print(i)
        for j in allBuildings[1]:
            allUrl=saveImages(j,i)

            print(allUrl)
            print(j)
        
            #data.setUniversityImages(i,{"Images": allUrl})
            

  