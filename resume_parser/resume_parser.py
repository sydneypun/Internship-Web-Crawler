# Resume Parser Function
# A Note From Team Nougat: This resume parser function utilizes a library developed by Omkar Pathak
# https://github.com/OmkarPathak/pyresparser
# Resume Parsing Code referenced from this website: https://www.omkarpathak.in/2018/12/18/writing-your-own-resume-parser/

import string
import glob
import re
import sys
import importlib
import os
from pathlib import Path
from pyresparser import ResumeParser
import nltk
nltk.download('stopwords')

def extractSkills(resume_list):
    skill_list = []
    # Comparing resume.txt with skills.txt file
    with open("/Users/nealgoyal/Desktop/new/final-project-nougat/resume_parser/skills.txt", "r") as rf:
        for line in rf:
            skill_list.append(line.strip())

    query_list = []
    for word in resume_list:
        if word in skill_list:
            query_list.append(word)

    return query_list

def main ():
    # Resume Parser Call
    # Calling ResumeParser library to parse PDF resume
    data = ResumeParser("/Users/nealgoyal/Desktop/new/final-project-nougat/resume_parser/Engineering_Resume_19-20.pdf").get_extracted_data()

    with open("/Users/nealgoyal/Desktop/new/final-project-nougat/resume_parser/resume.txt", "w", encoding='utf-8') as rf:
        rf.truncate()
        rf.write(str(data))

    resume_list = []

    # Formatting resume.txt file
    remove = dict.fromkeys(map(ord, '\n ' + string.punctuation))
    # Comparing resume.txt with skills.txt file
    with open("/Users/nealgoyal/Desktop/new/final-project-nougat/resume_parser/resume.txt", "r", encoding='utf-8') as fin:
        for line in fin:
            for word in line.split():
                word = word.translate(remove)
                resume_word = word.lower()
                resume_list.append(resume_word)
    print(resume_list)
    query_list = extractSkills(resume_list)

    #with open("/Users/nealgoyal/Desktop/new/final-project-nougat/resume_parser/query_skills.txt", "w") as file_out:
        #file_out.truncate()
        #file_out.write(str(query_list))

if __name__ == "__main__":
    main()
