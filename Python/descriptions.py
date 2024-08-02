#2/10/24
#uses web scraping and Selenium to get the university general info for every school in school_list

from selenium import webdriver #webdriver is like a function called from the file
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from universities import school_list
#without 'from', we are importing the file itself
#import selenium vs from ... import...
import time

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=chrome_options)


def getInfo(university):
    url=f"https://www.google.com/search?q={university} university general info"
    driver.get(url) #"runs" the url
    time.sleep(2) #if the page takes too long to load, time.sleep gives it more time and then searches

    #info=driver.find_element(By.XPATH,"//span[@class=\"hgKElc\"]")
    info=driver.find_element(By.CLASS_NAME, "hgKElc")

    #quotes inside quotes: 1) '' 2) \" \"
    #find_element returns the first occurence 
    return info.text #returns gives function a value, replaces getInfo("UCI")
# print(getInfo("Georgia Institute of Technology"))
'''
for i in school_list:
    print(i)
    print(getInfo(i))
    '''
#university of the west, texas a m, the masters uni, thomas aquinas college, oak valley, ca south bay, andrews
#University of the West is a private, nonprofit university located in Los Angeles County, near the San Gabriel Mountains. Our beautiful green campus, modern classrooms, full-service library, on-site residence halls, and recreational facilities make UWest an educational oasis within the bustling Los Angeles metropolis.  
#Texas A&M University opened in 1876 as the state's first public institution of higher learning. Today, we are a research-intensive main university dedicated to sending leaders out into the world prepared to take on the challenges of tomorrow. Texas A&M is one of the largest public universities in the nation, and one of the few to have land-, sea- and space-grant designations. We are also the main university of The Texas A&M University System and a member of the Association of American Universities.
#The Master's University is a private non-denominational Christian university in Santa Clarita, California. The mission of The Master’s University is to empower students for a life of enduring commitment to Christ, biblical fidelity, moral integrity, intellectual growth and lasting contribution to the Kingdom of God worldwide.
#Thomas Aquinas College is a private Catholic liberal arts college with its main campus in Ventura County, California. A second campus opened in Northfield, Massachusetts in 2018. Its education is based on the Great Books, and students are instructed via the seminar method. 
#Oak Valley College is smart, debt-free, and together. The small-school environment creates a close-knit familial community. Oak Valley is innovative, efficient, Christ-centered college that helps students earn their Bachelor of Arts in Business degree in less time, for less money. For a fraction of what other universities cost, you’ll get a high-quality, in-person, practical experience at Oak Valley College. Best of all, graduate without the burden of student loan debt, so you are free to pursue your dreams.
#California South Bay University is a BPPE approved private educational institution based in Sunnyvale, California. California South Bay University offers the following degree programs: Master of Business Administration, Master of Science in Computer Science. 
#Today, Andrews is the best-known Adventist educational institution in the world. Students from across the United States and around the globe are attracted to Andrews because of what we stand for and what we offer. "U.S. News and World Report" says that Andrews is one of the most culturally diverse universities in the nation. Andrews University is a diverse and innovative community ready to help the next generation of World Changers deepen their knowledge, enrich their faith and change the world.
#Palo Alto University (PAU) is a non-profit, private educational institution in Palo Alto, California, United States. The school was founded in 1975 as the Pacific Graduate School of Psychology (PGSP). Palo Alto University offers two undergraduate degree programs (Bachelor of Science (B.S.) in Psychology and Social Action and B.S. in Business Psychology) and five graduate programs: a Ph.D. in Clinical Psychology; a Psy.D. in Clinical Psychology as part of a consortium with Stanford University, and two master's degree programs: an M.A. in Counseling, and an M.S. in Psychology. PAU subscribes to the practitioner-scientist training model, a variation of the Boulder scientist-practitioner model, which emphasizes clinical practice along with scientific training. PAU has an interconnected relationship with Stanford University and the Stanford University School of Medicine. PAU maintains its doctoral program in conjunction with Stanford University, often employs its students in Stanford research laboratories, and houses faculty members who teach at both institutions.

#Not sure if La Sierra Uni works, but La Sierra University is a private institution that was founded in 1922. It has a total undergraduate enrollment of 1,263 (fall 2022), and the campus size is 150 acres. It utilizes a quarter-based academic calendar. La Sierra University's ranking in the 2024 edition of Best Colleges is Regional Universities West, #41.






