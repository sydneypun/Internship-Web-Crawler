import json
import nltk
import re
import itertools
from itertools import chain
import os
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
nltk.download('punkt')

# -----------------------------------
# ORGANIZING DATA
# -----------------------------------
def pre_process(text):

    # lowercase
    text=text.lower()
    #remove tags
    text=re.sub("<!--?.*?-->","",text)
    # remove special characters and digits
    text=re.sub("(\\d|\\W)+"," ",text)
    return text

# -----------------------------------
# STOP WORDS
# -----------------------------------
def get_stop_words(stop_file_path):
    with open(stop_file_path, 'r', encoding="utf-8") as f:
        stopwords = f.readlines()
        stop_set = set(m.strip() for m in stopwords)
        return frozenset(stop_set)

# -----------------------------------
# PARSING JSON
# -----------------------------------

group = []
summaries = []
links = []

with open('internships.json') as f:
    internships = json.load(f)

docId = []
for num in range(0,101):
    docId.append(str(num))

for id in docId:
    summaries.append(internships[id]["body"])

for id in docId:
    links.append(internships[id]["link"])

for id in docId:
    case = {'title': internships[id]["title"], 'company': internships[id]["company"], 'summary': internships[id]["body"], 'link': internships[id]["link"] }
    group.append(case)

# Calling pre_process function
newSums = []
for summary in summaries:
    newSums.append(pre_process(summary))


#load a set of stop words
stopwords=get_stop_words("stopwords.txt")


# -----------------------------------
# COMP
# -----------------------------------

topJobs = {}

with open('/Users/nealgoyal/Desktop/new/final-project-nougat/resume_parser/query_skills.txt', "r") as rf:
    skills_list = rf.read()

res = []
for skill in skills_list:
    for data in group:
        if(skill in data['summary']):
            res.append(data)

top5 = res[:5]
print(top5)

for data in top5:
    for num in range(6):
        topJobs[num] = {
            "title": data['title'],
            "company": data['company'],
            "link": data['link'],
        }


json = json.dumps(topJobs)
f = open("topJobs.json","w+")
f.write(json)
f.close()

save_path = '/Users/nealgoyal/Desktop/new/final-project-nougat/web_application/web_application/app_core/static'
completeName = os.path.join(save_path, "myfile.txt")

file= open(completeName,"w")
for data in top5:
    file.write(data['title'] + "<br>")
    file.write('\n')
    file.write("<a href=" + data['link'] + ">Application Link" + "</a>" +  "<br>" + "<br>")
    file.write('\n')
    file.write('\n')

file.close()

# -----------------------------------
# TESTING
# -----------------------------------
