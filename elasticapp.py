import requests, json, os
from elasticsearch import Elasticsearch
import json

directory = '/'

# TF IDF

summaries = {}

with open('internships.json') as f:
    summaries = json.load(f)


# print(summaries["pj_1bcef3d9fc1b0b32"]["title"])

# ELASTIC SEARCH

res = requests.get('http://localhost:9200')
print (res.content)
es = Elasticsearch([{'host': 'localhost', 'port': '9200'}])

i = 1

for filename in os.listdir(directory):
    if filename.endswith(".json"):
        f = open(filename)
        docket_content = f.read()

        # Send the data into es
        es.index(index='myindex', ignore=400, doc_type='docket',
        id=i, body=json.loads(docket_content))
        i = i + 1
