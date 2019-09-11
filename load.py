from bs4 import BeautifulSoup
import requests 
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# url = input('Enter Youtube Video Url- ')
# filename = input('Enter filename- ')

source = requests.get('https://www.youtube.com/user/aajtaktv/videos').text
soup = BeautifulSoup(source, 'lxml')

csv_file = open('%s.csv' %('shubh'),'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Title', 'Views', 'Description'])

for content in soup.find_all('div', class_= "yt-lockup-content"):
    try:
        title = content.h3.a.text
        print(title)

        x = content.find('ul', class_="yt-lockup-meta-info").text
        views = x.split("views",1)
        print(views[0])

        description = content.find('div', class_="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2").text
        print(description)

    except Exception as e:
        description = None

    print('\n')
    csv_writer.writerow([title, views[0], description])

csv_file.close()