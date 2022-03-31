import requests
from bs4 import BeautifulSoup
from app import extract_info
import csv

file = open('app.csv', mode='w', newline ='')
writer = csv.writer(file)
writer.writerow(["webtoontitle","webtoonauthor","webtoonrating"])

WEBTOON_URL = f'https://comic.naver.com/webtoon/weekdayList?week=sat'
webtoon_html = requests.get(WEBTOON_URL)
webtoon_soup = BeautifulSoup(webtoon_html.text, "html.parser")

webtoonbox = webtoon_soup.find("ul",{"class":"img_list"})
webtoonlist= webtoonbox.find_all("li")

final_result = []
final_result += extract_info(webtoonlist)

for result in final_result:
    row=[]
    row.append(result["webtoontitle"])
    row.append(result["webtoonauthor"])
    row.append(result["webtoonrating"])
    writer.writerow(row)

print(final_result)