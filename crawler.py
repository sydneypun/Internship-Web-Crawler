import requests 
import urlparse
import json
from flask import request
from bs4 import BeautifulSoup 

# app = Flask(__name__)
# @app.route('/', methods=['POST', 'GET'])

s = requests.Session()

def fetch(url, data=None):
    if data is None:
        return s.get(url).content
    else:
        return s.post(url, data=data).content

def industrySearch():
    error = None
    if valid_industry(industry):
        return query_industry(industry)
    else:
        error = 'Invalid industry'
        return
    # if request.method == 'POST':
    #     if valid_industry(request.input['industry']):
    #         return query_industry(request.input['industry'])
    #     else:
    #         error = 'Invalid industry'

def industry_to_string(industry):
	industry = [letter.lower() for letter in industry]
	industry = ''.join(industry)
	industry = industry.replace(" ", "+")
	return industry

def valid_industry(industry):
	industry = industry_to_string(industry)
	URL = "https://www.indeed.com/jobs?q=" + industry + "&l="

	isValid_soup = BeautifulSoup(fetch(URL), 'html5lib')
	invalid = isValid_soup.findAll('div', attrs={'class':'bad_query'})
	if (invalid != []):
		return True

	return True

def query_industry(industry):
	# make input industry lowercase string separated by "+" instead of " "
	industry = industry_to_string(industry)
	internships = {}
	paginator = 0
	while(paginator < 60):
		URL = "https://www.indeed.com/jobs?q=" + industry + "&jt=internship&start=" + str(paginator)

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
			internships[jobId] = {
				"title": title,
				"company": company,
				"link": link,
				"body": body
			}

		paginator = paginator + 10

	json_ = json.dumps(internships)
	f = open("internships.json","w+")
	f.write(json_)
	f.close()
				

# call meathod(s)
industrySearch()