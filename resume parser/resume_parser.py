# Resume Parser Function 
# A Note From Team Nougat: This resume parser function utilizes a library developed by Omkar Pathak
# https://github.com/OmkarPathak/pyresparser
# Resume Parsing Code referenced from this website: https://www.omkarpathak.in/2018/12/18/writing-your-own-resume-parser/

import string
import re
import sys
import importlib
import os
from pyresparser import ResumeParser
import nltk
nltk.download('punkt')

def extractSkills(resume_list): 
    skill_list = []
    skill_file = os.path.dirname(__file__) + "/skills.txt"
    # Comparing resume.txt with skills.txt file 
    with open(skill_file, 'r') as f: 
        for line in f: 
            skill_list.append(line.strip())
    
    query_list = []
    for word in resume_list:
        if word in skill_list:
            query_list.append(word)
    
    return query_list     

def main (): 
    # Calling ResumeParser library to parse PDF resume 
    data = ResumeParser("C:/Users/sydne/OneDrive/Documents/Github/final-project-nougat/resume_parser/Engineering_Resume_19-20.pdf").get_extracted_data()
   
    # Added encoding utf-8 to prevent unicode error
    with open("C:/Users/sydne/OneDrive/Documents/Github/final-project-nougat/resume_parser/resume.txt", "w", encoding='utf-8') as rf:
        rf.truncate()
        rf.write(str(data))
    
    resume_list = []
    # Formatting resume.txt file 
    remove = dict.fromkeys(map(ord, '\n ' + string.punctuation))
    resume_file = os.path.dirname(__file__) + "/resume.txt"
    # Comparing resume.txt with skills.txt file 
    with open(resume_file, 'r', encodings='utf-8') as f: 
        for line in fin:
            for word in line.split(): 
                word = word.translate(remove)
                resume_word = word.lower()
                resume_list.append(resume_word)

    query_list = extractSkills(resume_list)
    file_out = open(os.path.dirname(__file__) + "/query_skills.txt", "w")
    file_out.truncate()
    file_out.write(str(query_list))

if __name__ == "__main__":
    main()