import requests
from bs4 import BeautifulSoup
import urllib.request
import re 



def getUniversityBuildings(university):
    if university=="Alliant International University":
        return AlliantBuildings()
    elif university=="American University":
        return AmericanBuildings()
    elif university=="American Heritage University of Southern California":
        return AmericanHeritageBuildings()
    elif university=="American Jewish University":
        return AmericanJewishBuildings()
    elif university=="Andrews University":
        return AndrewsBuildings()
    elif university=="ArtCenter College of Design":
        return ArtCenterBuildings()
    elif university=="Bard College":
        return BardBuildings()
    elif university=="Barnard University":
        return BarnardBuildings()
    elif university=="Berklee College of Music":
        return BerkleeMusicBuildings()
    elif university=="Biola University":
        return BiolaBuildings()
    elif university=="Boston College":
        return BostonCollegeBuildings()
    elif university=="Boston University":
        return BostonUniBuildings()
    elif university=="Bowdoin College":
        return BowdoinBuildings()
    elif university=="Brandeis University":
        return BrandeisBuildings()
    elif university=="Brown University":
        return BrownBuildings()
    elif university=="California Institute of Integral Studies":
        return CIISBuildings()
    elif university=="California Institute of Technology":
        return CalTechBuildings()
    elif university=="California Institute of the Arts":
        return InstituteOfTheArtsBuildings()
    elif university=="California Miramar University":
        return MiramarBuildings()
    elif university=="California Polytechnic State University, Pomona":
        return CalPolyPomonaBuildings()
    elif university=="California South Bay University":
        return SouthBayBuildings()
    elif university=="California State University Channel Islands":
        return ChannelIslandsBuildings()
    elif university=="California State University San Marcos":
        return SanMarcosBuildings()
    elif university=="California State University, Bakersfield":
        return BakersfieldBuildings()
    elif university=="California State University, Chico":
        return ChicoBuildings()
    elif university=="California State University, East Bay":
        return EastBayBuildings()
    elif university=="California State University, Fresno":
        return FresnoBuildings()
    elif university =="California State University, Fullerton":
        return FullertonBuildings()
    elif university =="California State University, Los Angeles":
        return CalStateLABuildings()
    elif university =="California State University, Monterey Bay":
        return MontereyBayBuildings()
    elif university =="California State University, Northridge":
        return NorthridgeBuildings()
    elif university=="California State University, Sacramento":
        return SacramentoBuildings()
    elif university=="California State University, San Bernardino":
        return SanBernardinoBuildings()
    elif university=="California State University, Stanislaus":
        return StanislausBuildings()
    elif university=="Cambridge College":
        return CambridgeBuildings()
    elif university=="Carnegie Mellon University":
        return CMUBuildings()
    elif university=="Case Western Reserve University":
        return CaseWesternBuildings()
    elif university=="Chapman University":
        return ChapmanBuildings()
    elif university=="Charles R. Drew University of Medicine and Science":
        return CharlesDrewBuildings()
    elif university=="Claremont Graduate University":
        return ClaremontBuildings()
    elif university=="Claremont McKenna College":
        return ClaremontMcKennaBuildings()
    elif university=="Colby College":
        return ColbyBuildings()
    elif university=="Colgate University":
        return ColgateBuildings()
    elif university=="College of the Holy Cross":
        return HolyCrossBuildings()
    elif university=="Columbia University":
        return ColumbiaBuildings()
    elif university=="Concordia University Irvine":
        return ConcordiaBuildings()
    elif university=="Cornell University":
        return CornellBuildings()
    elif university=="Dartmouth College":
        return DartmouthBuildings()
    elif university=="Dominican University of California":
        return DominicanBuildings()
    elif university=="Drexel University":
        return DrexelBuildings()
    elif university=="Duke University":
        return DukeBuildings()
    elif university=="Eckerd College":
        return EckerdBuildings()
    elif university=="Emory University":
        return EmoryBuildings()
    elif university=="Florida State University":
        return FloridaStateBuildings()
    elif university=="Franklin & Marshall College":
        return FranklinMarshallBuildings()
    elif university=="Georgia Institute of Technology":
        return GeorgiaTechBuildings()
    elif university=="George Mason University":
        return GeorgeMasonBuildings()
    elif university=="George Washington University":
        return GeorgeWashingtonBuildings()
    elif university=="Georgetown University":
        return GeorgetownBuildings()
    elif university=="Graduate Theological Union":
        return GraduateTheologicalBuildings()
    elif university=="Grinnell College":
        return GrinnellBuildings()
    elif university=="Hamilton College":
        return HamiltonBuildings()
    elif university=="Harvard University":
        return HarvardBuildings()
    elif university=="Harvey Mudd College":
        return HarveyMuddBuildings()
    elif university=="Haverford College":
        return HaverfordBuildings()
    elif university=="Holy Names University":
        return HolyNamesBuildings()
    elif university=="Howard University":
        return HowardBuildings()
    elif university=="Humphreys University":
        return HumphreysBuildings()
    elif university=="Illinois Institute of Technology":
        return IllinoisTechBuildings()
    elif university=="Indiana University Bloomington":
        return IndianaBloomingtonBuildings()
    elif university=="Johns Hopkins University":
        return JohnsHopkinsUniversity()
    elif university=="La Sierra University":
        return LaSierraBuildings()
    elif university=="Laguna College of Art and Design":
        return LagunaBuildings()
    elif university=="Lehigh University":
        return LehighBuildings()
    elif university=="Loyola Marymount University":
        return LoyolaMarymountBuildings()
    elif university=="Menlo College":
        return MenloCollegeBuildings()
    elif university=="Michigan State University":
        return MichiganStateBuildings()
    elif university=="Middlebury College":
        return MiddleburyBuildings()
    elif university=="National University":
        return NationalBuildings()
    elif university=="New York University":
        return NYUBuildings()
    elif university=="North Carolina State University":
        return NorthCarolinaStateBuildings()
    elif university=="Northeastern University":
        return NortheasternBuildings()
    elif university=="Northwestern Polytechnic University":
        return NWPolytechnicBuildings()
    elif university=="Northwestern University":
        return NorthwesternBuildings()
    elif university=="Notre Dame de Namur University":
        return NotreDameBuildings()
    elif university=="Oak Valley College":
        return OakValleyBuildings()
    elif university=="Oberlin College":
        return OberlinBuildings()
    elif university=="Occidental College":
        return OccidentalBuildings()
    elif university=="Otis College of Art and Design":
        return OtisCollegeBuildings()
    elif university=="Pacific Lutheran Theological Seminary":
        return PacificLutheranBuildings()
    elif university=="Pacific Oaks College":
        return PacificOaksBuildings()
    elif university=="Pacific School of Religion":
        return PacificReligionBuildings()
    elif university=="Pacific Union College":
        return PacificUnionBuildings()
    elif university=="Pacifica Graduate Institute":
        return PacificaGraduateBuildings()
    elif university=="Palo Alto University":
        return PaloAltoBuildings()
    elif university=="Pennsylvania State University":
        return PennStateBuildings()
    elif university=="Pepperdine University":
        return PepperdineBuildings()
    elif university=="Pitzer College":
        return PitzerBuildings()
    elif university=="Point Loma Nazarene University":
        return PointLomaBuildings()
    elif university=="Pomona College":
        return PomonaCollegeBuildings()
    elif university=="Princeton University":
        return PrincetonBuildings()
    elif university=="Providence Christian College":
        return ProvidenceChristianBuildings()
    elif university=="Purdue University":
        return PurdueBuildings()
    elif university=="Rensselaer Polytechnic Institute":
        return RensselaerBuildings()
    elif university=="Rhode Island School of Design":
        return RhodeIslandDesignBuildings()
    elif university=="Rice University":
        return RiceBuildings()
    elif university=="Rochester Institute of Technology":
        return RochesterTechBuildings()
    elif university=="Rutgers University":
        return RutgersBuildings()
    elif university=="Saint Joseph's University - Hawk Hill Campus":
        return SaintJosephHawkHillBuildings()
    elif university=="Saint Mary's College of California":
        return SaintMaryBuildings()
    elif university=="Samuel Merritt University":
        return SamuelMerrittBuildings()
    elif university=="San Diego Christian College":
        return SanDiegoChristianBuildings()
    elif university=="San Diego State University":
        return SanDiegoStateBuildings()
    elif university=="San Francisco State University":
        return SanFranciscoStateBuildings()
    elif university=="San Joaquin College of Law":
        return SanJoaquinBuildings()
    elif university=="Santa Clara University":
        return SantaClaraBuildings()
    elif university=="Saybrook University":
        return SaybrookBuildings()
    elif university=="Scripps College":
        return ScrippsBuildings()
    elif university=="Simpson University":
        return SimpsonBuildings()
    elif university=="Smith College":
        return SmithBuildings()
    elif university=="Soka University of America":
        return SokaBuildings()
    elif university=="Sonoma State University":
        return SonomaStateBuildings()
    elif university=="Southern Methodist University":
        return SouthernMethodistBuildings()
    elif university=="Southwestern Law School":
        return SouthwesternLawBuildings()
    elif university=="Stanford University":
        return StanfordBuildings()
    elif university=="Swathmore College":
        return SwathmoreBuildings()
    elif university=="Syracuse University":
        return SyracuseBuildings()
    elif university=="Temple University":
        return TempleBuildings()
    elif university=="Texas A&M University":
        return TexasAMBuildings()
    elif university=="The College of New Jersey":
        return CollegeOfNJBuildings()
    elif university=="The Master's University":
        return MastersBuildings()
    elif university=="The New School":
        return NewSchoolBuildings()
    elif university=="Thomas Aquinas College":
        return ThomasAquinasBuildings()
    elif university=="Touro University California":
        return TouroBuildings()
    elif university=="Tufts University":
        return TuftsBuildings()
    elif university=="Tulane University":
        return TulaneBuildings()
    elif university=="University of Chicago":
        return ChicagoBuildings()
    elif university=="University of Colorado Boulder":
        return ColoradoBoulderBuildings()
    elif university=="University of Colorado Denver":
        return ColoradoDenverBuildings()
    elif university=="University of Connecticut":
        return ConnecticutBuildings()
    elif university=="University of Delaware":
        return DelawareBuildings()
    elif university=="University of Denver":
        return DenverBuildings()
    elif university=="University of Florida":
        return FloridaBuildings()
    elif university=="University of Hawaii at Manoa":
        return HawaiiManoaBuildings()
    elif university=="University of Houston":
        return HoustonBuildings()
    elif university=="University of Kentucky":
        return KentuckyBuildings()
    elif university=="University of La Verne":
        return LaVerneBuildings()
    elif university=="University of Louisville":
        return LouisvilleBuildings()
    elif university=="University of Maryland":
        return MarylandBuildings()
    elif university=="University of Maryland, Baltimore County":
        return MarylandBaltimoreCountyBuildings()
    elif university=="University of Massachusetts Amherst":
        return MassachusettsAmherstBuildings()
    elif university=="University of Miami":
        return MiamiBuildings()
    elif university=="University of Michigan":
        return MichiganBuildings()
    elif university=="University of North Carolina at Chapel Hill":
        return NorthCarolinaChapelHillBuildings()
    elif university=="University of Notre Dame":
        return NotreDameBuildings()
    elif university=="University of Oregon":
        return OregonBuildings()
    elif university=="University of Pennsylvania":
        return UPennBuildings()
    elif university=="University of Pittsburgh":
        return PittsburghBuildings()
    elif university=="University of Redlands":
        return RedlandsBuildings()
    elif university=="University of Rochester": 
        return RochesterBuildings()
    elif university=="University of San Diego":
        return SanDiegoBuildings()
    elif university=="University of San Francisco":
        return SanFranciscoBuildings()
    elif university=="University of Texas at Austin":
        return TexasAustinBuildings()
    elif university=="University of Vermont":
        return VermontBuildings()
    elif university=="University of Virginia":
        return VirginiaBuildings()
    elif university=="University of Washington":
        return WashingtonBuildings()
    elif university=="University of West Los Angeles":
        return WestLosAngelesBuildings()
    elif university=="University of Wisconsin-Madison":
        return WisconsinMadisonBuildings()
    elif university=="University of the Pacific":
        return PacificBuildings()
    elif university=="University of the People":
        return PeopleBuildings()
    elif university=="University of the West":
        return WestBuildings()
    elif university=="Ursinus College":
        return UrsinusBuildings()
    elif university=="Vanderbilt University":
        return VanderbiltBuildings()
    elif university=="Vanguard University":
        return VanguardBUildings()
    elif university=="Vassar College":
        return VassarBuildings()
    elif university=="Virginia Commonwealth University":
        return VirginiaCommonwealthBuildings()
    elif university=="Virginia Tech":
        return VirginiaTechBuildings()
    elif university=="Wake Forest University":
        return WakeForestBuildings()
    elif university=="Washington University in St. Louis":
        return WashUBuildings()
    elif university=="Wesleyan University":
        return WesleyanBuildings()
    elif university=="Westcliff University":
        return WestcliffBuildings()
    elif university=="Western State College of Law":
        return WesternStateBuildings()
    elif university=="Western University of Health Sciences":
        return WesternHealthSciencesBuildings()
    elif university=="Westmont College":
        return WestmontBuildings()
    elif university=="Whittier College":
        return WhittierBuildings()
    elif university=="Woodbury University":
        return WoodburyBuildings()
    elif university=="Worcester Polytechnic Institute":
        return WorcesterBuildings()
    elif university=="Yale University":
        return YaleBuildings()
    elif university=="Zaytuna College":
        return ZaytunaBuildings()

    elif university=="University of California, Los Angeles":
        return UCLABuildings()
    elif university=="University of Southern California":
        return USCBuildings()
    elif university=="University of California, Irvine":
        return UCIBuildings()
    
def UCLABuildings():
    url="https://registrar.ucla.edu/faculty-staff/classrooms-and-scheduling/building-list"
    req=requests.get(url) #gets all html code from the url
    soup=BeautifulSoup(req.content,"html5lib") #.content is a property inside the class req
    tableData=soup.findAll("td") #finds all instances of td within the the table
    buildings=[]
    #every 2(or x) I take 1
    for i in range(1,len(tableData),2):
        #print(tableData[i].get_text())
        buildings.append(tableData[i].get_text())
    buildingList=[1, buildings, []]
    return(buildingList)
def USCBuildings():
    url="https://classes.usc.edu/term-20241/building-directory/"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("td")
    buildings=[]
    for i in range(0,len(tableData)):
        buildings.append(tableData[i].get_text())
    buildingList=[1, buildings, []]
    return(buildingList)
def UCIBuildings():
    url="https://special.lib.uci.edu/collections/anteater-chronicles/browse-buildings-by"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("td")
    buildings=[]
    for i in range(0,len(tableData),8):
        buildings.append(tableData[i].get_text())
    buildingList=[1, buildings, []]
    return (buildingList)
def CalPolyPomonaBuildings():
    url="https://www.cpp.edu/maps/text-map.php?id=28554&list=cat"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("li")
    buildings=[]
    for i in range (1,len(tableData)):
        buildings.append(tableData[i].get_text())
    buildingList=[1, buildings, []]
    return(buildingList)
def AlliantBuildings():
    buildingList=[8, ["Kauffman Library","Office of Accessibility"],["Fresno Campus","Irvine Campus","Los Angeles Campus","Phoenix Campus","Sacramento Campus","San Diego Campus","Emeryville Campus","Online Programs"]]
    return buildingList
def AmericanBuildings():
    buildings=["Anderson Hall","Asbury Building","Battelle-Tompkins","Beeghly Building","Bender Library","Butler Pavilion","Cassell Hall","Centennial Hall","Child Development Center","Clark Hall","Constitution Hall","Don Myers Technology and Innovation Building","Duber Hall","East Quad Building","Federal Hall","Friedheim Quadrangle","Gray Hall","Hall of Science","Hamilton Building",'Hughes Hall',"Hurst Hall","Jacobs Recreation Complex","Katzen Arts Center","Kay Spiritual Life Center","Kerwin Hall","Kogod School of Business","Kreeger Building","Leonard Hall","Letts Hall","Mary Graydon Center","McCabe Hall","McDowell Hall","McKinley Building","Media Production Center","Nebraska Hall",'Osborn Building',"President's Office Building", "Reeves Field","Rockwood Building","Roper Hall","School of International Service","Sports Center","Sports Center Annex","Watkins Building","Woods-Brown Ampitheather"]
    buildingList=[1,buildings,[]]
    return buildingList
def AmericanHeritageBuildings():
    buildingList=[1, ["Main Building"],[]]
    return buildingList
def AmericanJewishBuildings():
    buildingList=[1, [],[]]
    return buildingList
def AndrewsBuildings():
    url="https://www.andrews.edu/services/safety/parking/map.html"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("td")
    buildings=[]
    for i in range(1,len(tableData),4):
        buildings.append(tableData[i].get_text())
    for i in range(len(buildings)): #don't need -1 after len
        buildings[i]=buildings[i].replace("\n\t\t\t\t","")
        buildings[i]=buildings[i].replace("\xa0","")
    buildingList=[1, buildings, []]
    #index looping > for i in list
    #print(list(range(len(buildingList))))
    return(buildingList)
def ArtCenterBuildings():
    url="https://www.artcenter.edu/about/campus/overview.html"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("h3")
    buildings=[]
    for i in range(1,len(tableData)-2):
        buildings.append(tableData[i].get_text())
    buildingList=[1, buildings, []]
    return (buildingList)
def BardBuildings():
    url="https://www.bard.edu/catalogue/index.php?aid=1208507&sid=671464"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("strong")
    buildings=[]
    for i in range(30,len(tableData)):
        buildings.append(tableData[i].get_text())
    for i in range(len(buildings)):
        buildings[i]=buildings[i].replace(":\xa0","")
        buildings[i]=buildings[i].replace(":","")
    buildingList=[1, buildings, []]
    return (buildingList)
def BarnardBuildings():
    url="https://barnard.edu/eventsmgmt/spaces"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("h2")
    buildings=[]
    for i in range(4,len(tableData)-3):
        buildings.append(tableData[i].get_text())
    buildingList=[1, buildings, []]
    return (buildingList)
def BerkleeMusicBuildings():
    buildings=["1090 Boylston Street","1108 Boylston Street","1120 Boylston Street","1126 Boylston Street","1140 Boylston Street","130 Massachusetts Avenue","132 Ipswich Street","135 Massachusets Avenue","136 Massachusets Avenue","161 Massachusets Avenue","167 Massachusets Avenue","169 Massachusets Avenue","171 Massachusets Avenue","18 Belvidere Street (Saint Cecilia Parish)","181 Massachusets Avenue","22 Fenway","24 Fenway","25 Fordham Road","26 Fenway","264 Commonwealth Avenue","270 Commonwealth Avenut","31 Hemenway Street","32 Fenway","54 Fenway","7 Haviland Street","8 Fenway","855 Boylston Street","899 Boylston Street","921 Boylston Street","939 Boylston Street","98 Hemenway Street"]
    buildingList=[1,buildings,[]]
    return buildingList
def BiolaBuildings():
    url="https://www.biola.edu/campus-map"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("a")
    buildings=[]
    for i in range(6,len(tableData)-29):
        buildings.append(tableData[i].get_text())
    buildingList=[1, buildings, []]
    return (buildingList)
def BostonCollegeBuildings():
    url="https://www.bc.edu/bc-web/about/maps-and-directions/chestnuthill-campus-map.html"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("td")
    buildings=[]
    for i in range(0,len(tableData),2):
        buildings.append(tableData[i].get_text())
    buildingList=[1, buildings, []]
    return (buildingList)
def BostonUniBuildings():
    url="https://www.bu.edu/summer/summer-sessions/life-at-bu/campus-resources/building-codes/"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("td")
    buildings=[]
    for i in range(1,len(tableData),3):
        buildings.append(tableData[i].get_text())
    buildingList=[1, buildings, []]
    return (buildingList)
def BowdoinBuildings():
    url="https://www.bowdoin.edu/about/campus-location/facilities/campus-and-buildings.html"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("strong")
    buildings=[]
    for i in range(0,len(tableData)):
        buildings.append(tableData[i].get_text())
    buildings.remove(buildings[len(tableData)-1])
    buildings.remove(buildings[len(tableData)-2])
    buildings.remove(buildings[len(tableData)-4])
    buildingList=[1, buildings, []]
    return (buildingList)
def BrandeisBuildings():
    buildings=["60 Turner Street","567 South Street Apartments","Bernstein-Marcus Administration Center","Coffman Residence Hall","Deroy Residence Hall","Epstein Building","Faculty Center","Fellows Garden","Goldman-Schwartz Fine Arts","Gryzmish Center","Hassenfield Conference Center","International Business School","Irving Presidential Enclave","Lemberg Academic Center","Lember Children's Center","Lewis Residence Hall","Lodge at Brandeis","Main Entrance","Information Booth","May Residence Hall","Pollakc Fine Arts","Teaching Center","Rabb School","Renfield Residence Hall","Ridgewood Residence Hall A", "Ridgewood Residence Hall B", "Ridgewood Residence Hall C","Rose Art Museum","Rosenthal Residence Hall East","Rosenthal Residence Hall North","Rosenthal Residence Hall South","Sachar International Center","Carl and Ruth Shapiro Admissions Center","Carl adn Ruth Shapiro Campus Center","Shapiro Residence Hall","Sherman Hall","Slosberg Music Center","Spingold Theater Center","Usen Residence Hall","Village Residence Hall","Ziv Quad Hall A", "Ziv Quad Hall B","Ziv Quad D","Ziv Quad Mazer Hall","Abelson-Bass-Yalem Bassine Science Building","Berlin Chapel","Bethelem Chapel","Brown Social Science Center","Cable Residence Hall","Chapels Field","Edison-Lecks Science Building","Farber Library","Feldberg Communications Center","Foster Bio-Medical Research Center","Gerstenzang Science Library","Goldfarb Library","Golding Health Center","Golding Judaic Center","Goldsmith Building","Gordon Residence Hall","Harlan Chapel","Hassenfeld-Krivoff Residence Hall","Heller-Brown Building","Heller School for Social Policy and Management","Intercultural Center, Swig Hall","Kosow-Wolfson-Rosensweig","Kutz Hall","Landsman Research Facility","Lemberg Hall","Lown School of Near Eastern and Judaic Studies","Mailman House","Jack, Joseph and Morton Mandel Center for Studies in Jewish Education","Mandel Center for the Humanities","Olin-Sang American Civilization Center","Pearlman Hall","Rabb Graduate Center","Reitman Residence Hall","Rosenstiel Basic Medical Sciences Research Center","Rubenstein-Pomerantz Residence Hall","Scheffres Residence Hall","Schneider Building","Schwartz Hall","Abraham Shapiro Academic Complex","Carl J. Shapiro Science Center","Shapiro Brothers Residence Hall","Shiffman Humanities Center","Skyline Residence Hall","Stoneman Infimary and Public Safety","Usdan Student Center","Usen Castle","Volen National Center for Complex Systems"]
    buildingList=[1,buildings,[]]
    return buildingList
def BrownBuildings():
    url="https://en.wikipedia.org/wiki/List_of_Brown_University_buildings"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("td")
    buildings=[]
    length=len(tableData)-520
    for i in range(0,length,7):
        #tableData[i]=tableData[i].strip()
        buildings.append(tableData[i].get_text())
    buildingList=[1, buildings, []]
    return (buildingList)
def CIISBuildings():
    buildingList=[1, "CIIS Main Buildings", []]
    return (buildingList)
def CalTechBuildings():
    url="https://en.wikipedia.org/wiki/Campus_of_the_California_Institute_of_Technology"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("td")
    buildings=[]
    for i in range(1,len(tableData),5):
        buildings.append(tableData[i].get_text())
    for i in range(len(buildings)): #don't need -1 after len
        buildings[i]=buildings[i].replace("\n","")
    buildingList=[1,buildings,[]]
    return (buildingList)
def InstituteOfTheArtsBuildings():
    buildingList=[1,["Ahmanson Residence Hall", "Broad and Annex Studios", "Butler Buildings", "Chouinard Residence Hall", "Generator Building", "John Baldessari Studios Building & Crit Space", "Main Building","Main Entrance", "Outdoor Dance Theater","REDCAT","School of Art","School of Critical Studies","School of Film/Video","School of Theater","The Herb Alpert School of Music","The Sharon Disney Lund School of Dance","Wild Beast"],[]]
    return (buildingList)
def MiramarBuildings():
    buildingList=[3,[],["San Diego campus", "La Puente campus", "San Jose campus"]]
    return (buildingList)
def SouthBayBuildings():
    buildingList=[5,[],["North Campus", "South Campus", "Campus Saint-Jean", "Augustana Campus", "Enterprise Square"]]
    return (buildingList)
def ChannelIslandsBuildings():
    url="https://www.csuci.edu/fs/facility/custodial/buildings.htm"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("p")
    buildings=[]
    for i in range(0,len(tableData)):
        buildings.append(tableData[i].get_text())
    buildings.remove(buildings[-1])
    buildings.remove(buildings[-2])
    buildings.remove(buildings[-3])

    for i in range(len(buildings)): #don't need -1 after len
        buildings[i]=buildings[i].replace("\n\t\t\t","")
        buildings[i]=buildings[i].replace("\n\t\t","")
    buildingList=[1,buildings,[]]
    return (buildingList)
def SanMarcosBuildings():
    buildingList=[1,["Administrative Building", "Center for Children & Families", "Epstein Family Veterans Center", "Kellog Library", "M. Gordon Clarke Fieldhouse", "McMahan House", "Public Safety Building", "Sports Center", "Student Health & Counseling Services Building", "University Student Union", "Academic Hall", "Arts Building", "Extended Learning Building", "Markstein Hall", "Science Hall 1", "Science Hall 2", "Social & Behavior Sciences Building", "University Commons", "University Hall", "Viasat Engineering Pavilion", "North Commons", "The QUAD", "University Village Apartments"], []]
    return buildingList
def BakersfieldBuildings():
    url="https://cms.concept3d.com/map/accessible.php?id=1963&cId=56871"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("a")
    buildings=[]
    for i in range(0,len(tableData)):
        buildings.append(tableData[i].get_text())
    buildings.remove(buildings[0])
    buildings.remove(buildings[1])
    buildingList=[1,buildings,[]]
    return (buildingList)
def ChicoBuildings():
    url="https://www.csuchico.edu/traditions/campus/buildings.shtml"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("h2")
    buildings=[]
    for i in range(0,len(tableData)):
        buildings.append(tableData[i].get_text())
    buildingList=[1,buildings,[]]
    return (buildingList)
def EastBayBuildings():
   #buildings are in pdf format so manuel input
    buildings=["Art & Education", "Accessibility Services", "Applied Sciences Center", "Associated Students Inc.","Pioneer Bookstore", "C.E. Smith Museum of Anthropology","CORE", "Corporation Yard/Receiving","Dining Commons","Diversity and Inclusion Student Center","Field House and Offices","Facilities Maintenance","Food Stand","Stduent Health Center","University Library", "Music Building","Meiklejohn Hall","Pioneer Amphitheatre","Physical Education & Gym", "Parking Services","Pioneer Heights Student Housing","Robinson Hall","Recreation and Wellness Center","Student Services & Adminstration","Science Building - North","Science Building - South","Student and Faculty Support", "University Theatre","University Union", "Valley Business and Technology Center","Welcome Center for Future Students","Welcome Center parking"],["Academic Services","Contra Costa Hall","Facilities Operation", "Library","Campus Union"]
    buildingList=[3,buildings,["Hayward","Concord","Oakland"]]
    return (buildingList)
def FresnoBuildings():
    buildings=["Aquatics Center","Physical Therapy & Intercollegiate Athletics","North Gym Annex","North Gym","Grosse Industrial Technology","Engineering West","Quad","Social Science","McKee Fisk","South Gym","Professional Human Services","Peace Garden","Engineering East","McLane Hall","University Student Union","University Center","Vincent E. Petrucci Viticulture Building","Donald E. Gumz Enology Building","Agricultural Operations","FM Corp Yard","Agricultural Mechanics","Agricultureal Sciences","Frank W. Thomas Building","Speech Arts","Kremen Education/Human Development","Student Health and Counseling Center","Birch Hall","Sycamore Hall","Residence Halls Atrium","Aspen/Ponderosa Hall","Lynda & Stewart Resnick Student Union","Kennel Bookstore","Baker Hall","Graves Hall","Homan Hall","Sequoia/Cedar Hall","Lab School Annex","Lab School","Joyal Administration","Conley Art","University High School","Speech Arts","University Business Center","Allergy Free Garden","Smittcamp Alumni House","Leon S. Peters Business","Satellite Student Union","Animal Science Pavilion","Print Shop & Mailroom","Jordan Agricultural Research Center","Post Harvest Lab","Campus Pointe","Save Mart Center","Ornamental Horticulture Unit"]
    buildingList=[1,buildings,[]]
    return (buildingList)
def FullertonBuildings():
    buildings=["Anderson Field","Arts Drive Visitor Information center","Associated Road Visitor Information center","Auxiliary Services Corporation","Becker Amphitheater","Bookstore/Titan Shops","Brynes Circle (West of Anderson Field)","Children's Center","Clayes Performing Arts Center","College Park","Commons","Computer Science","Corporation Yard","Dan Black Hall","Eastside (Folino Drive) Visitor Information center","Eastside Parking Structore","Eastside Parking Structure 2 (Under Construction)","Education Classroom","Engineering","Fullerton Arboretum","Gastronome","Golf Practice Facility","Golleher Alumni House","Goodwin Field","Gordon Hall","Humanities-Social Sciences","Jewell Plummer Cobb Residence Halls","Kinesiology & Health Science","Langsdorf Hall","McCarthy Hall","Meng Concert Hall (Inside CPAC)","Military Science Building","Modular Complex","Nutwood Parking Structure","Parking and Transportation Office","Pollak Library","Resident Hall Lot (Student Housing)","Ruby Gerontology Center","South Campus Drive Lot","Steven G. Mihaylo Hall","Student Health and Counseling Center","Student Recreation","Student Wellness","Titan Gymanasium","Titan Hall","Titan House","Titan Stadium","Titan Student Union","Titan Track and Field","University Police","Visual Arts"]
    buildingList=[1,buildings,[]]
    return (buildingList)
def CalStateLABuildings():
    url="https://www.calstatela.edu/map"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("span")
    buildings=[]
    for i in range(7,len(tableData),5):
        buildings.append(tableData[i].get_text())
    for i in range(len(buildings)): #don't need -1 after len
        buildings[i]=buildings[i].replace("\n","")
        buildings[i]=buildings[i].replace("\n    \n    \n  ","")
        buildings[i]=buildings[i].replace("\n  \n    \n    \n  \n  ","")
        buildings[i]=buildings[i].replace('Emergency Phone',"")
        buildings[i]=buildings[i].replace('          ',"")
        buildings[i]=buildings[i].replace("  ","")

    for i in range (len(buildings)):
        if i=='Emergency Phone':
            buildings.remove(buildings[i])
    buildings1=[]
    for i in range(len(buildings)):
        if buildings[i]!="":
            buildings1.append(buildings[i])

    buildingList=[1,buildings1,[]]
    return (buildingList)
def MontereyBayBuildings():
    buildings=["Administration Buildng","Alumni & Visitors Center","Beach Hall","Black Box Cabaret","Business Information and Technology","Central Plant","Chapman Science Academic Center","College of Arts, Humanities, and Social Sciences","Cinematic Arts & Technology","Coast Hall","Del Mar","Dining Commons","Dunes Hall","Facilities Management","Forest Hall","Gavilan Hall","Green Hall","Grove Hall","Harbor Hall","Health & Wellness Services","Heron Hall","IT Services","Mail Room / Shipping & Receiving","Meeting House","Music Hall","Oaks Hall","Oaks Hall Annex","Oaks Hall Storage","Ocean Hall","Otter Express","Otter Student Union","Pacific Hall","Playa","Reading Center","Sand Hall","Science Instructional Lab Annex","Science Research Lab Annex","Student Center","Student Services","Surf Hall","Tanimura & Antle Family Memorial Library","Telecommunications","Tide Hall","University Center","University Storage","Valley Hall","Visual & Public Art - A","Visual & Public Art - B","Visual & Public Art - C","Visual & Public Art - D", "Watershed Institute","Wave Hall","World Theater","Asilomar Hall","Avocet Hall","Cypress Hall","Manzanita Hall","Promontory - West","Promontory - Center","Promontory - East","Pinnacles Suites","Sanderling Hall","Strawberry Apartments","Tortuga Hall","Vineyard Suites","Willet Hall","Yarrow Hall","Aquatic Center","Field House","Field Office","Otter Sports Center"]
    buildingList=[1,buildings,[]]
    return (buildingList)
def NorthridgeBuildings():
    url="https://www.csun.edu/licensing/university-buildings"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("h2")
    buildings=["The Soraya","Extended University Commons","Chancellor's Office"]
    for i in range(0,len(tableData)):
        buildings.append(tableData[i].get_text())
        buildings[i]=buildings[i].replace("\n"," ")
    buildingList=[1,buildings,[]]
    return (buildingList)
def SacramentoBuildings():
    buildings=["Sutter Hall","Sierra Hall","Dining Commons","Draper Hall","Jenkins Hall","Desmond Hall","American River Courtyard","Riverview Hall","Athletic Center","Facilities Management","University Print & Mall","Yosemite Hall","Sacramento Hall","Shasta Hall","River Front Center","Main Quad","Lassen Hall","Round House","Del Norte Hall","Sequoia Hall","Greenhouses","Douglass Hall","Mendocino Hall","Challenge Center","Solano Hall","Kadema Hall","Central Plant","Mariposa Hall","Calaveras hall","Alpine Hall","Placer Hall","Humboldt Hall","Non-Destructive Lab","Santa Clara Hall","Riverside Hall","Brighton Hall","Eureka Hall","Capistrano Hall","Facilities Corp Yard","Studio Theatre","Outpost","Library Quad","Library","Tschannen Science Complex","Planetarium","Hornet Bookstore","Children's Center","Tahoe Hall","South Green","Academic Information Resource Center","Amador Hall","University Union","Police Department","Art Sculpture Lab","Hornet Stadium","The WELL","Benicia Hall","Harper Alumni Center","BAC Yard","Capital Public Radio","Napa Hall","Modoc Hall","Hornet Commons"]
    buildingList=[1,buildings,[]]
    return (buildingList)
def SanBernardinoBuildings():
    buildings=["Plant/Central Warehouse","Facilities Plannting & Management","Auto Fleet Services","Environmental Health & Safety","Administrative Services","University Police","HVAC Central Plant","Chemical Sciences","Biological Sciences","TEMP. Classroms","TEMP Office","Physical Sciences","Social & Behavioral Sciences","Faculty Office Building","Administration","University center for Developmental Disabilities","Robert & Frances Fullerton Museum of Art","Visual Arts Center","Children's Center","Sierra Hall","Chaparral Hall","John M. Pfau Library","Ronald E. Barnes Theatre","Performing Arts","Building 23","Student Union South","University Hall","Information Center","Student Union East","Student Union North","Student Health Center","Jack J. Brown Hall","Cajon Hall","Coyote Village","Coyote Commons","Running Springs","Arrowhead Village Housing","Serrano Village","University Village","Center for Global Innovation","College of Education","Health & PE Complex","Coussoulis Arena","Physical Education","Temp. Kinesiology Annex","Student Recreation & Wellness Center"]
    buildingList=[1,buildings,[]]
    return (buildingList)
def StanislausBuildings():
    url="https://www.csustan.edu/campus-maps"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("td")
    buildings=[]
    for i in range(2,len(tableData),3):
        buildings.append(tableData[i].get_text())
    for i in range(len(buildings)):
        buildings[i]=buildings[i].replace(' ("A" prefix are in Acacia Building)','')
    buildingList=[1,buildings,[]]
    return (buildingList)
def CambridgeBuildings():
    buildings=[]
    buildingList=[5,buildings,["Cambridge College - Boston","Cambridge College - Lawrence","Cambridge College - Puerto Rico", "Cambridge College - Southern California","Cambridge College - Springfield"]]
    return buildingList
def CMUBuildings():
    buildings=["Alumni House","ANSYS Hall","Baker Hall (DC)","Bakery Square","Bramer House","Cohon University Center","College of University Center","Cyert Hall","Doherty Hall","Facilities Management Services Building","FMS Roads & Grounds","Gates Center for Computer Science (SCS)","Hall of the Arts","Hamburg Hall (HC)","Hamerschlag Hall","Hillman Center for Future Generation Technologies","Hunt Library","Integrated Innovation Institute Margaret Morrison","Mehrabian Collaborative Innovation Center","Mellon Institute (MCS)","Mill 19","National Robotics Engineering Center","Newell-Simon Hall","Osher Lifelong Learning Institute","Pittsburg Technology Center","Porter Hall","Posner Center","PPG 6","Purnell Center for the Arts","Rand Building","Roberts Engineering Hall","Scaife Hall (E)","Smith Hall","Scot Hall","Skibo Gymnasium", "Software Engineering Institute","TCS Hall","Tepper Building (TSB)","Warner Hall","Wean Hall","Whitfield Hall","WQED Building","Coulter Welcome Center","Office of Undergraduate Admission","Art Park","Center for Student Diversity & Inclusion","Dining Services","Disability Resources","The Fence","Fifth Avenue Neighborhood Commons","University Health Services","Unviersity Store","Human Resources","Housing Services","Miller ICA","Office of International Education","Walking to the Sky","Paush Bridge","Peace Garden","Boss House","Clyde House","Donner House","Fairfax Apartments","Fifth and Clyde House","Fifth Neville Apartments","Forbes Beller Apartments","Greek Quad","Hammerschlag House","Henderson House","Highlands Apartments","Margaret Morrison Apartments Greek Housing","McGill House","Morewodo E-Tower","Morewood Gardens","Mudge House","Nevile Apartments","Residence on Fifth","Resnik House","Roselawn Terrace","Scobell House","Shady Oak Apartments","Shirley Apartments","Spirit House","Stever House","Welch House","West Wing","Woodlawn Apartments"]
    buildingList=[1,buildings,[]]
    return buildingList
def CaseWesternBuildings():
    url="https://case.edu/its/archives/Buildings/bldgsazlist.htm"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("a")
    buildings=[]
    for i in range(11,len(tableData)):
        buildings.append(tableData[i].get_text())
    for i in range(len(buildings)):
        buildings[i]=buildings[i].replace("\n      ","")
    buildings.remove(buildings[168])
    buildings.remove(buildings[167])
    buildingList=[1,buildings,[]]
    return (buildingList)
def ChapmanBuildings():
    buildings=["Anderson Athletics Complex","Anderson Tennis Center","Argyros Forum","Becket Building","Beckman hall","Bertea Hall","Bhathal Student Services Center","Career and Professional Development","Center for Creative and Cultural Industries","Chapman Studios West","Community Relations","Cortese Elder Law Center","Crean Hall","Cypress Street Schoolhouse","DeMille Hall","Digital Media Arts Center","Doti Hall","Earl Babbie Research Center","Elliott Alumni House","Emergency Management - Fire and Life Safety","Entertainment Technology Center","Event Operations","Fish Interfatih Center","Hasinger Science Center","Hilbert Museum","Hutton Sports Center","Institute for Earth, Computing, Human and Observing","Institute for Interdisciplinary Brain and Behavioral Sciences","Institutional Research and Religion, Economics and Society","Irivine Lecture Hall","Keck Center for Science and Engineering","Kennedy Hall","Knott Studios","Leatherby Center for Entrepreneurship and Business Ethnics","Leatherby Libraries","Legal Affairs","Memorial Hall","Military and Veterans Law Institute","Moulton Hall","Musco Center for the Arts","Office of Institutional Compliance and Internal Audit","Oliphant Hall","President Emeritus Office","Reeves Hall","Risk Management and Environmental Health and Safety","Roosevelt Hall","Smith Hall","Student Health Center","Student Psychological Counseling Services","The Packing House at Chapman","Thompson Policy Institute","Veterans Resource Center","Van Neumann Hall","Waltmar Foundation","Waltmar Theater","Wilkinson Hall"]
    buildingList=[1,buildings,[]]
    return buildingList
def CharlesDrewBuildings():
    buildings=["Avis and Mark Ridley Thomas Wellness Center","The Student Center","Keck Building","Keck Auditorium","Building N","W. Montague Cobb Medical Education Building","Life Sciences Research Nursing Education Building"]
    buildingList=[1,buildings,[]]
    return buildingList
def ClaremontBuildings():
    buildings=["Office of Admissions and Visitor Center","Arts & Humanities Faculty","Academic Computing Building (ACB)","Albrecht Auditorium","Art and Humanities Faculty","Behavioral & Organizational Sciences","Blaisdell House (Arts & Humanities faculty)","California Botanic Garden (Botany Department)","Center for Business & Management of the Arts/ Museum Leadership Institute","Center for Neuroecomoics Studies","Center for the Arts","Claremont Evaluation Center","Harper Hall","John Stauffer Hall of Learning","Mathematical Sciences Faculty Offices","Mathematical Sciences/ Social & Computational Sciences Lab","McManus Hall of Graduate Studies","Quality of Life Research Center","Ron W. Burkle Family Building (Drucker School of Management)","School of Community & Global Health","Yuhaaviatam Center for Health Studies","Drucker Institute","Facilities Office","George and Margaret Jagels Buildings","Harper Hall East (Student Services)","Office of Information Technology","CGU Housing","Jenkins Courtyard","William S. Rosecrans Tower and Court","Honnold/Mudd Library","Student Life, Diversity & Leadership House","Robert E. Tranquada Student Services Center","Veterans Lounge","Chicano Latino Student Affairs (CLSA)","Office of Black Student Affrais (OBSA)","Transdisciplinary Studies and Preparing Future Faculty"]
    buildingList=[1,buildings,[]]
    return (buildingList)
def ClaremontMcKennaBuildings():
    buildings=["Adams Hall / Davidson Lecture Hall","Bauer Center North","Bauer Center South","Bauer Forum","Bernard Field Station","Freeberg Forum","Heggblade Center","Honnold/Mudd Library","Human Resources","Kravis Center","M.M.C. Athenaeum","McKenna Auditorium","Pickford Auditorium","Robert Day School","Roberts Hall North","Roberts Hall South","Seaman Hall","The Massoud","W.M. Keck Science Center","W.M. Keck Science Physics Lab","Ath Offices","Center Court","CMC Public Safety","Dean of Students","Mills Avenue Office","Office of Admission","Office of Financial Aid","Soll Center for Student Opportunity","Story House","The Cottages","Tranquada Student Services Center"]
    buildingList=[1,buildings,[]]
    return buildingList
def ColbyBuildings():
    url="https://en.wikipedia.org/wiki/List_of_Colby_College_buildings"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("td")
    buildings=[]
    for i in range(2,len(tableData),5):
        buildings.append(tableData[i].get_text())
    buildings.remove(buildings[-1])
    for i in range(len(buildings)):
        buildings[i]=buildings[i].replace("\n","")
        buildings[i]=buildings[i].replace("\n\n","")
    buildings.remove(buildings[33])
    buildings.remove(buildings[33])
    buildings.remove(buildings[33])
    buildings.insert(33,"Marriner Hall")
    buildings.insert(34,"Sturtevant Hall")
    buildings.insert(35,"Taylor Hall")
    buildings.insert(36,"Williams Hall")
    buildingList=[1,buildings,[]]
    return buildingList
def ColgateBuildings():
    buildings=["Alumni Hall","Benton Center","Dana Arts Center","Hascall Hall","Ho Science Center","Lathrop Hall","Little Hall","McGregory Hall","Office of Undergraduate Studies (OUS)","Olin Hall","Paul J. Schupf Studio Arts Center","Persson Hall","Wynn Hall","Lawrence Hall","Andrews Hall","Bryan Complex","Burke Hall","Curtis Hall","Drake Hall","East Hall","Gate House","Jane Pinchin Hall","Newell Apartments","Parker Apartments","Preston Hill Apartments", "Stillman Hall","Townhouse Apartments","West Hall","University Court Apartments","Campus Safety","Chapel House","Community Memorial Hospital","Counseling Center","Haven - Sexual Violence Support and Resources","Student Health Services","Shaw Wellness Institute","Brehmer Theater","Clifford Gallery","Colgate Memorial Chapel","Hamilton Movie Theater","Linsley Geology Museum","Longyear Museum of Anthropology","Palace Theater","Picker Art Gallery","Ryan Studio"]
    buildingList=[1,buildings,[]]
    return buildingList
def HolyCrossBuildings():
    buildings=["O'Kane Hall", "Fenwick Hall","Smith Hall","Dinand Library","Integrated Science Complex","Beaven Hall","Smith Laboratories","O'Neil Hall","Swords Hall","Haberlin Hall","Millard Art Center","Stein Hall","Brooks Hall","Clark Hall","Hanselman Hall","Lehy Hall","Healy Hall","Loyola Hall","Williams Hall","Alumni Hall","Carlin Hall","Wheeler Hall","Figge Hall","Hogan Campus Center","Ciampi Hall","St. Joseph Memorial Chapel","Greenhouse","Campion House","Kimball Hall","Memorial Palza","Hogan Courtyard"]
    buildingList=[1,buildings,[]]
    return buildingList
def ColumbiaBuildings():
    url="https://www.registrar.columbia.edu/content/building-codes"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("td")
    buildings=[]
    for i in range(1,len(tableData),2):
        buildings.append(tableData[i].get_text())
    buildings.remove(buildings[-1])
    buildingList=[1, buildings, []]
    return (buildingList)
def ConcordiaBuildings():
    buildings=["Administration","Good Shepherd Chapel","Founders Hall","Center Student Leadership Developemt (CSLD)","Hallerberg Center","Performing Arts Annex","CU Arena","CU Center","Library, Arts & Theater","Chi Alpha","Chi Beta","Maintenance","Gate House 1","RHO","Grimm Student Union","Gate House 2","Grimm Hall North","Grimm Hall South","Borland-Manske Center: Music","Borland-Manske Center: Christ College", "Chi Dela Apartments","Chi Gamma Apartments","Chi Zeta Apartments","Chi Epilson Apartments","Chi Kappa Apartments","Chi Theta Apartments","Chi Omicron Apartments","Chi Lambda Apartments","Chi Rho Suites","Chi Sigma Suites"]
    buildingList=[1,buildings,[]]
    return buildingList
def CornellBuildings():
    url="https://en.wikipedia.org/wiki/List_of_Cornell_University_buildings"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("td")
    buildings=[]
    for i in range(0,1190,7):
        buildings.append(tableData[i].get_text())
    for i in range(1190,len(tableData),8):
        buildings.append(tableData[i].get_text())

    for i in range(len(buildings)):
        buildings[i]=buildings[i].replace("\n","")
    buildings.remove(buildings[-1])
    buildingList=[1, buildings, []]
    return buildingList
def DartmouthBuildings():
    url="https://en.wikipedia.org/wiki/Campus_of_Dartmouth_College"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("td")
    buildings=[]
    for i in range(0,151,5):
        buildings.append(tableData[i].get_text())
    for i in range(155,444,6):
        buildings.append(tableData[i].get_text())
    for i in range(449,len(tableData),5):
        buildings.append(tableData[i].get_text())
    for i in range(len(buildings)):
        buildings[i]=buildings[i].replace("\n"," ")
    buildings.remove(buildings[-1])
    buildings.remove(buildings[-1])
    buildings.remove(buildings[-1])
    buildings.remove(buildings[-1])
    buildings.append("Class of 1953 Commons")
    buildings.append("Class of 1978 Life Sciences Center")
    buildings.append("Visual Arts Center")
    buildingList=[1, buildings, []]
    return buildingList
def DominicanBuildings():
    buildings=["Academic Affairs","Academic Support Services","Admissions","Advancement","Alumni Relations","Art Gallery","School of Liberal Arts and Education","ASDU (Associated Students of Dominican University of California)","Athletics Offices","The Epicurean Group","Bookstore","Barowsky School of Business","Guzman Hall","Bertrand Hall","Magnolia House","Edgehill Mansion","Alemany Library","Angelico Hall","Fanjeaux Hall","Conlan Center","Caleruega Hall","Business Services","Campus Ministry","Career Services","Chapel","Chilly's Café","Computer Labs","Counseling Services","Creekside Room","ELS Language Centers","Financial Aid","Guzman Lecture Hall","Gymnasium","School of Health and Natural Sciences","Pennafort Hall","Meadowlands Hall","Health Center","Housing Office (Residential Life)","Human Resources","Information Technology","International Studies","Mail Services","Marketing","Nursing Labs","Osher Lifelong Learning Institute","San Marco Art Studios","San Marco Art Gallery","Shield Room","Suzuki School of Music","Teaching and Learning Center","Weight Room/Multipurpose Room"]
    buildingList=[1,buildings,[]]
    return buildingList
def DrexelBuildings():
    url="https://drexel.edu/about/locations/university-city-campus/ucity-campus-map"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("td")
    buildings=[]
    for i in range(1,len(tableData),2):
        buildings.append(tableData[i].get_text())
    for i in range(len(buildings)):
        buildings[i]=buildings[i].replace("\n            "," ")
        buildings[i]=buildings[i].replace("\t","")
    buildingList=[1, buildings, []]
    return (buildingList)
def DukeBuildings():
    #West Campus buildings
    url="https://dukecard.duke.edu/west-campus-buildings/"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("button")
    buildings=[]
    for i in range(2,len(tableData)):
        buildings.append(tableData[i].get_text())
    #East Campus buildings
    url="https://library.duke.edu/rubenstein/uarchives/history/exhibits/building-names/east"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("a")
    for i in range(19,len(tableData)-41):
        buildings.append(tableData[i].get_text())
    #Central campus buildings
    url="https://dukecard.duke.edu/central-campus-buildings/"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("button")
    for i in range(2,len(tableData)):
        buildings.append(tableData[i].get_text())
    #Medical campus buildings
    url="https://dukecard.duke.edu/medical-campushospital-buildings/"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("button")
    for i in range(2,len(tableData)):
        buildings.append(tableData[i].get_text())
    buildingList=[4,buildings,["West Campus","East Campus","Central Campus","Medical Campus"]]
    return buildingList
def EckerdBuildings():
    buildings=["Alumni Grove","Armacost Library","Art Studio","Bininger Center for Performing Arts (BIN)","Bullard Tennis Courts","Cafeteria and Dining","Brown Hall","Center for Visual Arts","Clay Lab","Cobb Building","Continuing Education Center (CEC)","Doyle Sailing Center","Forrer Language Center (FO)","Fox Hall (Hough Center)","Fox Woods","Franklin Templeton Building (FT)","Galbraith Marine Science Laboratory (GMSL)","GO Pavilion","Edmunson Hall","Lindsey Hall","James Center for Moleculer and Life Sciences","Lewis House","McArthur Physical Education Center","Miller Auditorium","Alpha Complex","Beta Complex","Delta Complex","Epsilon Complex","Iota Complex","Kappa Complex","Nu Complex","Omega Complex","Sigma Complex","West Lodge","Zeta Complex", "Roberts Music Center (RO)","Seibert Humanities Building (SE)","Sheen Annex","Sheen Center","Slater's Woods","Student Lounge","Turley Athletic Complex","Upham Administration Building","waterfront Complex","Welcome Center","Wireman Chapel"]
    buildingList=[1,buildings,[]]
    return buildingList
def EmoryBuildings():
    url="https://communications.emory.edu/resources/style-guide/emory-specifics/campuses-buildings.html"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("li")
    buildings=[]
    for i in range(15,len(tableData)-18):
        buildings.append(tableData[i].get_text())
    buildingList=[4,buildings, ["Atlanta Campus","Briarcliff Property"," Clairmont Campus", "Oxford Campus"]]
    return buildingList
def FranklinMarshallBuildings():
    url="https://www.fandm.edu/housing/on-campus-residential-facilities.html"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("a")
    buildings=[]
    for i in range(104,len(tableData)-36):
        buildings.append(tableData[i].get_text())
    url="https://library.fandm.edu/c.php?g=933708&p=6730459"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("b")
    for i in range(0,len(tableData)):
        buildings.append(tableData[i].get_text())
    for i in range(len(buildings)):
        buildings[i]=buildings[i].replace("\xa0"," ")
    buildingList=[1,buildings, []]
    return buildingList
def FloridaStateBuildings():
    buildings=["Advocacy Center - College of Law","Alligator Point - President's Cottage","Alligator Pt.","Alpha Dela Pi Pavilion","Alumni Center Facility","Ame Building","Arlington Building","Art Teaching Labs","Askew Student Life Center","Ausley House - Village Green - College of Law","Azalea Hall","B.K. Roberts Hall - College of Law","Bat House - Civic Center","Bellamy Building","Bill's Bookstore","Biology Unit I","Biomedical Research Facility","Broward Hall","Bryan Hall","Cage Wash Facility","Caldwell House - Village Green - College of Law","Caps Dielectrics Labs","Caps High Bay Lab","Caps Medium Voltage Lab",'Carnaghi Arts Building',"Carothers Hall","Carraway Building","Cawthon Hall","Challenger Learning Center","Chemical Science Laboratories","Child Development Center","City Centre Building","Cob - Jim Moran Institute","Coburn Wellness Center","Collier Clinic - College of Medicine","Collins Research Building","COM - Autism Institute","COM - Daytona State College - McKinnon Hall","COM - Florida Medical Practice Plan","COM - Ft. Pierce Regional Medical Facility","COM - Pensacola Regional Medical Facility","COM - Sarasota Regional Campus","COM - Tallahassee Regional Campus","Creighton/Bayou Building","Criminology and Criminal Justice Building","Critchfield Hall","Damon House - Village Green - College of Law","DC Magnet Building","DeGraff Hall East","DeGraff Hall West","Deviney Hall","Diffenbaugh Building","Dirac Science Library","Dittmer Chemistry Lab","Dodd Hall","Dodd Lecture Hall","Dorman Hall","Dunlap Success Center","Duxbury Hall","Energy Resesarch Facility","Engineering Portable", "Engineering Lab Building","Eoas Building","ETV Transmitter Building 2","Facility for Arts Research","FAMU - FSU Engineering Building","FARM - Animal Pen","FARM - Lab Animal Resources", "FARM - Radiation Storage","FARM - Roofing Material Storage", "FARM - Storage Building","FARM - Theater Scene Storage", "FDLE Mail Facility","FHP Academy","FHP Dorm","Fine Arts Building","Fisher Lecture Hall","Florida Capitol Building","Frank Shaw Building - Innovation Park","FSU Foundation Building","FSU Primary Health - College of Medicine","FSUS Science/Intermediate Building","FSUS Steam Building","General Science Building","Gilchrist Hall","Grenne-Lewis House","Harpe-Johnson Building","Hecht House","Hobby-Harrison/Cawthon House - Village Green - College of Law","Hoffman Teaching Lab","Honors Scholars & Fellows","Housewright Music Building","Howser Batting Tunnel","Jennie Murphree Hall","Jim Moran Building","Johnson Building - Fuqua Resesarch Complex",'Johnston Building',"Kasha Laboratory","Keen Building","Kellogg Building","Kemper Lab","King Life Science Building","Kuersteiner Music Building","Lafayette Building 1339","Landis Hall","Law Research Center - College of Law","Leach Center","Legacy Hall (College of Business)","Liberty Square Building","Longmire Building","Love Building","Mabry Building","Magnolia Hall","Marine Lab","McCollum Hall","McIntosh Track & Field Building","Mendenhall Building","Miami-Dade Courthouse","Morcom Mechanical Building","Morgan Building - Fuqua Research Complex","New Student Union","NMR Building","Nursery","NW Residence Hall","Opera Scene Shop","Pearl Tyner Welcome Center","Pepper Building","President's House","Psychology Department Auditorium","Ragans Hall","Recycling Center","Research Building - College of Medicine","Research Complex - Commonwealth","Research's Entrepreneurial Building","Reynolds Hall","Richards Building","Rogers Hall","Rotunda - College of Law","Rovetta Building","Salley Hall","Sand Volleyball Building","Sandels Building","Seminole Landing","Shaw Building (Main Campus)","Shores Building","Sliger Building - Fuqua Research Complex","Stavros Center","Stiles-Smith Team Building","Stone Building","Strozier Library","Student Services Building","Supreme Court Building","Tallahassee Memorial Hospital","Tanner Hall","Technology Services Building","Thagard Building","The Clock Building","The Collegiate School","The Lab","Theatre Annex","Trasher Building - College of Medicine","Traditions Hall","Tucker Civic Center","Tully Gym",'Turlington Building','Turnbull Conference Center',"University center","Veterans Legacy center","Warren Building","Westcott Building","Westcott Welcome Center","Wildwood Halls","Williams Building","Winchester Building"]
    buildingList=[1,buildings, []]
    return buildingList
def GeorgeMasonBuildings():
    buildings=["Adams Hall","Alan and Sally Merten Hall","Amherst Hall","Angel Cabrera Global Center","Aquia Building","Art and Design Building","Blue Ridge Hall","Brunswick Hall","Carow Hall","Carroll Hall","Carty House","Center for the Arts","Child Development Center","Commonwealth Hall",'David King Hall',"Democracy Lane","Dickenson Hall","Dominion Hall","Donald and Nancy de Laski Performing Arts Building","East Building","Eisenhower Hall","Enterprise Hall","Essex Hall","Exploratory Hall","Fenwick Library","Finley Buildings","Grayson Hall","Hampton Roads Hall","Hanover Hall","Harris Theatre","Harrison Hall","Horizon Hall","Innovation Hall","Jackson Hall","James Buchanan Hall","Jefferson Hall","Johnson Center","Kelley II","Kennedy Hall","Krasnow Institute","Krug Hall","Lecture Hall","Liberty Square","Lincoln Hall","Long and Kimmy Nguyen Engineering Building","Madison Hall","Mason Enterprise center","Mathy House","Monroe Hall","Music/Theater Building","Northeast Module","Northeast Module II","Northern Neck", "Nottoway Annex","Peterson Hall","Peterson Population Health Center","Piedmont Hall","Planetary Hall","Potomac Heights","Research Hall","Rivanna Module","Roberts House","Rogers Hall","Roosevelt Hall","Sandbridge Hall","Skyline Fitness Center","Southside Dining Hall","Student Union Building I","Tallwood House","Taylor Hall","The Hub","Thompson Hall","Tidewater Hall",'Truman Hall','Washington Hall',"West Building","West PE Module","Whitetop Hall","Wilson Hall","Fuse at Mason Square","Van Metre Hall","Hazel Hall","Vernon Smith Hall","3300 Fairfax Drive","933 N Kenmore Street","Beacon Hall","Biomedical Resesarch Laboratory","BRL Annex","Katherine G. Johnson Hall","Colgan Hall","Discovery Hall","Forensics Farm","Hylton Performing Arts Center","Hylton Performing Arts Center - Education Wing","Innovation Park","Institute for Advanced Biomedical Research","Life Sciences Engineering Building","Physical Plant Compound"]
    buildingList=[3,buildings, ["Fairfax Campus","Mason Square Campus","Science & Technology Campus"]]
    return buildingList
def GeorgiaTechBuildings():
    url="https://avservices.gatech.edu/buildings/"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("h5")
    buildings=[]
    for i in range(0,len(tableData)):
        buildings.append(tableData[i].get_text().strip())
    buildingList=[1,buildings, []]
    return buildingList
def GeorgeWashingtonBuildings():
    url="https://explore.gwu.edu/buildings"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("h3")
    buildings=[]
    #buildings.append(tableData[15].get_text())
    for i in range(0,len(tableData)):
        buildings.append(tableData[i].get_text())
    for i in range(len(buildings)):
        buildings[i]=buildings[i].replace("\xa0"," ")
        buildings[i]=buildings[i].replace("Funger Hall (FNGR)2201 G Street NW • View building details","Funger Hall (FNGR)")
    buildingList=[1,buildings, []]
    return buildingList
def GeorgetownBuildings():
    url="https://en.wikipedia.org/wiki/List_of_Georgetown_University_buildings"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("th")
    buildings=[]
    for i in range(8,len(tableData)-19):
        buildings.append(tableData[i].get_text())
    for i in range(len(buildings)):
        buildings[i]=buildings[i].replace("\n","")
    buildingList=[1,buildings, []]
    return buildingList
def GraduateTheologicalBuildings():
    buildings=["Center for the Arts & Religion (CARe)","Center for Dharma Studies (CDS)","The Center for Islamic Studies (CIS)","The Richard S. Dinner Center for Jewish Studies (CJS)","The Center for Theology and the Natural Sciences (CTNS)"]
    buildingList=[1,buildings,[]]
    return buildingList
def GrinnellBuildings():
    buildings=["Conney M. Kimbo Black Cultural Center","Natatorium","Darby Gym/Fitness Center","Norris Hall","Clark Hall","Rawson Hall","Langan Hall","Smith Hall","Harris Center","Cowles Hall","Rosenfield Center","Noyce Science Center","Alumni Recitation Hall","Carnegie Hall","Herrick Chapel","Herrick Chapel","Steiner Hall","Goodnow Hall","Grinnell College Forum","Burling Library","Macy House","Harry Hopkins House","1127 Park","Nollen House","John Chyrstal Center","Bucksbaum Center for the Arts","Windsor House","Preschool Lab","Old Glove Factory","Grinnell House","Rathje Hall","Rose Hall","Kershaw Hall","Lazier Hall","Mears Cottage","Loose Hall","Read Hall",'Haines Hall',"James Hall","Cleveland Hall","Main Hall"]
    buildingList=[1,buildings,[]]
    return buildingList
def HamiltonBuildings():
    url="https://www.hamilton.edu/library/library_collections/archives/buildings.cfm?id=bldgDate"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("td")
    buildingsWithDemolishedBuildings=[]
    for i in range(7,len(tableData),5):
        buildingsWithDemolishedBuildings.append(tableData[i].get_text())
    for i in range(len(buildingsWithDemolishedBuildings)):
        buildingsWithDemolishedBuildings[i]=buildingsWithDemolishedBuildings[i].replace("\xa0","")
    buildings=[]
    for i in range(len(buildingsWithDemolishedBuildings)):
        if buildingsWithDemolishedBuildings[i].isnumeric():
            pass
        else:
            buildings.append(buildingsWithDemolishedBuildings[i])
    buildingList=[1,buildings, []]
    return buildingList
def HarvardBuildings():
    buildings=["1 Bow St.","2 Arrow St.","2 Divinity Ave.","34 Kirkland St.","5 Bryant St.","54 Dunster St.","61 Kirkland St.","9 Kirkland Place","Adams House - Randolph Hall","Adams House - Russell House","Adams House - Westmorly Court", "Agassiz House","Art Studios - University Squash Courts, 6-8 Linden St.","Barker Center","Bauer Life Sciences Building (Bauer Lab)","Biological Lab","Botanical Museum - University Museum","Boylston Hall","Cabot House - Bertram Hall","Cabot House - Whitman Hall","Carpenter Center","Center for European Studies - Adolphus Busch Hall","CGIS Knafel (North)","CGIS South","Conant Chemistry Lab","Converse Chemistry Lab","Cruft Lab","Currier House - Bingham Hall","Currier House - Gilbert Hall","Currier House - Tuchman Hall","Dana-Palmer House","Dunster House","Eliot House","Emerson Hall","Farkas Hall","Geological Museum - University Museum","Harvard Art Museums","Harvard Hall","Harvard Mseum of the Ancient Near East","Hilles","Hoffman Lab","Holden Chapel","Houghton Library","Jefferson Lab","Kirkland House - Bryan Hall","Lab For Integrated Science and Engineering (LISE)","Lamont Library","Lehman Hall, The Student Center at Harvard Griffin GSAS","Leverett House - McKinlock Hall","Littauer Center","Loeb Drama Center (ART)","Loeb House, 17 Quincy St.","Lowell Hall","Lowell House","Lyman Lab","Mallinckrodt Chemistry Lab","Mather House","Maxwell Dworkin","Memorial Hall","Museum of Comparative Zoology (MCZ)","Music Building","Northwest Building","Observatory Building A","Observatory Building D",'Observatory Perkin Lab','Peabody Museum',"Pforzhemier House - Moors Hall","Phillips Brooks House","Pierce Hall","Pusey Library","Quincy House - New Residence Hall","Quincy House - Stone Hall","Robinson Hall","Sackler Building 485 Broadway","Science Center","Sever Hall","Sherman Fairchild Biochemistry Lab",'Tozzer Anthropology Building',"University Herbaria","Vanserg Building","Warren House","Widener Library","Williams James Hall","Winthrop House - Standish Hall"]
    buildingList=[1,buildings, []]
    return buildingList
def HarveyMuddBuildings():
    buildings=["Beckman Hall","F.W. Olin Science Center","Galileo Hall","Hoch-Shanahan Dining Commons","Jacobs Science Center","Joseph B. Platt Campus Center","Kingston Hall","Norman F. Sprague Center","Parsons Engineering Building","R. Michael Shanahan Center for Teaching and Learning","Ronald and Maxine Linde Activities Center","Scott A. McGregor Computer Science Center","W.M. Keck Laboratories","Case Residence Hall","East Hall/Mildred E. Mudd Hall","Frederick and Susan Sontag Residence Hall","Garrett House","J.L. Atwood Residence Hall","North Hall","Ronald and Maxine Linde Residence Hall","South Hall/Marks Hall","Wayne '73 and Julie Drinkward Residence Hall","West Hall","Caryll Mudd and Norman F. Sprague Jr. Courtyard and Gallery","Drinkward Recital Hall","Hoch-Shanahan Dining Commons"]
    buildingList=[1,buildings,[]]
    return buildingList
def HaverfordBuildings():
    url="https://www.haverford.edu/campus-map"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("h5")
    buildings=[]
    for i in range(0,len(tableData)):
        buildings.append(tableData[i].get_text())
    buildingList=[1,buildings, []]
    return buildingList
def HolyNamesBuildings():
    buildings=["Michael and Maureen Hester Administration", " aul J. Cushing Library" , "Tobin Gymnasium, and McLean Chapel"]
    buildingList=[1,buildings,[]]
def HowardBuildings():
    buildings=["Academic Support Building A (Education)", "Academic Support Building B","Andrew Carnegie Hall","Andrew Rankin Memorial Chapel","Armour Blackburn University Center","Cancer Research Center","CB Powell Building (Communications)","Charles Drew Hall","Chauncey Cooper Hall (Pharmacy)", "Chemical Engineering Building","Chemistry Building","College Hall North","College Hall South","Early Learning Center","Effingham Apartments","Ernest Just Hall (Biology)","Founders Library - MSRC","Founders Library - UGL", "Frederick Douglass Memorial Hall","Annex II (Nursing & Allied Health Science)","Annex III (Graduate School)", "George Cook Hall","Harriett Tubman Quadrangle","Crandall Hall",'Fraizer Hall',"Wheatley Hall","Baldwin Hall","Truth Hall","Hospital Towers",'Howard Mackey Building (Architecture)',"Howard Manor Apartments","Howard Plaza Tower (West)","Howard Plaza Towers (East)","Howard University Bookstore","Howard University Hospital","Howard University Service Center","iLab",'Inabel Linsday Hall (Social Work)',"Interdisciplinary Resesarch Building","Ira Aldridge Theatre","John Burr Gymnasium Building","Laser Chemistry Building","Louis Cramton Auditorium","Louis Downing Hall (Engineering)","Louis Stokes Health Sciences Library","Lulu Childers Hall (Fine Arts)",'Mary Bethune Annex',"Mary Bethune Annex Dining Hall","Medical Arts Building (Student Health)","Mental Health Center","Middle School for Math & Science","Mordecai Johnson Admin. Building","Numa Adams Building (Medicine)","Oliver Howard Hall","Ralph Bunche Center","Russell Dixon Building (Dentistry)","School of Business","Seeley Mudd Building (Medicine)","Warehouse Building","WHUR-Radio","WHUT-TV","Wilbur Thirkield Hall (Physics)","William Greene Memorial Stadium","Wonder Plaza (ETS)"]
    buildingList=[1,buildings,[]]
    return buildingList
def HumphreysBuildings():
    buildings=[]
    buildingList=[3, buildings,["Stockton Campus","Modesto Campus","Drivon School of Law"]]
    return buildingList
def IllinoisTechBuildings():
    url="https://www.iit.edu/about/campus-information/mies-campus/mies-campus-buildings"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("td")
    buildings=[]
    for i in range(0,len(tableData),3):
        buildings.append(tableData[i].get_text())
    for i in range(len(buildings)):
        buildings[i]=buildings[i].replace("\n\t\t\t","")
        buildings[i]=buildings[i].replace("\xa0"," ")
    buildingList=[1,buildings, []]
    return buildingList
def IndianaBloomingtonBuildings():
    url="https://registrar.indiana.edu/information/building-codes.html"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("td")
    buildings=[]
    for i in range(1,len(tableData),2):
        buildings.append(tableData[i].get_text())
    buildingList=[1,buildings, []]
    return buildingList
def JohnsHopkinsUniversity():
    #url="https://www.jhu.edu/maps-directions/campus-map/"
    buildings=["Abel Wolman House Alumni Memorial Residences","AMR 1","AMR 2","AMR 3, Building A", "AMR 3, Building B",'Ames Hall',"Barnes & Noble Johns Hopkins Bookstore","Barton Hall","Biology East","The Blackstone Apartments","Bloomberg Center for Physics & Astronomy","Bradford Apartments","Brody Learning Commons","Bunting Meyerhoff Interfaith and Community Service Center","The Charles Apartments","Charles Commons","Chemistry Building",'Clark Hall',"Cordish Lacrosse Center","Croft Hall","Dell House","Dunning Hall","Education Building","Garland Hall","Gatehouse","Gilman Hall","Glass Pavilion","Greenhouse & Greenhouse South","Hackerman Hall","Hodson Hall","Homewood Apartments","Homewood Apartments Annex","Homewood Early Learning Center",'Homewood Field',"Homewood Museum","Hopkins Square","Jenkins Hall","Johns Hopkins Club","Krieger Hall","Lacross Hall of Fame","Latrobe Hall","Levering Hall","Levi Building","Macualay Hall","Malone Hall","Marland Hall","Mason Hall","Mattin Center","Maxine F. Singer Building / Carnegie Institution of Washington","McCoy Hall","Mergenthaler Hall","Merrick Barn","Milton S. Eisenhower Library",'Mudd Hall',"Newton H. White Jr. Athletic Center","Nichols House","Olin House","Power Plant","Ralph S. O'Connor Recreation Center","Remsen Hall","Rogers House",'ROTC Building',"San Martin Center",'Schelle Pavilion',"Shaffer Hall","Shriver Hall","Smokler Center for Jewish Life (Hillel)","Steinwald House","Steven Muller Building / STScl","Undergraduate Teaching Labs","Whitehead Hall","Wolman Hall","Wyman Park Building","1 E. 31st St.","5-15 W. 29th St.","115 W. University Parkway","3001 Remington","3001 N. Charles St.","3003 N. Charles St. South Entrance","3103 N. Charles St.","3105 N. Charles St.","3505 N. Charles St."]
    buildingList=[1,buildings, []]
    return buildingList
def LaSierraBuildings():
    #url="https://lasierra.edu/campus-map/"
    buildings=["Alumni Center", "Administration","Ambs Hall","Angwin Hall","Alumni Pavilion","Alumni Pavilion Annex","Alumni Pavilion Pool" ,"Archaeology","Calkins Hall","Convenience Center","Common Ground Pond","Cossentine Hall","Path of the Just (Campus Mall)","Clough Park","Custodial Warehouse","Dining Commons","Gladwyn Hall","Health & Exercise Science" ,"Hole Memorial Auditorium","Student/Staff Housing","Hamilton Terrace","Humanities Hall","Information Technology","Library","Library Mall","La Sierra Hall","Matheson Chapel","Natural Foods","Observatory","Palmer Hall","T. B. Price Science Complex","School of Education","San Fernando Hall","South Hall","Security Kiosk","San Pasqual Schoolhouse","Sierra Towers","Sierra Vista Hall","University Church","Visual Arts Center","Tom & Vi Zapara School of Business","Welcome Center/Campus Tours"]
    buildingList=[1,buildings, []]
    return buildingList
def LagunaBuildings():
    buildings=["Administration Building"]
    buildingList=[1,buildings,[]]
    return buildingList
def LehighBuildings():
    url="https://en.wikipedia.org/wiki/List_of_Lehigh_University_buildings"
    req=requests.get(url)
   # print(req.status_code)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("td")
  #  print(soup)
    buildings=[]
    for i in range(1,len(tableData),2):
        buildings.append(tableData[i].get_text())
    for i in range(len(buildings)):
        buildings[i]=buildings[i].replace("\n"," ")
    buildingList=[1,buildings, []]
    return buildingList
def LoyolaMarymountBuildings():
    buildings=["University Hall","William H. Hannon Library","Hilton Center for Business","Xaiver Hall","St. Robert's Hall","Charles Von der Ahe","Communications Arts","Burns Fine Art Center, Burns Annex","Hogan Hall","Murphy Recital Hall","Sacred Heart Chapel","Malone Student Center","Foley Building","Foley Annex","Seaver Science Hall","Life Sciences Building","Daum Hall","Pereira Hall of Engineering, Doolan Hall","Burns Recreation Center","Gersten Pavilion","Lion Athletic Center","Athletics Fields","Leavey 5","O'Malley Apartments","Leavey 4","Leavy 6",'McCarthy Hall',"Rains Hall","Jesuit Community","McKay Hall","Tenderich Hall","Hannon Apartments","Whealan Hall","Dey Rey North/South","Rosecrans Hall","Palm North/South","Doheny Hall"]
    buildingList=[1,buildings,[]]
    return buildingList
def MenloCollegeBuildings():
    buildings=["Administration","Admissions","Alumni & Development Office","Arrillaga Hall","Athletics Offices","Bowman Library","Brawner Hall","Campus Post Office","Campus Store","Cartan Athletic Fields","Club Sports","Dining Hall","El Camino Hall","Fitness Center","Florence Moore Hall","Haynes-Prim Pavilion (GYM)","Howard Hall","Innovation Center","Kratt Hall","Michaels Hall","O'Brien Hall","President's House","Quad","Russell Center","Security Office","Sports Pavilion","Student Union","Wunderlich Field"]
    buildingList=[1,buildings,[]]
    return buildingList
def MichiganStateBuildings():
    url="https://www.campus-maps.com/michigan-state-university/"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("a")
    buildings=[]
    for i in range(0,len(tableData)):
        buildings.append(tableData[i].get_text())
    for i in range(0,273):
        buildings.pop(0) #note that .pop(x), x is the index that we want to pop!
    for i in range(len(buildings)-9,len(buildings)):
        buildings.pop(-1)
    buildingList=[1,buildings, []]
    return buildingList
def MiddleburyBuildings():
    url="https://en.wikipedia.org/wiki/List_of_Middlebury_College_buildings"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("td")
    buildings=[]
    for i in range(1,len(tableData),4):
        buildings.append(tableData[i].get_text())
    buildings=buildings[:-1]
    buildingList=[1,buildings, []]
    return buildingList
def MorehouseBuildings():
    buildings=["Samuel T. Graves Hall","Joseph T. Robert Hall/Post Office","Sale Hall Annex","Sale Hall","John Hope Hall","John H. Hopps Jr. Technology Tower","Charles Merrill Hall","Benjamin E. Mays National Memorial","William H. Danforth Chapel","Triplex","Nabrit-Mapp-McKay Hall","Physical Plant","Wiley A. Perdue Residence Hall","B.R. Brazeal Hall/James B. Ellison College Infirmary","Franklin L. Forbes Arena","Samuel H. Archer Hall","Kilgore Residence Hall","Thomas Kilgore Jr. Campus Center","Campus Police","Chivers/Lane Dining Hall","Benjamin E. Mays Hall","LLC Residence Hall","Charles D. Hubert Residence Hall","W.E.B. DuBois Residence Hall","Frederick Douglass Resource/Archives Center","William Jefferson White Residence Hall","Claude B. Dansby Hall","Tennis Courts","Benjamin G. Brawley Hall","John H. Wheeler Hall","Joseph E. Lowery Boulevard Security Booth","Physical Plant Maintenance Building","B.T. Harvey Staudium/Edwin Moses Track","Martin Luther King Jr. International CHapel","Gloster Hall","Howard Thurman National Obelisk","Martin Luther King Jr. Statue","Walter E. Massey Leadership Center","Shirley A. Massey Executive Conference Center","Gloster Hall Annex","Parking Deck","Morehouse Bookstore","The Visitors Center","The Ray Charles Performing Arts Center","Aretha Robinson Hall","Davidson House","ROTC Building","Otis Moss Jr. Residential Suites","TRIO Program","Centruy Campus"]
    buildingList=[1,buildings,[]]
    return buildingList
def NationalBuildings():
    buildings=["College of Letters and Sciences","Sanford College of Education","School of Business and Management","School of Engineering and Computing","School of Health and Human Services","School of Professional Studies"]
    buildingList=[1,buildings,[]]
    return buildingList
def NYUBuildings():
    url="https://www.nyu.edu/students/student-information-and-resources/registration-records-and-graduation/registration/classroom-locations.html"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("td")
    buildings=[]
    for i in range(9,len(tableData)-203,2):
        buildings.append(tableData[i].get_text())
    for i in range(len(buildings)):
        buildings[i]=buildings[i].replace("\n\t\t\t\t\t\t\t\t\t","")
        buildings[i]=buildings[i].replace("\n\t\t\t\t\t\t\t\t","")
        buildings[i]=buildings[i].replace('\n',"")
        buildings[i]=buildings[i].replace("\xa0"," ")
    buildingList=[1,buildings, []]
    return buildingList
def NorthCarolinaStateBuildings():
    url="https://facilities.ofa.ncsu.edu/resources/buildings/"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("td")
    buildings=[]
    for i in range(0,len(tableData),7):
        buildings.append(tableData[i].get_text())
    buildings.pop(0)
    buildingList=[1,buildings, []]
    return buildingList
def NortheasternBuildings():
    url="https://en.wikipedia.org/wiki/Category:Northeastern_University_buildings"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("a")
    buildings=[]
    for i in range(44,len(tableData)-19):
        buildings.append(tableData[i].get_text())
    buildingList=[1,buildings, []]
    return buildingList
def NWPolytechnicBuildings():
    url="https://www.nwpolytech.ca/maps/#"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("a")
    buildings=[]
    for i in range(307,len(tableData)-20):
        buildings.append(tableData[i].get_text())
    buildingList=[1,buildings, []]
    return buildingList
def NorthwesternBuildings():
    url="https://maps.northwestern.edu/txt"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("a")
    buildings=[]
    for i in range(12,len(tableData)-20):
        buildings.append(tableData[i].get_text())
    buildingList=[1,buildings, []]
    return buildingList
def NotreDameBuildings():
    buildings=["St Mary's Hall","Financial Aid","Registrar","Business Office","International Student Office","School of Education Faculty","School of  Psychology Faculty",'Academic Support Center',"School of Business Management Faculty","Student Lounge","Julie Billiart Hall","Chapel Annex","Disability Resource Center","Madison Art Center","Advancement","Alumni Affairs","Conferences and Events","Housing","Tabard","Facilities Management","Toso Residence (Namur)","Human Resources Administration","Office of the President","Office of the Provost","Gellert Library","Wiegand Gallery","Province Center","Cuvilly Hall","Ralston Hall Mansion","Dining Hall","Taube Center","Koret Athletic Field","NDNU Theatre","St. Joseph Hall","New Hall","Gavin Hall"]
    buildingList=[1,buildings,[]]
    return buildingList
def OakValleyBuildings():
    buildings=[]
    buildingList=[1,buildings,["Santa Ana Campus"]]
    return buildingList
def OberlinBuildings():
    url="https://www2.oberlin.edu/external/EOG/ChronoofOCBuildings/ChronoOfOCBuildings.html"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("td")
    buildings=[]
    for i in range(10,len(tableData)-7,3):
        buildings.append(tableData[i].get_text())
    for i in range(len(buildings)):
        buildings[i]=buildings[i].replace(" \n      ","")
        buildings[i]=buildings[i].replace("\n      ","")
    buildingList=[1,buildings, []]
    return buildingList
def OccidentalBuildings():
    buildings=["Academic Commons/Mary Norton Clapp Library","Academic Quad","Alumni Gym Fitness center/Payton Jordan Athletic Center","Anderson Center for Environmental Sciences","Anderson Field","Annenberg President's House","AGC Administrative Center/Cannon Rotunda","Bell Field","Bell-Young Hall","Berkus Hall","BioScience Building","Booth Music and Speech Center",'Bird Studio',"Braun Hall","Campus Safety","Cannon Plaza","Chilcott Hall","Child Development Center","Choi Auditorium","Collins House/Office of Admission","Culley Athletic Facility","De Mandel Aquactics Center",'Emmons Wellness Center',"Erdman Hall","Facilities Management","Fowler Hall","Haines Hall","Hameetman Career Center","Herrick Memorial Chapel and Interfaith Center","Hinchliffe Hall","Intercultural Community center","Johnson Hall/ McKinnon Global Forum","Johnson Student Center and Freeman College Union",'Keck Theater',"Kemp Stadium/Patterson Field/Henry Track","KcKinnon Family Tennis Center/Robinson Family Terrace","Mitchell Garden","Moore Lab of Zoology","Mullin Family Studio and Art Gallery","Newcomb Hall","Norris Hall of Chemistry","Norris Residence Hall (North)","Norris Residence Hall (South)","Oxy Arts","Pauley Hall","Remsen Bird Hillside Theater",'Rush Gymnasium',"Samuelson Alumni Center","Samuelson Campus Pavilion/Tiger Cooler","Soccer Fields","Spencer Field House","Stearns Hall","Steward-Cleland Hall","Swan Hall","Sycamore Glen","Thorne Hall","Treehouse Building","Department of Urban and Environmental Policy","Urban and Environmental Policy Institute","Upward Bound","Weingart Center for the Liberal Arts","Wylie Hall"]
    buildingList=[1,buildings, []]
    return buildingList
def OtisCollegeBuildings():
    buildings=["Ahmanson Hall","Digital Printing Center","Laboratory Press/Letterpress",'Media Services',"Monhoff Printmaking Lab","Online Studio",'Screening Room',"Studenet Counseling Center","Admissions",'Campus Store',"Continuing Education and Pre-College Programs","Human Resources and Development","Mailroom","Purchasing","Student Health and Wellness Center","Academic Advising","Business Office and Payroll","Career Services","Communications and Marketing","Faculty/Staff Break Room","Institutional Advancement","One Stop: Financial Aid/Student Accounts/Registration","Provost",'Senior Administration/President',"Student Affairs","Foundation Liberal Arts and Sciences - Information Technology Office","Computer Lab","Digital Media","Tech Help Desk","Academic Mentoring",'Architecture/Landscape/Interiors',"Artists, Community, and Teaching/Interdisciplinary Studies", "Creative Action","Communication Arts","Graduate Graphic Design","Photography Lab","3-D Output Center","Model Shop","Toy Design","Café","Campus Security","Center for International Education","Facuty Teaching and Learning Center","Forum","Residence Life and Housing","Student Activities","Student Life Center","Fashion Archive","Fashion Sophomore/Junior","Sewing Studio","Fashion Design","Fashion Design and Illustration","Classrooms","Fitting Theater","Fashion Senior Sewing Studio","Dining Commons - Elaine's Millard Sheets Library","Student Learning Center","Media Lounge","Student Residences","Studio Lounge","Study Lounge","Kitchen Lounge","Galef Center for Fine Arts","Ben Maltz Gallery","Bolsky Gallery","Lighting Studio","Ceramics and Studio Sculptures","Fine Arts Graduate Writing","North Building","Product Design"]
    buildingList=[1,buildings,[]]
    return buildingList
def PacificLutheranBuildings():
    buildings=["Sawyer Annex","Sawyer Hall","Giesy Hall","Chapel of the Cross","Founders' Hall","Founders' Annex","Beasom Dormitory","Outdoor Gathering Space"]
    buildingList=[1,buildings,[]]
    return buildingList
def PacificOaksBuildings():
    buildings=["Learnning Commons and Library","Lobby","Admissions","Registrar's Office","Office of the President","Academic Affairs Program Managers","Computer Lab","Dean's Office"]
    buildingList=[1,buildings,[]]
    return buildingList
def PacificReligionBuildings():
    buildings=["Holbrook Building","Center for LGBTQ & Gender Studies in Religion"]
    buildingList=[1,buildings,[]]
    return buildingList
def PacificUnionBuildings():
    url="https://www.puc.edu/about-puc/campus-map"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("h4")
    buildings=[]
    for i in range(0,len(tableData)):
        buildings.append(tableData[i].get_text())
    for i in range(2):
        buildings.pop(-1)
    buildingList=[1,buildings, []]
    return buildingList
def PacificaGraduateBuildings():
    buildings=["Residence Hall","Opus Archives","Yurt","Kitchen","Dining Hall","Barrett Center","Library","Administration Building","Computer Resource Center","Lobby","Board Room","Administration Building"]
    buildingList=[1,buildings,[]]
    return buildingList
def PaloAltoBuildings():
    url="https://www.paloaltou.edu/about/departments-and-offices"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("td")
    buildings=[]
    for i in range(6,len(tableData),4):
        buildings.append(tableData[i].get_text())
    for i in range(len(buildings)):
        buildings[i]=buildings[i].replace("\xa0","")
    buildingList=[1,buildings, []]
    return buildingList
def PennStateBuildings():
    url="https://en.wikipedia.org/wiki/List_of_Penn_State_academic_buildings"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("li")
    buildings=[]
    for i in range(76,len(tableData)-161):
        buildings.append(tableData[i].get_text())
    buildingList=[1,buildings, []]
    return buildingList
def PepperdineBuildings():
    buildings=["Appleby Center","Amphitheatre","Adamson Plaza","Bookstore","Beaman Patio","Black Family Plaza Classrooms",'Cultural Arts Center',"Center for Communications and Business",'Central Receing',"Department of Public Safety","Elkins Auditorium","Firestone Fieldhouse","Fireside Room","Heritage Hall","Housing and Residence Life","Hub for Spiritual Life","Howard A. White Center","Joslyn Plaza","Kresge Reading Room","Keck Science Center","Light House","Music Building","Mullin Town Square","Payson Library","Pendleton Learning Center","Raitt Recital Hall","Rockwell Academic Center","Stauffer Chapel","Student Success Center","Smothers Threatre","Thornton Administrative Center","Tyler Campus Center","Harilela International Tennis Stadium","Villa Graziadio","Weisman Museum","Waves Cafe","Connor House","Phillips House","E. Pengilly House","Peppers House","Hayes House","White House","Fifield House","Pauley House","Rockwell Towers Residence Hall","Crocker House","J. Pengilly House","Knott House","Eaton House","Darnell House","Miller House","DeBell House","Banowsky House","Krown Alpha House","Krown Beta House","Shafer House","Sigma House","Seaside Residence Hall"]
    buildingList=[1,buildings,["Malibu Campus","West Los Angeles Graduate Campus","Calabasas Campus",""]]
    return buildingList
def PitzerBuildings():
    buildings=["Broad Center","Broad Hall","Gold Student Center",'Avery Hall & George C.S. Benson Auditorium',"Fletcher Hall","Scott Hall"]
    buildingList=[1,buildings, []]
    return buildingList
def PointLomaBuildings():
    buildings=["Bond Academic Center","Bresee Alumni House","Cabrillo Annex","Cabrillo Hall","Campus Facilities","Colt Hall","Culbertson Hall","Draper Hall","Evans Hall","Fermanian Business Center","Fermanian School of Business","Latter Hall","Mieras Hall",'Nicholson Commons',"Public Safety","Records","Rohr Hall","Rohr Science","Ryan Learning Center","Ryan Library","Sator Hall","Smee Hall","Starkey A","Starkey B","Starkey C","Taylor Hall","University Advancement","Welcome Center","Greek Amphitheatre","Cooper Music Center","Keller Visual Arts Center","Salomon Theatre","Athletics Office","Atheletic Training Center",'Golden Gym',"Brown Chapel","First Church of Nazarene","Prescott Prayer Chapel","Finch Hall","Flex Apartments 41-49","Goodwin Hall","Hendricks Hall","Klassen Hall","Nease Hall","Wiley Hall","Young Hall"]
    buildingList=[1,buildings,[]]
    return buildingList
def PomonaCollegeBuildings():
    url="https://www.pomona.edu/administration/facilities-campus-services/offices/mail/building-address-list"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("td")
    buildings=[]
    for i in range(0,len(tableData),2):
        buildings.append(tableData[i].get_text())
    for i in range(len(buildings)):
        buildings[i]=buildings[i].replace("\xa0","")
    buildingList=[1,buildings, []]
    return buildingList
def PrincetonBuildings():
    buildings=["1879 Hall","1901 Hall","1903 Hall","1912 Pavilion","1915 Hall","1927 Clapp Hall","1937 Hall","1938 Hall","1939 Hall","1952 Stadium","1967 Hall","1976 Hall","1981 Hall","Alexander Hall","Andlinger Center for Energy and the Environment","Architecture Laboratory","Architecture School","Art Museum","Arts Tower","Baker Hall","Baker Rink","Bedford Field","Bendheim House","Berlind Theatre","Blair Hall","Bloomberg Hall","Bobst Hall","Bogle Hall","Bowen Hall","Brown Hall","Burr Hall","Buyers Hall","Caldwell Field House","Campbell Field","Campbell Hall","Campus Club","Cannon Green","Cap & Gown Club","Cannon Dial Elm Club","Center for Jewish Life","Chancellor Green","Chapel","Charter Club","Chilled Water Plant","Clarke Field","Class of 1887 Boathouse","Cleveland Tower","Clio Hall","Cloister Inn","Cogeneration Plant","College Road Apartments","Colonial Club","Community Hall","Computer Science Building",'Cooling Towers',"Corwin Hall","Cottage Club","Cuyler Hall","DeNunzio Pool","Dickinson Hall","Dillon Court East","Dillon Court West","Dillon Gymnasium","Dinky Bar and Kitchen","Dod Hall","Dodge Hall","Dodge-Osborn Hall","East Pyne Hall","Edwards Hall","Effron Music Builidng","Elementary Particles Lab West","Engineering Quadrangle","Eno Hall","Feinberg Hall",'Ferris Thompson Apartments',"Fields Center","Fine Hall","Finney Field","Firestone Library","Fisher Hall","Fisher Hall (Whitman)","Forbes College","Foulke Hall","Frelinghuysen Field","Frick Chemistry Laboratory","Friend Center","Frist Campus Center","Garden Theatre","Gauss Hall","Graduate College","Green Hall","Grounds Storage Buildings","Guyot Hall","Hamilton Hall","Hargadon Hall","Helm Building","Henry Hall","Holder Hall","Hoyt Laboratory","Icahn Laboratory","Ivy Club","Jadwin Gymnasium","Jadwin Hall","Joline Hall","Jones Hall","Julis Romo Rabinowitz Building","Labyrinth Books","Lakeside Garage","Lakeside Apartments and Townhouses","Laughlin Hall","Lauritzen Hall","Lewis Library","Little Hall","Lockhart Hall","Maclean House","MacMillan Building","Madison Hall","Maeder Hall","Marx Hall","McCarter Threatre","McCosh Hall","McCosh Health Center","McDonnell Hall","Moffett Laboratory","Morrison Hall","Mudd Library","Murley-Pivirotto Family Tower","Murray Theater","Museum Store","Nassau Hall","New South Building","North Garage","Olden House","Palmer House","Pardee Field","Patton Hall","Peretsman Scully Hall","Peyton Hall","Princeton Neuroscience Institute","Princeton University Press",'Princeton University Store',"Procter Hall","Prospect Apartments","Prospect House","Pyne Hall","Quandrangle Club","Roberts Stadium","Robertson Hall","Rock Magnetism Laboratory","Roots Ocean Prime","Scheide Caldwell House","Schultz Laboratory","Scully Hall","Shea Rowing Center","Sherrerd Green","Sherrerd Hall","Simpson International Building","Spelman Halls","Springdale Golf Course","Stanhope Hall","Stephen Fitness Center","Streicker Bridge","Strubing Field","Terrace Club","Thermal Energy Storage Tank","Thomas Laboratory","TIGER","Tiger Inn","Tower Club","Upper Strubing Field","Visitor Parking Lot","Wallace Dance Building and Theater","Wallace Hall","Wawa","Weaver Track and Field Stadium","Wendell Hall","West Garage","West Lodge","Whig Hall","Wilcox Hall","Wilf Hall","Witherspoon Hall","Woolworth Center for Musical Studies","Wright Hall","Wu Hall","Wyman Cottage","Wyman House","Yoseloff Hall"]
    buildingList=[1,buildings, []]
    return buildingList
def ProvidenceChristianBuildings():
    url="https://www.providencecc.edu/divi_overlay/about-campus/"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("h2")
    buildings=[]
    for i in range(0,len(tableData)):
        buildings.append(tableData[i].get_text())
    buildings=buildings[1:]
    buildingList=[1,buildings, []]
    return buildingList
def PurdueBuildings():
    url="http://www.cyto.purdue.edu/cdroms/cyto1/14/pucl/flowcyt/campus.htm"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    buildingsAll=[]
    for i in soup.body.children: #ALTERNATIVE METHOD
        buildingsAll.append(i.string)
    buildings=[]
    for i in range(9,len(buildingsAll),5):
        buildings.append(buildingsAll[i])
    buildingList=[1,buildings, []]
    return buildingList
def RensselaerBuildings():
    url="https://en.wikipedia.org/wiki/List_of_RPI_buildings"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("span")
    buildings1=[]
    for i in range(107,len(tableData)-57):
        buildings1.append(tableData[i].get_text())
    buildings=[buildings1[0],buildings1[15],buildings1[21],buildings1[36],buildings1[41],buildings1[47],buildings1[52],buildings1[62],buildings1[67],buildings1[73],buildings1[83],buildings1[88],buildings1[93],buildings1[98],buildings1[103],buildings1[108],buildings1[113],buildings1[118],buildings1[123],buildings1[128],buildings1[133],buildings1[138],buildings1[148],buildings1[153],buildings1[158]]
    buildingList=[1,buildings, []]
    return buildingList
def RhodeIslandDesignBuildings():
    buildings=["68-72 South Main Street","173 Benefit Street","Aldrich Building","Angell Street Studios","Auditorium Building","Bank Building","Barstow House","Bayard Ewing Building (BEB)","Benson Hall","Canal Street Studios","Carpenter House","Carr House","Center for Integrative Technologies (CIT)","Central Power Plant (CPP)","Chace Center","College Building","Colonial Apartments","Congdon House","Design Center","Dexter House","Dexter House Studio","Dunnell House","Dwight House","Dyer Street Building - 123","East Hall","Ewing Multicutural Center","Firehouse","Fletcher Building","Homer Hall","Illustration Studies Building (ISB)","Industrial Design Building","Kinsley Warehouse","Larned House","Mandle Center (15 West)","Market House","Meeting Street Studios","Memorial Hall","Metcalf Building","Nickerson Hall","North Hall","Pardon Miller House","Point Street Studios","President's House","RISD Museum","Somain Barn Building","Somain Building 1","Somain Building 2","Somain Building 3","Somain Building 3","South Hall","Tanner Building","The House At Tillinghast Place","Tillinghast Place","Washington Place","Waterman Street Building","Weybosset Street Studios","What Cheer Garage + Studios","Woods-Gerry House"]
    buildingList=[1,buildings,[]]
    return buildingList
def RiceBuildings():
    url="https://registrar.rice.edu/facstaff/buildings-and-classrooms"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("td")
    buildings=[]
    for i in range(1,len(tableData),2):
        buildings.append(tableData[i].get_text())
    buildingList=[1,buildings, []]
    return buildingList
def RochesterTechBuildings():
    url="https://www.rit.edu/facilitiesmanagement/buildings-maps"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("td")
    buildings=[]
    for i in range(2,len(tableData),3):
        buildings.append(tableData[i].get_text().strip())
    buildingList=[1,buildings, []]
    return buildingList
def RutgersBuildings():
    url="https://dcs.rutgers.edu/classrooms/building-identification-codes"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("td")
    buildings=[]
    for i in range(5,len(tableData),4):
        buildings.append(tableData[i].get_text())
    buildingList=[1,buildings, []]
    return buildingList
def SaintJosephHawkHillBuildings():
    url="https://en.wikipedia.org/wiki/List_of_Saint_Joseph%27s_University_buildings"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("li")
    buildings=[]
    for i in range(50,len(tableData)-52):
        buildings.append(tableData[i].get_text())
    cleaned_buildings = [building.split(',', 1)[0] for building in buildings]
    buildingList=[1,cleaned_buildings, []]
    return buildingList
def SaintMaryBuildings():
    buildings=["Edward S. Ageno East","Edward S. Ageno West","Ferdinand and Camille Ageno Hall (C)","Marjorie David Ageno Hall (B)","Micheal E. Ageno Hall (A)","Aquinas Hall","Assumption Hall","Augustine Hall","Becket Hall","Claeys Hall North","Claeys Hall South","De La Salle Hall","Freitas Hall","Guerrieri Hall East","Guerrieri Hall West","Justin Hall","Mitty Hall","More Hall","Sabatte Hall","Syufy Hall","Thille Hall","Brousseau Hall","Brother Cornelius Art Center","Dante Hall","Filippi Academic Hall","Galileo Hall","Garaventa Hall","Geissberge Observatory","Korth Academic Center","Power Plant","Psychology","SMC Museum of Art","St. Albert Hall Library","Sichel Hall","Syufy Performing Arts","Oliver Hall","Delphine Intercultural Center","Bookstore","Fenlon Hall","Brother Urban Gregory Hall (BUG)","Hagerty Lounge","LeFevre Threatre","Saint Mary's Chapel","Siena House","Soda Activity Center","St. Joseph Hall","Brother Jerome West Hall - Visitory Center"]
    buildingList=[1,buildings, []]
    return buildingList
def SamuelMerrittBuildings():
    url="https://www.samuelmerritt.edu/discover/smu-campuses/oakland-campus"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("strong")
    buildings=[]
    for i in range(0,len(tableData)):
        buildings.append(tableData[i].get_text())
    tableData2=soup.findAll("b")
    for i in range(0,len(tableData2)):
        buildings.append(tableData2[i].get_text())
    for i in range(len(buildings)):
        buildings[i]=buildings[i].replace('\xa0',' ')
    buildings.remove(buildings[12])
    buildingList=[3,buildings, ["Oakland Campus","Sacramento Campus","San Francisco Peninsula Campus"]]
    return buildingList
def SanDiegoChristianBuildings():
    buildings=["San Diego Christian College Library","Gillespie Field"]
    buildingList=[1,buildings,[]]
    return buildingList
def SanDiegoStateBuildings():
    url="https://directory.sdsu.edu/"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("td")
    buildings=[]
    for i in range(1,len(tableData),2):
        buildings.append(tableData[i].get_text())
    buildingList=[1,buildings, []]
    return buildingList
def SanFranciscoStateBuildings():
    url="https://maps.sfsu.edu/"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("td")
    buildings=[]
    for i in range(1,len(tableData),2):
        buildings.append(tableData[i].get_text())
    buildingList=[1,buildings, []]
    return buildingList
def SanJoaquinBuildings():
    buildings=["New American Legal Clinic","Mediterranean Renaissance building"]
    buildingList=[1,buildings,[]]
    return buildingList
def SantaClaraBuildings():
    url="https://university-operations.scu.edu/facilities/space-data/building-information/"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("a")
    buildings=[]
    for i in range(90,len(tableData)-17):
        buildings.append(tableData[i].get_text())
    for i in range(len(buildings)):
        buildings[i]=buildings[i].replace("\xa0"," ")
    buildingList=[1,buildings, []]
    return buildingList
def SaybrookBuildings():
    url="https://cms.concept3d.com/map/accessible.php?id=1910&cId=52707"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("a")
    buildings=[]
    for i in range(2,len(tableData)):
        buildings.append(tableData[i].get_text())
    buildingList=[1,buildings, []]
    return buildingList
def ScrippsBuildings():
    buildings=["Alumnae Field and Underground","Balch Auditorium","Balch Hall","Baxter Hall","Bowling Green","Buildings and Grounds Department","Dartmouth House, 1030 EmPOWER Center","Denison Library, Ella Strong Sicilian Court","Edwards Humanities Building","Elm Tree Lawn","Facilities Department","Field House, Sallie Tiernan","Honnold Gate","Honnold/Mudd Library","Huntley Bookstore","Inscription Walk","Jaqua Quadrangle","Keck Science Department, W.M.","Malott Commons","Margaret Fowler Garden","McAlister Center","Millard Sheets Art Center","Performing Arts Center","Pool","Browning Scripps, Ellen","Clark, Grace Scripps","Dorsey, Susan Miller","Frankel, Cecil and Bessie","Gabrielle Jungels-Winkler","Kimberly, Mary","NEW Hall", "Routt, Mary","Routt Apartments","Toll, Eleanor Joy","Wilbur, Marguerite and Van Rensselaer","Revelle House, Ellen Clark","Richardson Dance Studio","SARLO","SCORE","Steele Hall","Vita Nova Hall","Wood Steps, Elizabeth Monroe","240 House"]
    buildingList=[1,buildings,[]]
    return buildingList
def SimpsonBuildings():
    buildings=["Owen Student Services Center","Admissions","LaBaume-Rudat Hall","Lecture Hall / A.W. Tozer Seminary","Science & Nursing Center","Laboratories","Francis-Grubbs Learning Center","Library","Future STEM Building","Maintenance Building","James M. Grant Student Life Center","Gymnasium / Music","Emeriti Dining Center","The Caf","Prayer Chapel","Collord-Humphries","Mod 7 Training Room","Thompson-Mangham Residence Hall","Irwin-Shellrude Residence Hall","Morgan-Sharpe Residence Hall","Currie-Ediger Residence Hall","Cooper-Heath Residence Hall","Measell-Taylor Residence Hall"]
    buildingList=[1,buildings,[]]
    return buildingList
def SmithBuildings():
    buildings=["8 College Lane","10 Prospect Street","Kahn Liberal Arts Institute","Offices/Student Activities","College Administration","40 Green Street","Faculty Offices","Development Office","Wurtele Center for Leadership","Admission Office","Ainsworth Gymnasium","Alumnae Gymnasium","Alumnae House","Bass Hall","Boathouse","Brown Fine Arts Center","Graham Hall","Hillyer Hall", "Hillyer Art Library","Museum of Art",'Burton Hall',"Campus Center","Campus Center","Capen Annex","Clark Hall","Conference Center","Crew House","David Center","Dawes House","Dewey Hall","Drew Hall","Facilities Management","Field House","Ford Hall","The Gables","Garrison Hall","Gill Hall","Hatfield Hall","Helen Hills Hills Chapel","Henshaw Complex","Indoor Track and Tennis Facility","John M. Greene Hall","Lilly Hall","Lyman Plant House and Conservatory","McConnell Hall","Mendenhall Center for the Performing Arts","Morgan Hall","Neilson Library","Pierce Hall","President's House","Sabin-Reed Hall","Sage Hall","Scott Gymnasium","Schacht Center for Health and Wellness","Seelye Hall","Stoddard Hall and Annex","Tilly Hall","Tyler Annex","Unity House","Wright Hall","Young Library","Albright House","Baldwin House","Capen House","Chapin House","Mary Ellen Chase House","Comstock House","Conway House","Cushing House","Cutter House","Eleanor Duckett House","Ellen Emerson House","54 Green Street","44 Green Street","Friedman Complex","Gardiner House","Haven House","Hopkins House","Hubbard House","Jordan House","Franklin King House","Lamont House","Lawrence House","Morris House","Morrow House","Northrop House","150 Elm Street","Park Annex","Park House","Parsons Annex","Parsons House","Laura Scales House","Sessions Annex","Sessions House","Talbot House","Tenney House","Tyler House","Washburn House","Wesley House","Wilder House","Martha Wilson House","Ziskind House"]
    buildingList=[1,buildings,[]]
    return buildingList
def SokaBuildings():
    buildings=["Scientific Research Laboratories","Soka Instructional Garden","Soka Instructional Aquaculture Facility","The Hamersley Environment Microbiology Laboratory","Life Sciences Building","Luis and Linda Nieves Observatory","Creative Arts Studio","Language and Culture Lab","Recreation Center","Peace Fountain & Lake","Founders Hall","Soka Performing Arts Center","Wangari Maathai Hall","Linus & Ava Helen Pauling Hall","Science Building","Mohandas & Kasturba Gandhi Hall","Daisaku & Kaneko Library","student Center","Sunrise Residence Hall","Abeona Residence Hall","Somnus Residence Hall","Sunset Residence Hall","Umoja Residence Hall","Aurora Residence Hall","Horizon Residence Hall","Lokahi  Residence Hall","Ubuntu Residence Hall","Acjachemen Residence Hall","Small Conference Center","Athenaeum","Guest Residence","Aliso & Wood Canyons Wilderness Park","Facilities Building"]
    buildingList=[1,buildings, []]
    return buildingList
def SonomaStateBuildings():
    buildings=["Alumni Grove","Athropological Studies Center","Art Building","Beaujolais Village","Bookstore","Building 49","Cabernet Village","Carson Hall","Children's School","Cooperage","Darwin Hall","Environmental Technology Center","Facilities Service","Fieldhouse","Green Music Center","Gymnasium","Holocaust & Genocide Memorial Grove","International Hall","Ives Hall","Lakes","Library","Nichols Hall","Observatory","Person Theatre","Recreation Center","Salazar Hall","Sauvignon Village","Schroeder Hall","Tuscany Village","Verdot Village","Weill Hall","Zinfandal Village"]
    buildingList=[1,buildings,[]]
    return buildingList
def SouthernMethodistBuildings():
    url="https://www.smu.edu/aboutsmu/maps/buildingindex"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("td")
    buildings=[]
    for i in range(0,len(tableData)):
        buildings.append(tableData[i].get_text())
    buildingList=[1,buildings, []]
    return buildingList
def SouthwesternLawBuildings():
    buildings=["Westmoreland Building","Bullocks Wilshire Builidng","Leigh Taylor Law Library","Julian Dixon Courtroom and Advocacy Center"]
    buildingList=[1,buildings,[]]
    return buildingList
def StanfordBuildings():
    url="https://en.wikipedia.org/wiki/Category:Stanford_University_buildings_and_structures"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("a")
    buildings=[]
    for i in range(44,len(tableData)-22):
        buildings.append(tableData[i].get_text())
    additional=["Allen Center for Integrated Systems","Applied Physics Building","Arboretum Children's Center","Arrilaga Alumni Center","Bechtel International Center","Black Community Services Center","Blake Wilbur Clinic","Bolivar House","Bowman Alumni House","Braun Music Center","Carnegie Institution","Cedar Hall","Center for Advanced Study in Behaviorial Science","Center for Educational Research at Stanford","Center for Turbulence Research","Chemical Biology Lorry Lokey","Codura Hall","Cummings Art Building","Cypress Hall","Durand Builidng","Electrical Engineering Building","Forsythe Hall","Gates Computer Sciences","Gilbert Biologial Sciences Building","Green Earth Sciences Building","High Energy Physics Lab","Keck Science Building","Landau Economics","School of Law","Mariposa House","Mayer Cancer Biology","School of Medicine","Meyer Library","Mitchell Earth Sciences Building","Memorial Church","Moore Materials Research","Mudd Chemistry Building","National Bureau of Econ. Research","Old Chemistry Building","Packard Children's Hospital","Pine Hall","Recycling Center","Redwood Hall","Sequoia Hall","Serra House","Skilling Building","Spruce Hall","Stanford Auxiliary Library","Sweet Hall","Stauffer Buildings","Track House","Ventura Hall","Wallenberg Hall","William R. Hewlett Teaching Center"]
    for i in range(len(additional)):
        buildings.append(additional[i])
    buildingList=[1,buildings, []]
    return buildingList
def SwathmoreBuildings():
    url="https://www.sccs.swarthmore.edu/users/03/dbing/history/buildings.html"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("td")
    buildings=[]
    for i in range(5,len(tableData),4):
        buildings.append(tableData[i].get_text())
    buildingList=[1,buildings, []]
    return buildingList
def SyracuseBuildings():
    url="https://library.syracuse.edu/special-collections-research-center/university-archives/buildings/alphabetical-list-of-su-buildings/"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("a")
    buildings=[]
    for i in range(119,len(tableData)-13):
        buildings.append(tableData[i].get_text())
    buildingList=[1,buildings, []]
    return buildingList
def TempleBuildings():
    url="https://www.collegemagazine.com/10-most-eccentric-pieces-of-architecture-at-temple-university/"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("h3")
    buildings=[]
    for i in range(0,len(tableData)-25):
        buildings.append(tableData[i].get_text())
    for i in range(len(buildings)):
        buildings[i]=buildings[i].replace("\xa0","")
    url2="https://en.wikipedia.org/wiki/Campus_of_Temple_University"
    req=requests.get(url2)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("dt")
    for i in range(0,len(tableData)):
        buildings.append(tableData[i].get_text())
    buildingList=[1,buildings, []]
    return buildingList
def TexasAMBuildings():
    url="https://ssc.tamu.edu/buildings/"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("td")
    buildings=[]
    for i in range(0,len(tableData),4):
        buildings.append(tableData[i].get_text())
    for i in range(len(buildings)):
        buildings[i]=buildings[i].lower()
        buildings[i]=buildings[i].title()
    buildingList=[1,buildings, []]
    return buildingList
def CollegeOfNJBuildings():
    url="https://libguides.tcnj.edu/c.php?g=628008&p=4412193"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("p")
    buildings=[]
    for i in range(55,len(tableData),3):
        buildings.append(tableData[i].get_text())
    for i in range(len(buildings)):
        buildings[i]=buildings[i].title()
    buildingList=[1,buildings, []]
    return buildingList
def MastersBuildings():
    buildings=["Reese Center for Science and Mathematics","Dunkin Student Center/Mustang Grill","Alumni House/Development/Chancellor's Office","Computer & Information Sciences","Powell Library/Legacy Center","JJ Rutherford Admin./Admissions/Financial Aid","Student Employment & Academic Resource Center","Computer Center","Vider Administrative Services","Wood Shop","King Hall/Student Activities","Campus Production","Hotchkiss Hall",'Slight Hall',"Dixon Hall","Waldock Hall",'C.W. Smith Hall',"Sweazy Hall","Tennis Courts","TMU Online","Health Center","Pearl C. Schaffer School of Education Center","Campus Safety","The MacArthur Center/Bross Court","Trophy Coffee","Louis Herwaldt Stadium","Fitness Center","Kinesiology and Physical Education","Cross Country Clubhouse","Plant Operations","Soccer Clubhouse","Communication Center","Biblical Studies Center","Music Center","Business Center","English and History Center"]
    buildingList=[1,buildings,[]]
    return buildingList
def NewSchoolBuildings():
    url="https://www.newschool.edu/buildings/venue-descriptions/"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("h5")
    buildings=[]
    for i in range(0,len(tableData)):
        buildings.append(tableData[i].get_text())
    for i in range(len(buildings)):
        buildings[i]=buildings[i].title()
    buildingList=[1,buildings, []]
    return buildingList
def ThomasAquinasBuildings():
    url="https://www.thomasaquinas.edu/about/one-program-two-coasts/california/campus-map"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("td")
    buildings=[]
    for i in range(2,len(tableData),2):
        buildings.append(tableData[i].get_text())
    for i in range(len(buildings)):
        buildings[i]=buildings[i].replace('\xa0'," ")
    buildings.pop(23)
    buildingList=[1,buildings, []]
    return buildingList
def TouroBuildings():
    buildings=["Truett Hall","Lander Hall","Farragut Inn","Wilderman Hall/College of Education and Health Sciences","Metabolic Research Center/Counseling & Student Health Center","College of Osteopathic Medicine","Library","IT Department","Pharmacy Practice Center","Student Garden","MOBEC","Outdoor Gym",'Meditation Garden',"The Grove","Harter Way","Mare Island Naval Hospital","Main Entrance","Thompson Hall"]
    buildingList=[1,buildings,[]]
    return buildingList
def TuftsBuildings():
    url="https://m.famousfix.com/list/buildings-at-tufts-university"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("h2")
    buildings=["Aidekman Arts Center","Alumnae Hall","Anderson Hall","Balch Arena Theater","Barum Hall","Bendetson Hall","Boston School of Occupational Therapy (BSOT)","Braker Hall","Cabot Center (The Fletcher School)","Carmichael Hall","Chase Center","Cohen Auditorium","Conference Bureau","Consens Gym","Curtis Hall","Dewick-MacPhie Dining Hall","Dowling Hall","Fine Arts House","Gantcher Center","Hill Hall","Lane Hall","Lewis Hall","Miller Hall","Miner Hall","Mugar Hall","Polin Center for Language and Cultural Studies"]
    for i in range(0,len(tableData)):
        buildings.append(tableData[i].get_text())
    buildingList=[1,buildings, []]
    return buildingList
def TulaneBuildings():
    url="https://www.yumpu.com/en/document/view/7703177/buildings-by-number-tulane-university-admission#google_vignette"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("p")
    buildings=[]
    for i in range(7,len(tableData)-18):
        buildings.append(tableData[i].get_text())
    building_names = re.findall(r'\d+\s+(.+?)(?=\s+\d+|\Z)', buildings[0]) #REGULAR EXPRESSION since before we have just one list with all the numbers and names
    for i in range(5):
        building_names.pop(-1)
    newBuildings=[]
    for i in range(len(building_names)):
        if building_names[i].isnumeric()==False:
            newBuildings.append(building_names[i])
    newBuildings[22]="Lavin-Bernick Center for University Life"
    newBuildings[-1]="38 Office of Undergraduate Admission"
    buildingList=[1,newBuildings, []]
    return buildingList    #split it on the spaces, [0-9]+ ?, regex patterns finding unmbers
def ChicagoBuildings():
    url="https://registrar.uchicago.edu/faculty-staff/classroom-scheduling/buildings-directory-2/"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("td")
    buildings=[]
    for i in range(0,len(tableData)):
        buildings.append(tableData[i].get_text())
    for i in range(len(buildings)):
        buildings[i]=buildings[i].replace("\xa0"," ")
    buildings.pop(3)
    buildingList=[1,buildings, []]
    return buildingList
def ColoradoBoulderBuildings():
    url="https://www.colorado.edu/brand/how-use/text-tone/editorial-style-guide/building-names"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("li")
    buildings=[]
    for i in range(16,len(tableData)-30):
        buildings.append(tableData[i].get_text())
    buildingList=[1,buildings, []]
    return buildingList
def ColoradoDenverBuildings():
    url="https://www.cuanschutz.edu/offices/facilities-management/parking-transportation-maps/cu-denver-campus-permit-parking/campus-maps"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("a")
    buildings=[]
    for i in range(11,27):
        buildings.append(tableData[i].get_text())
    for i in range(66,73):
        buildings.append(tableData[i].get_text())
    for i in range(len(buildings)):
        buildings[i]=buildings[i].replace(" - Events on Campus","")
        buildings[i]=buildings[i].replace(" -Events on Campus","")
    buildingList=[1,buildings, []]
    return buildingList
def ConnecticutBuildings():
    url="https://its.uconn.edu/network-refresh-project-complete/"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("td")
    buildings=[]
    for i in range(1,len(tableData),3):
        buildings.append(tableData[i].get_text())
    for i in range(len(buildings)):
        buildings[i]=buildings[i].title()
    buildingList=[1,buildings, []]
    return buildingList
def DelawareBuildings():
    url="https://sites.udel.edu/it-ums/buildings/"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("strong")
    buildings=[]
    for i in range(1,len(tableData)):
        buildings.append(tableData[i].get_text())
    buildingList=[1,buildings, []]
    return buildingList
def DenverBuildings():
    url="https://www.du.edu/registrar/faculty-staff-resources/course-scheduling-guide/room-building-list"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("td")
    buildings=[]
    for i in range(2,len(tableData),2):
        buildings.append(tableData[i].get_text())
    for i in range(len(buildings)):
        buildings[i]=buildings[i].replace('\n\t\t\t',' ')
        buildings[i]=buildings[i].replace('\n',' ')
    buildings.pop(3)
    buildingList=[1,buildings, []]
    return buildingList
def FloridaBuildings():
    url="https://en.wikipedia.org/wiki/List_of_University_of_Florida_buildings"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("td")
    buildings=[]
    for i in range(1,len(tableData)-20,7):
        buildings.append(tableData[i].get_text())
    for i in range(len(buildings)):
        buildings[i]=buildings[i].replace("\n"," ")
    buildingList=[1,buildings, []]
    return buildingList
def HawaiiManoaBuildings():
    url="https://manoa.hawaii.edu/campusmap/buildings/"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("strong")
    buildings=[]
    for i in range(0,len(tableData)):
        buildings.append(tableData[i].get_text())
    buildingList=[1,buildings, []]
    return buildingList
def HoustonBuildings():
    url="https://uh.edu/infotech/services/facilities-equipment/supported-classrooms/"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("a")
    buildings=[]
    for i in range(64,len(tableData)-35):
        buildings.append(tableData[i].get_text())
    buildingList=[1,buildings, []]
    return buildingList
def KentuckyBuildings():
    url="https://efacts.uky.edu/List"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("td")
    buildings=[]
    for i in range(1,len(tableData),4):
        buildings.append(tableData[i].get_text())
    for i in range(len(buildings)):
        buildings[i]=buildings[i].replace("\n                        ","")
        buildings[i]=buildings[i].replace("\n                    ","")
    buildingList=[1,buildings, []]
    return buildingList
def LaVerneBuildings():
    buildings=["Citrus Hall","Vista La Verne","The Oaks","Robert and Margaret Cogley Building","Arts and Communications Building","Barkely Building","Brandt Residence Hall","Bonita Building","Center for Advancement of Faculty Excellence","Central Services","Chapel","College of Business & Public Management","Dailey Theatre","Davenport Dining","E Street Building","ELS Language Center","Founders Hall","Graduate Academic Services","Hanawalt Fitness Center","Hanawalt House","Health Services","Hoover Building","Johnson Familiy Plaza","Landis Academic Center","Leo Hall","Lordsburg Building","Mainiero Hall","Miller Hall","Modular Classroom","Music Annex","Sneaky Park","South Quad","Sports Science & Athletic Pavilion","Stu-Han Residence Hall","University Advancement","Wilson Library","Woody Hall"]
    buildingList=[1,buildings,[]]
    return buildingList
def LouisvilleBuildings():
    url="https://louisville.edu/registrar/registration/related_information/building_codes"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("td")
    buildings=[]
    for i in range(6,len(tableData),4):
        buildings.append(tableData[i].get_text())
    buildingList=[1,buildings, []]
    return buildingList
def MarylandBuildings():
    url="https://en.wikipedia.org/wiki/List_of_University_of_Maryland,_College_Park_Campus_Buildings"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("td")
    buildings=[]
    for i in range(2,len(tableData)-80,5):
        buildings.append(tableData[i].get_text().strip())
    buildingList=[1,buildings, []]
    return buildingList
def MarylandBaltimoreCountyBuildings():
    url="https://www.umaryland.edu/designandconstruction/name-cross-reference/"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("td")
    buildings=[]
    for i in range(1,len(tableData),3):
        buildings.append(tableData[i].get_text())
    buildingList=[1,buildings, []]
    return buildingList
def MassachusettsAmherstBuildings():
    url="https://www.umass.edu/mail/campus-building-addresses"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("td")
    buildings=[]
    for i in range(3,len(tableData),3):
        buildings.append(tableData[i].get_text())
    for i in range(len(buildings)):
        buildings[i]=buildings[i].replace('\n\t\t\t\t','')
    buildings.pop(131)
    buildingList=[1,buildings, []]
    return buildingList
def MiamiBuildings():
    url="https://en.wikipedia.org/wiki/Category:Buildings_and_structures_of_Miami_University"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("a")
    buildings=[]
    for i in range(48,len(tableData)-22):
        buildings.append(tableData[i].get_text())
    buildingList=[1,buildings, []]
    return buildingList
def MichiganBuildings():
    url="https://ro.umich.edu/calendars/schedule-of-classes/locations"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("p")
    allText=[]
    for i in range(0,len(tableData)-3):
        allText.append(tableData[i].get_text())
    buildings=[]
    for i in range(len(allText)):
        buildings.append(allText[i].split("\n")[1])
    buildingList=[1,buildings, []]
    return buildingList
def NorthCarolinaChapelHillBuildings():
    url="https://planroom.unc.edu/FastBuildingList.aspx?field=FacilID"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("a")
    buildings=[]
    for i in range(18,len(tableData),2):
        buildings.append(tableData[i].get_text())
    for i in range(len(buildings)):
        buildings[i]=buildings[i].replace("                                                         ","")
        buildings[i]=buildings[i].replace("                                         ","")
        buildings[i]=buildings[i].replace("                                      ","")
        buildings[i]=buildings[i].replace('           ','')
        buildings[i]=buildings[i].replace('    ','')
        buildings[i]=buildings[i].replace("   ","")
        buildings[i]=buildings[i].replace('  ','')
    buildingList=[1,buildings, []]
    return buildingList
def NotreDameBuildings():
    url="https://dulac.nd.edu/atoz/building-directory/"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("h2")
    buildings=[]
    for i in range(0,len(tableData)):
        buildings.append(tableData[i].get_text())
    for i in range(len(buildings)):
        buildings[i]=buildings[i].replace("\xa0"," ")
    buildingList=[1,buildings, []]
    return buildingList
def OregonBuildings():
    url="https://en.wikipedia.org/wiki/List_of_University_of_Oregon_buildings"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("td")
    buildings=[]
    for i in range(0,len(tableData)-10,5):
        buildings.append(tableData[i].get_text())
    for i in range(len(buildings)):
        buildings[i]=buildings[i].replace("\n"," ")
    buildingList=[1,buildings, []]
    return buildingList
def UPennBuildings():
    url="https://facilities.upenn.edu/maps/locations"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("h2")
    buildings=[]
    for i in range(0,len(tableData)-1): 
        buildings.append(tableData[i].get_text())
    for i in range(6):
        url=f'https://facilities.upenn.edu/maps/locations?page={i}'
        req=requests.get(url)
        soup=BeautifulSoup(req.content,"html5lib")
        tableData=soup.findAll("h2")
        for i in range(0,len(tableData)-1): 
            buildings.append(tableData[i].get_text())
    buildingList=[1,buildings, []]
    return buildingList
def PittsburghBuildings():
    url="https://www.capitalassets.pitt.edu/building-list"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("td")
    buildings=[]
    for i in range(0,len(tableData),6): 
        buildings.append(tableData[i].get_text().title())
    for i in range(len(buildings)):
        buildings[i]=buildings[i].replace("\xa0"," ")
    buildingList=[1,buildings, []]
    return buildingList
def RedlandsBuildings():
    buildings=["Administration Building","Admissions Office","Alumni House","Ann Peppers Hall","Appleton Hall","Armacost Library","Art Studio","Baseball Stadium","Bookstore","Brown Amphitheater","Bulldog Café","Campus Events Office","Casa Loma Room","Chapel Annex","Chaplain's Office","Copy Center","Currier Gymnasium","Development Office","Duke Hall","Energy Center","Facilities Management","Farquhar Fields","Farquhar Utility Building","Field House","Financial Aid Office","Fine Arts","Fitness Center","Frederick Loewe Performance Hall","Gannett Center","Gallery","Greek Theatre","Gregory Hall","Hall of Letters","Hedco Hall","Hentschke Hall","Hornby Hall","Human Resources Office","Hunsaker University Center","Irvine Commons","Johnston Center","Jones Computer Center","Larsen Hall","Lewis Hall","Memorial Chapel","Office Services","Orton Center","Plaza Café","Post Office","President's Office","Public Safety Office","Quad","R Field","Redlands Symphony","Registrar","School of Business","School of Education","Softball Field","Student Accounts","Student Development Center","Student Health Center","Student Life Office","Ted Runner Stadium","Theatre Arts Building","Thompson Aquatic Center","Ticket Booth","Truesdail Speech Center","University Club","University Communications","University Hall","Verdieck Tennis Courts","Wallichs Theatre","Watchorn Hall","Willis Center","Anderson Hall","Bekins Hall","Bekins-Holt Hall","Brockton Apartments","California-Founders Halll","Central Avevnue Apartments","Cortner Hall","East Hall","Fairmont Hall","Grossmont Hall","Grove Apartments","Melrose Hall","Merriam Hall","North Hall","Williams Hall"]
    buildingList=[1,buildings,[]]
    return buildingList
def RochesterBuildings():
    url="https://tech.rochester.edu/building-names/"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("td")
    buildings=[]
    for i in range(2,len(tableData),4): 
        buildings.append(tableData[i].get_text().title())
    buildingList=[1,buildings, []]
    return buildingList
def SanDiegoBuildings():
    url="https://blink.ucsd.edu/sponsor/advancement/advancement-services/stewardship/named-buildings/index.html"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("td")
    buildings=[]
    for i in range(7,len(tableData),7): 
        buildings.append(tableData[i].get_text())
    buildingList=[1,buildings, []]
    return buildingList
def SanFranciscoBuildings():
    url="https://en.wikipedia.org/wiki/University_of_San_Francisco"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("ul")
    buildings=[]
    for i in range(46,47): 
        buildings.append(tableData[i].get_text())
    newBuildings=buildings[0].split("\n") #REGEX TO REMOVE PARENTHESES AND THE NUMBERS INSIDE THE PARENTHESES
    buildings_without_parentheses = [re.sub(r'\s*\([^)]*\)', '', building) for building in newBuildings]
    buildings_without_parentheses[-1]=buildings_without_parentheses[-1].replace("[30]","")
    buildingList=[1,buildings_without_parentheses, []]
    return buildingList
def TexasAustinBuildings():
    url="https://utdirect.utexas.edu/apps/campus/buildings/nlogon/facilities/"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("td")
    buildings=[]
    for i in range(0,len(tableData),4): 
        buildings.append(tableData[i].get_text().title())
    buildingList=[1,buildings, []]
    return buildingList
def VermontBuildings():
    url="https://www.uvm.edu/~campus/tour/buildinghistories.html"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("a")
    buildings=[]
    for i in range(6,len(tableData)): 
        buildings.append(tableData[i].get_text())
    for i in range(len(buildings)):
        buildings[i]=buildings[i].replace("\n              "," ")
        buildings[i]=buildings[i].replace("\n          "," ")
        buildings[i]=buildings[i].replace("    "," ")
        buildings[i]=buildings[i].replace("   "," ")
    locations_without_asterisk = [location for location in buildings if '*' not in location]
    filtered_locations = [location for location in locations_without_asterisk if 'reet' not in location and location.strip() != '']
    filtered_locations.remove("Angell Lecture Hall")
    filtered_locations.remove("Buckham Hall")
    filtered_locations.remove("Chittenden Hall")
    filtered_locations.remove("Medical Alumni Bldg.")
    filtered_locations.remove("University Store")
    buildingList=[1,filtered_locations, []]
    return buildingList
def VirginiaBuildings():
    url="https://en.wikipedia.org/wiki/Category:Buildings_of_the_University_of_Virginia"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("a")
    buildings=[]
    for i in range(45,len(tableData)-22): 
        buildings.append(tableData[i].get_text())
    buildingList=[1,buildings, []]
    return buildingList
def WashingtonBuildings():
    url="https://www.washington.edu/students/reg/buildings.html"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("a")
    buildings=[]
    for i in range(39,len(tableData)-16): 
        buildings.append(tableData[i].get_text())
    buildingList=[1,buildings, []]
    return buildingList
def WestLosAngelesBuildings():
    buildings=["Lobby","Library","UWLA School of Law","UWLA School of Business"]
    buildingList=[1,buildings, []]
    return buildingList
def WisconsinMadisonBuildings():
    url="https://www.map.wisc.edu/buildings/"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("td")
    buildings=[]
    for i in range(0,len(tableData),2): 
        buildings.append(tableData[i].get_text())
    buildingList=[1,buildings, []]
    return buildingList
def PacificBuildings():
    buildings=["Academic Advising and Career Services Center","Admission Office","Alan and Olive Gardemeyer Field","Alex G. Spanos Center","Alumni House","Anderson Hall","Art Center","Bannister Hall","Baun Hall","Bechtel International Center",'Benerd College',"Bill Simoni Field","Biological Sciences Center","Biological Laboratories","Brookside Field","Buck Memorial Hall","Burns Tower","Calaveras Hall","Callison Hall","Carter House","Casa Jackson","Casa Werner","Ceramic Studio","Chambers Technology Center","Chan Family Hall","Chan Family Health Sciences Learning Center and Clinics Building","Classroom Building","Colliver Hall","Communication Department","Conservatory of Music, Faye Spanos Concert Hall","Covered Performance Center","Cowell Wellness Center","Dance Studio","DeMarcus Brown Studio, Theatre ARts","DeRosa University Center","Disability Services","Don and Karen DeRosa University Center","Eberhardt School of Business","Edward and Alice Long Memorial Hall","Eiselen House","Elbert Covell Hall","Engineering and Computer Science","Engineering and Computer Science South Campus Labs","Eve Zimmerman Tennis Center","Farley House","Finance Center","George Wilson Hall","Geosciences Center","Graduate School","The Grove","Hand Hall","Health Science Library","Human Resources","Humanities Wing","Hydraulics Laboratory","Janet Leigh Theatre","Jeannette Pwell Art Center","Jessie Ballantyne Hall","John Ballantyne Hall","John T. Chambers Technology Center","Khoury Hall","Knoles Hall","Library","Long Theatre","McCaffrey Center","McConchie Hall","Military and Veterans Student Center","Monagan Hall","Morris Chapel","Olson Hall","Owen Hall","Pacific House","Price House","Psychology Department","Public Safety","Raymond Great Hall","Recital Hall","Rehearsal Hall","Ritter House","Robb Garden","School of Engineering and Computer Science","Weber Hall","Wemyss Hall","William Knox Holt Memorial Library"]
    buildingList=[1,buildings, []]
    return buildingList
def PeopleBuildings():
    buildings=["Online"]
    buildingList=[1,buildings, []]
    return buildingList
def WestBuildings():
    buildings=["University of the West Library", "University of the West Residential Halls"]
    buildingList=[1,buildings, []]
    return buildingList
def UrsinusBuildings():
    buildings=["The Commons","Corson Hall","Berman Museum of Art","Olin Hall","Bomberger Hall","Myrin Library","Pfhaler Hall","Innovation and Discovery Center","Thomas Hall","Wellness Center","The Kaleidoscope","Wismer Center","Campus Safety","IIE Center","Floy Lewis Bakes Center","Ritter Hall","Stauffer Hall","Paisley Hall","Beardwood Hall","Brodbeck Hall","Wilkinson Hall","Curtis Hall","Reimert Hall","201 9th Ave.","New Hall","Richter Hall","North Hall","Clamer Hall","476 Main St. CEDC Office","Commonwealth","Maples Hall","Fetterolf House","Sturgis House","Hobson Hall","Shreiner Hall","Musser Hall","Yost House","Duryea Hall","Zwingli Hall","624 Main St.","Olevian Hall","Schaff Hall","Lynnewood Hall","Omwake Hall","777 Main St.","Wicks House","Elliot House","Todd Hall","Isenberg Hall","732 Main St.","942 Main St.","944 Main St."]
    buildingList=[1,buildings,[]]
    return buildingList
def VanderbiltBuildings():
    url="https://cpc-fis.vanderbilt.edu/map/campusviewer/infopages/BuildingDirectory.html"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("td")
    buildings=[]
    for i in range(1,len(tableData),2): 
        buildings.append(tableData[i].get_text().title())
    for i in range(len(buildings)):
        buildings[i]=buildings[i].replace("Th","th")
        buildings[i]=buildings[i].replace("Nd","nd")
        buildings[i]=buildings[i].replace("21St","21st")
        buildings[i]=buildings[i].replace("the","")
    buildingList=[1,buildings, []]
    return buildingList
def VanguardBUildings():
    buildings=["Scott Academic Center","The East Wing Scott Academic Center","Samson's Cafe","Laguna Hall","Huntington Hall","Gymnasium","The Cove/Bookstore/Outtakes","The Café","Newport Hall","Balboa Hall","Catalina Hall","Theatre Modular","O. Cope Budge Library","Lyceum Theatre","Information Technology","Human Resources","Smith Hall","Natural Sciences Offices","Music Studios","Needham Chapel","Forrest Room/Campus Safety","Music and Theatre Offices","Newport Mesa Church","The Cove Office Modular","Social Sciences Offices","Psychology Offices","Grad Clinical Psych","Classrooms","Facilities Offices/Central Plant","NMC Dome","Heath Academic Center","Nursing Annex/Mailroom"]
    buildingList=[1,buildings,[]]
    return buildingList
def VassarBuildings():
    url="https://vcencyclopedia.vassar.edu/category/buildings-grounds-technology/buildings/"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("h2")
    buildings=[]
    for i in range(0,len(tableData)): 
        buildings.append(tableData[i].get_text())
    buildingList=[1,buildings, []]
    return buildingList
def VirginiaTechBuildings():#added 5/18/24
    url="https://www.vt.edu/about/locations/buildings.html"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("a",{"class": "vt-subnav-droplist-item"})
    buildings=[]
    for i in range(0,len(tableData)): 
        buildings.append(tableData[i].get_text().strip())
    buildingList=[1,buildings, []]
    return buildingList

def VirginiaCommonwealthBuildings():
    url="https://maps.vcu.edu/monroepark/list.html"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("a")
    buildings=[]
    for i in range(33,len(tableData)-15): 
        buildings.append(tableData[i].get_text())
    filtered_locations = [location for location in buildings if 'Back to top' not in location and location.strip() != ''] 
    buildingList=[1,filtered_locations, []]
    return buildingList
def WakeForestBuildings():
    url="https://en.wikipedia.org/wiki/Category:Wake_Forest_University_buildings"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("a")
    buildings=[]
    for i in range(45,55): 
        buildings.append(tableData[i].get_text())
    buildingList=[1,buildings, []]
    return buildingList
def WashUBuildings():
    url="https://wustl.edu/about/campuses/danforth-campus/"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("a")
    buildings=[]
    for i in range(133,len(tableData)-47): 
        buildings.append(tableData[i].get_text())
    filteredBuildings= [i for i in buildings if 'Top ↑' not in i] 
    buildingList=[1,filteredBuildings, []]
    return buildingList
def WesleyanBuildings():
    url="https://www.wesleyan.edu/registrar/general_information/building_codes.html"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("td")
    buildings=[]
    for i in range(1,len(tableData),4): 
        buildings.append(tableData[i].get_text().title())
    buildingList=[1,buildings, []]
    return buildingList
def WestcliffBuildings():
    buildings=["Academic Resource Center"]
    buildingList=[4,buildings,"Main Campus - Irvine, California","Los Angeles Campus - Santa Monica, California","Miami Campus - Miami, Florida","Orlando Campus - Orlando, Florida"]
    return buildingList
def WesternStateBuildings():
    buildings=["Western State College of Law Library","Main Building","Administration Building"]
    buildingList=[1,buildings,[]]
    return buildingList
def WesternHealthSciencesBuildings():
    url="https://www.westernu.edu/facilities/campus-hours/#accordion-1-button"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("td")
    buildings=[]
    for i in range(0,len(tableData),4): 
        buildings.append(tableData[i].get_text())
    buildings.pop(-2)
    buildings[3]="Pet Health Center (PHC)"
    buildingList=[1,buildings, []]
    return buildingList
def WestmontBuildings():
    url="https://www.westmont.edu/residence-hall-room-descriptions"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("strong")
    buildings=[]
    for i in range(0,len(tableData)-1): 
        buildings.append(tableData[i].get_text().title())
    add=["Adams center for the Visual Arts","Administrative Building B","Biology Laboratory","Carr Field","Carroll Hall","Conference Services","Deane Chapel","Deane Field","Deane Hall","Gaede Institute","Health and Counseling Center","Hubbard Hall","Kerr Memorial Center","Kerrwood Hall","Lovik Field","Martin Institute/Willard Center","Murchison Physical Education Complex and Pool","Music Building","Observatory","Porter Center","Porter Hall/Theatre","Reyonlds Hall","Clark Classroom","Nancy Voskuyl Prayer Chapel","Voskuyl Library","Westmont Ridley-Tree Museum of Art","Whittier Hall","Winter Hall for Science and Mathematics"]
    for i in range(len(add)):
        buildings.append(add[i])
    buildingList=[1,buildings, []]
    return buildingList
def WhittierBuildings():
    url="https://www.whittier.edu/reslife/halls"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("h2")
    buildings=[]
    for i in range(12,len(tableData)-2): 
        buildings.append(tableData[i].get_text().strip())
    add=["A.J. Villalobos Hall","Arnold Hall","Broadoaks Children's School","Campbell Residence Hall","College Hall","Counseling Center","Deihl Hall","Dezember Alumni House/Faculty Master House","Earlham House","Garrett Faculty Master House","Graham Athletic Center","Guilford House","Hamilton House","Hanover House","Harris Amphitheatre","Hartley Faculty Master House","Hastings House","Hoover Hall","Memorial Chapel","Memorial Stadium","Mendenhall Building","Philadelphia House","Platner Hall","Redwood Building","The Rock","Rose Hills Foundation Center for Library and Information Resources","Ruth B. Shannon Center for the Performing Arts","Slade Aquatic Center","Stauffer Science Center","Wanberg Residence Hall","Wardman Gym/Art center","Wardman Hall","Weingart Hall"]
    for i in range(len(add)):
        buildings.append(add[i])
    buildingList=[1,buildings, []]
    return buildingList
def WoodburyBuildings():
    buildings=["Ahmanson Main Space","Screening Room","San Diego Showroom","Wedge Gallery","Nan Rae Gallery","Academic Affairs","Admissions","Alumni Quad","Alumni Gallery","ASG House/Pool","Bookstore","Bowman Conference Room","Business Office","Cabrini Hall","Career Services","Central Services","Chandler Dean's Suite","Counseling Services","Deisgn Center","Development & Alumni Relations","Enkebool Courtyard","Fletcher Jones Foundation Auditorium","Health Services","Hensel Hall","Information & Security",'Information Technology',"Institute for Transdisciplinary Studies Offices","Judith Tamkin Fashion Gallery","Julius Shulman Institute","Isaacs Faculty Center","Kirby Hall Entertainment Media","Kirkendall Conference Room","Kummer Business Faculty Center","Los Angeles Times Library","Lynn Saffell Board Room","Malburg Atrium","Marketing & Enrollment","Miller Hall","Naidorf Hall","New Woody's","Nielsen Conference Room","North Hall","Office of the President","Powell Gallery","Ralph M. Parsons Studio","School of Architecture Offices","School of Business","School of Media, Culture & Design Offices","South Hall","Student Development","Tamkin Business Plaza","Nielsen Athletic Complex","Whitten Student Center","Wilshire Hall","Writing Center"]
    buildingList=[1,buildings, []]
    return buildingList
def WorcesterBuildings():
    url="https://www.wpi.edu/about/locations"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("td")
    buildings=[]
    for i in range(0,len(tableData)): 
        buildings.append(tableData[i].get_text().strip())
    buildingList=[1,buildings, []]
    return buildingList
def YaleBuildings():
    url="https://catalog.yale.edu/ycps/building-abbreviations/"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,"html5lib")
    tableData=soup.findAll("td")
    buildings=[]
    for i in range(1,len(tableData),2): 
        buildings.append(tableData[i].get_text().strip())
    buildingList=[1,buildings, []]
    return buildingList
def ZaytunaBuildings():
    buildings=["Euclid Dormitory","Maryam Bint Bwayba Dormitory"]
    buildingList=[2,buildings,["Lower Campus","Upper Campus"]]
    return buildingList


#print(getUniversityBuildings("Saint Joseph's University - Hawk Hill Campus")) #print should be commeneted out when running other files.
    
#QUESTIONS:f
#1) return doesn't seem to be returning anything in the terminal but switching it to print works.
#2) for universities with multiple campuses, should I make separate building lists for each campus or put them all in one list?
#3) for Andrews University, each element in the building list is like \n\t\t\t\tWelcome Center (Globe). How do I get rid of the /n/t in front?
#4) for ArtCenter College of Design, it has two campuses with its own buildings as well as three art studios. Right now the method only prints out the 5 facilities (in general), not the individual buildings within the two campuses. 
# format of [5, [[],[],[],[][]], [Name of campus 1, campus 2]] empty list for third elemetn for schools w 1 campsu

#5) for Barnard University 
        #Mixed within the list are elements like lobbies, Classrooms, etc: should those be removed from the list manually like buildingList[15].remove()
#yes
        #['ALTSCHUL HALL', 'Altschul Atrium', 'Tunnel Gallery', 'THE DIANA CENTER', 'Liz’s Place', 'Millicent Carey McIntosh Student Dining Room', 'Judith Shapiro Faculty Room', 'Louise Heublein McCagg ’59 Gallery', 'ELLIOTT HALL', 'Bella & Elsa S. Mehler Parlor', 'FUTTER FIELD\xa0', 'THE QUAD', 'The Arthur Ross Courtyard', 'Weber Living Room', "Jan R. and Marley Blue Lewis '05 Parlor", 'LOBBIES', 'Event Spaces', 'BARNARD HALL', 'Sulzberger Parlor', 'James Room', 'THE DIANA CENTER', 'Event Oval', 'MILBANK HALL', 'Ella Weed Room', 'THE QUAD', 'Helene L. Kaplan ’53 Tower Suite', 'Classrooms', 'Altschul Hall classrooms', 'Barnard Hall classrooms', 'Diana Center classrooms', 'Milbank Hall classrooms', 'Sulzberger Hall classroom']
#6) for Berklee College of Music, the buildings are in <a> link tags, but I''m having trouble finding the right <a> tags. 
#7) for brandeis univeresity, there is the same problem with <a> link tags. 
#8) for brown university, each element has \n at the end and .strip() gives an error that Nonetype is not callable.

#9) for California Lutheran university, the names are in <span> but the list returned is empty.
#10) for California Miramar University, there were really no building lists available so I just put in the 3 campus locations in the list.

#UNIVERSITIES THAT DO NOT WORK at all: 
#Alliant International University, American heritage university of southern california, american jewish university, berklee college of music, brandeis uni, 

#NOTES:
#1) I removed Berean Bible College bc there wasn't enough info
#2) Boston College has 4 campuses - 1 main one and other not as big for other internal schools like law shcool for example. I only included the main chestnut hill campus. 
#3) for California Institute of the Arts, the buildings were in <articles> and it was throwing a weird error so I manually inputted the few number of buildings.
#MULTIPLE CAMPUSES: ArtCenter College of Design

#Uni's without a building list - Alliant International University, American heritage university of southern california, american jewish university


#3/19/24
#Cal State LA has some issues 
#deleted Claremont lincoln university bc its 100% online, does that mean firebase needs to be updated?

#3/26/24
#what if i want to add a university? the buildings lat and long information etc in firebase?
#florida state university - code finds nothing, buildings not showing up here.
#in database.py, whats the point of def delete(self): and def upload_file(self, file_name, firebase_path):

#github
#can multiple ppl edit one android studio flutter project?
#github ?

#4/13/24
#lehigh unviersity
#michigan state

#4/20/24
#purdue uni



#5/4/24

#learned to prettify/ format things using functions like lower upper title capitalize
#learned how to deal with exceptions like building names in #text

#what if we want to add more buildings
#tulane university, its one big list all together

#5/11/24
#uni of michigan was interesting, maybe could have used regex but i didnt
#research regex for tulane
#deleted university of antelope valley bc of its closure due to financial issues
#used f string to navigate through multiple pages of buildings to ensure collecting all the building names
#filtering/cleaning using list comprehension

#regex for tulane
#university of san francisco could use regex??
#yes used regex for university of san francisco


#what if we want to add more buildings
#error in tulane uni for list index out of range
#for rec page, instead of paragraph text or in addition to it, can we show the universities of our app; patrick could probably do it, prob don't have to ask management but we/he can. problem is the format of chat vs our format
#will we have a log in?

#BUILDINGS TO ADD: georgia tech, university of maryland, virginia tech, 
'''

Alliant International University', 'American Heritage University of Southern California',
               'American Jewish University', 'Andrews University', 'ArtCenter College of Design', 'Barnard College',
                'Biola University', 'Boston College', 'Boston University', 'Bowdoin College','Brandeis University',
               'Brown University', 'California Institute of Integral Studies', 'California Institute of Technology',
               'California Institute of the Arts', 'California Lutheran University', 'California Miramar University',
               ***'California Polytechnic State University, Pomona', 'California South Bay University',
                'California State University Channel Islands',
               'California State University San Marcos', 'California State University, Bakersfield',
               'California State University, Chico', 'California State University, East Bay',
               'California State University, Fresno', 'California State University, Fullerton',
               'California State University, Los Angeles', 'California State University, Monterey Bay',
               'California State University, Northridge', 'California State University, Sacramento',
               'California State University, San Bernardino', 'California State University, Stanislaus',
               'Cambridge College', 'Carnegie Mellon University', 'Case Western Reserve University',
               'Chapman University', 'Charles R. Drew University of Medicine and Science',
               'Claremont Graduate University', 'Claremont Lincoln University', 'Claremont McKenna College', 'Colby College', 'Colgate University','College of the Holy Cross',
               'Columbia University', ****'Concordia University Irvine', 'Cornell University', 'Dartmouth College',
               'DeVry University', 'Deep Springs College', 'Dominican University of California', 'Drexel University',
               'Duke University', 'Eckerd College','Emory University',  'Florida State University',
               'George Mason University', 'George Washington University','Georgetown University', 'Golden Gate University',
               'Graduate Theological Union', 'Grinnell College','Hamilton College','Harvard University', 'Harvey Mudd College', 'Haverford College','Holy Names University',
               'Howard University', 'Humphreys University', 'Illinois Institute of Technology',
               'Indiana University Bloomington', 'Johns Hopkins University', 
               'La Sierra University',
                'Laguna College of Art and Design', 'Lehigh University',
               'Loyola Marymount University', 'Menlo College',
               'Michigan State University', 'Middlebury College', 'Morehouse College','National University', 'New York University','North Carolina State University',
               'Northeastern University', 'Northwestern Polytechnic University', 'Northwestern University',
               'Notre Dame de Namur University', 'Oak Valley College', 'Oberlin College','Occidental College', 
               #'Oikos University',
               'Otis College of Art and Design', 'Pacific Lutheran Theological Seminary', 'Pacific Oaks College',
               'Pacific School of Religion', 'Pacific Union College', 'Pacifica Graduate Institute',
               'Palo Alto University', 'Pennsylvania State University', 'Pepperdine University', 'Pitzer College', 'Point Loma Nazarene University',
               'Pomona College', 'Princeton University', 'Providence Christian College', 'Purdue University',
               'Rensselaer Polytechnic Institute', 'Rhode Island School of Design','Rice University', 'Rutgers University', "Saint Mary's College of California",
               'Samuel Merritt University', 'San Diego Christian College', 'San Diego State University',
               'San Francisco State University', 'San Joaquin College of Law', 'Santa Clara University',
               'Saybrook University', 'Scripps College', 'Simpson University', 'Smith College','Soka University of America',
               'Sonoma State University', 'Southern Methodist University', 'Southwestern Law School',
               'Stanford University', 'Swathmore College','Syracuse University', 'Temple University', 'Texas A&M University', 'The College of New Jersey'
               "The Master's University", 'The New School','Thomas Aquinas College', 'Touro University California', 'Tufts University',
               'Tulane University', 'University of Antelope Valley', 'University of Chicago','University of Colorado Boulder', 'University of Colorado Denver','University of Connecticut',
               'University of Denver', 'University of Florida', 'University of Hawaii at Manoa',
               'University of Houston', 'University of Kentucky','University of La Verne', 'University of Louisville',
               'University of Maryland, Baltimore County', 'University of Massachusetts Amherst', 'University of Miami',
               'University of Michigan', 'University of North Carolina at Chapel Hill', 'University of Notre Dame', 'University of Oregon',
               'University of Pennsylvania', 'University of Pittsburgh', 'University of Redlands',
               'University of Rochester', 'University of San Diego', 'University of San Francisco',
           'University of Texas at Austin', 'University of Vermont','University of Virginia',
               'University of Washington', 'University of West Los Angeles', 'University of Wisconsin-Madison',
               'University of the Pacific', 'University of the People', 'University of the West', 'Ursinus College',
               'Vanderbilt University', 'Vanguard University', 'Vassar College','Virginia Commonwealth University',
               'Wake Forest University', 'Washington University in St. Louis', 'Wesleyan University', 'Westcliff University',
               'Western State College of Law', 'Western University of Health Sciences', 'Westmont College',
               'Whittier College', 'Woodbury University', 'Worcester Polytechnic Institute', 'Yale University',
               'Zaytuna College']

'''
