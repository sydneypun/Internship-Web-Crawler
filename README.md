# Final Project: Team Nougat

## Internship Web Crawler 

Team Members: Emma Rivera, Neal Goyal, and Sydney Pun 

Github Repo Name: https://github.com/CS-UCR/final-project-nougat

__Overview:__ This internship web crawler seeks to simplify the internship searching process. With this web application, gone are the days in which students spend hours scouring the internet for internships. Instead, the searching process will be expedited because our application allows the user to simply upload their PDF resume and a ranked list of internship opportunities will be a click away. 

__Description of Part 1 (Crawling):__ We will build a web crawler in Python. We plan to crawl company pages in search of their internship opportunity listings. The libraries that we have considered are Scrapy and BeautifulSoup. Although Scrapy is a powerful web framework that allows for the extraction, processing, and storing of web data, it has a larger learning curve than BeautifulSoup which in comparison, is slower unless multiprocessing is used. As a result, we will consider testing both libraries to see which one is the best fit for our crawler.  

__Description of Part 2 (Retrieval):__ We reviewed the TA’s documentation on both indexing libraries. We also saw his examples from discussion on using Lucene for his project on CA DMV. We decided to go with Lucene because of the TA’s guidance on the benefits of Lucene. We will be using a Java Lucene wrapper called PyLucene to index our internship web crawler. Our MVP will be querying major, GPA, skills to match opportunities. The trickier part will be to evaluate experience level. In our second iteration, we will increase our scope to parse through experience and curate a more personalized internship list matching the individual’s experience level.

__Description of Part 3 (Extension):__ We will extend this web crawler by transforming it into a web application. Our web application will be developed with the web framework Django because it is a Python framework that allows for the integration of retrieval tools such as ElasticSearch and Lucene. With this web application, a front-end user-interface will allow the user to upload their PDF resume. We will then proceed to use page rank to return a ranked list of internship opportunities. The page rank algorithm will be constructed by identifying the similarities between the queried GPA, skill sets, major, etc. from the resume and the indexed web pages that were crawled. In addition, the application deadline for the internship opportunity will also be considered in the ranking process. 
