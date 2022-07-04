from webtoon import extract_info
import requests
from bs4 import BeautifulSoup
import csv

file = open('webtoon.csv', mode='w', newline='')

writer = csv.writer(file)
writer.writerow(["title","author","rating"])

final_result =[]


Webtoon_URL = f"https://comic.naver.com/webtoon/weekdayList?week=sat"
webtoon_html = requests.get(Webtoon_URL)
webtoon_soup = BeautifulSoup(webtoon_html.text,"html.parser")

weboon_list_box = webtoon_soup.find("ul",{"class":"img_list"})
webtoon_list = weboon_list_box.find_all("li") #이 코드 영상 다시 보기

print(webtoon_list)


final_result += extract_info(webtoon_list)

for result in final_result:
    row=[]
    row.append(result['title'])
    row.append(result['author'])
    row.append(result['rating'])
    writer.writerow(row) 

print(final_result)