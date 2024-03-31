# In this project by using web scrapping i am going to scrapp all the jobs that 
#has been posted few days ago and a file will store the jobs and after a some amount
#of time the program will scrap all the recently posted jobs  

#Here with out unfamiliar skill all jobs are being scrapped and stored
#on the text file


from bs4 import BeautifulSoup
import time
import requests

print('Put some skill that u are not familiar with')

unfamiliar_skill=input('>')

print(f'Filtering out {unfamiliar_skill}')

def find_jobs():
    html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=as&searchTextText=%22Java+%2C+Python%22&txtKeywords=%22Java+%2C+Python%22&txtLocation=').text
    # print(html_text)
    soup=BeautifulSoup(html_text,'lxml')
    #To find all jobs find_all()
    jobs=soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
    # Loop through each job and print its text
    #replace(' ','') is for replacing all white spacing
    for index,job in enumerate(jobs):
        published_date=job.find('span',class_='sim-posted').span.text.replace(' ','')
        if 'few' in published_date:
            company_name=job.find('h3',class_='joblist-comp-name').text.replace(' ','')
            skills=job.find('span',class_='srp-skills').text.replace(' ','')
            # This is a link in wvet list item under header tag and h2 tag 
            # link is given for more info. Access href from a tag
            more_info=job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                with open(f'Project(Web scrapping)/{index}.txt','w') as f:
                    f.write(f'company Name: {company_name.strip()}\n')
                    f.write(f'Required Skills: {skills.strip()}\n')
                    f.write(f'More Information:{more_info}')
                print(f'File saved in: {index}.txt')

if __name__=='__main__':
    while True:
        find_jobs()
        time_wait=10
        # wait for 10 minute 600 second
        print('waiting 10 minutes.....')
        # here sleep method take time in second
        time.sleep(time_wait*60)

