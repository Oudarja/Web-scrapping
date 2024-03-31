from bs4 import BeautifulSoup

with open(r'F:\PROJECT\web_scraping\Webscrapping\home.html','r') as html_file:
    content=html_file.read()
    # print(content)
    #A object of Beatuifulsoup is created and 
    #stred in soup variable
    soup=BeautifulSoup(content,'lxml')

    # print(soup.prettify)
    # find method just gives the first element of h5 tag 
    # tags=soup.find('h5')
    #For find all find_all() method is used
    #find all h5 tag element
    # courses_tags=soup.find_all('h5')

    # print(tags)

    course_cards=soup.find_all('div',class_='card')
    #Print all div element with card class
    #print(course_cards)
 
    # for course in course_cards:
    #     print(course.text)

    #print only the h5 element
    # for course in course_cards:
    #     print(course.h5)

    # for course in course_cards:
    #     course_name=course.h5.text
    #     course_price=course.a.text

    #     print(course_name)
    #     print(course_price)


    for course in course_cards:
        course_name=course.h5.text
        #here split methgod is used for spliting the word from sentence 
        #and -1 index is the last element 
        course_price=course.a.text.split()[-1]

        # print(course_name)
        # print(course_price)

        print(f'{course_name} costs {course_price}')
              

    



        



