from bs4 import BeautifulSoup

import requests

html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=as&searchTextText=%22Java+%2C+Python%22&txtKeywords=%22Java+%2C+Python%22&txtLocation=').text
# print(html_text)

soup=BeautifulSoup(html_text,'lxml')
#To find all jobs find_all()

jobs=soup.find('li',class_='clearfix job-bx wht-shd-bx')

# Loop through each job and print its text
# for job in jobs:
#     print(job.text.encode('utf-8', errors='replace').decode('utf-8'))
#replace(' ','') is for replacing all white spacing
company_name=jobs.find('h3',class_='joblist-comp-name').text.replace(' ','')
#company name within it span tag
skills=jobs.find('span',class_='srp-skills').text.replace(' ','')
# Here published  date is under 2 span tag so after one span tag one more span tag sjould be 
# included
published_date=jobs.find('span',class_='sim-posted').span.text.replace(' ','')


# print(company_name)
# print(skills)


print(f'company Name:{company_name}Required Skills:{skills} Published date{published_date}')