import requests
import urllib.parse
import json
from bs4 import BeautifulSoup

s = requests.Session()

def fetch(url, data=None):
    if data is None:
        return s.get(url).content
    else:
        return s.post(url, data=data).content

# fixme so q = {key word}
# not software engineer
internships = {}
paginator = 0
counter = 0
while(paginator < 60):
    URL = "https://www.indeed.com/jobs?q=software+engineer&jt=internship&start=" + str(paginator)

    list_soup = BeautifulSoup(fetch(URL), 'html5lib')
    jobs = list_soup.findAll('div', attrs={'class':'jobsearch-SerpJobCard'})

    for job in jobs:
        jobId = job.get('id')
        title = job.findAll('a', attrs={'class':'jobtitle'})[0].get('title')
        company = job.findAll('span', attrs={'class':'company'})[0].contents[0].strip()
        link = "https://www.indeed.com" + job.findAll('a', attrs={'class':'jobtitle'})[0].get('href')
        job_soup = BeautifulSoup(fetch(link), 'html5lib')
        strings = job_soup.findAll('div', attrs={'class':'jobsearch-jobDescriptionText'})[0].stripped_strings
        body = ""
        for string in strings:
            body = body + string.strip()
        internships[counter] = {
            "title": title,
            "company": company,
            "link": link,
            "body": body
        }
        counter = counter + 1

    paginator = paginator + 10

json = json.dumps(internships)
f = open("internships.json","w+")
f.write(json)
f.close()
