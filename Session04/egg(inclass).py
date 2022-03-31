import requests
from bs4 import BeautifulSoup
from egg import extract_info
import csv

file = open('egg.csv',mode='w', newline='')
writer = csv.writer(file)
writer.writerow("title","price","detail")

final_result =[]

for page in range(1,11):

    # 우리가 정보를 얻고 싶어하는 URL
    EGG_URL = f"https://search.shopping.naver.com/search/all?pagingIndex={page}&pagingSize=80&query=반숙란"
    # get 요청을 통해 해당 페이지 정보를 저장
    egg_html = requests.get(EGG_URL)
    # bs4 라이브러리를 통해 불러온 html을 우리가 원하는 형태로 파싱
    egg_soup = BeautifulSoup(egg_html.text,"html.parser")
    # print(egg_soup)

    egg_list_box = egg_soup.find("ul",{"class":"list_basis"})
    egg_list = egg_list_box.find_all("li",{"class":"basicList_item__2XT81"})

    final_result += extract_info(egg_list)

for result in final_result:
    row=[]
    row.append(result['title'])
    row.append(result['price'])
    row.append(result['detail'])
    writer.writerow(row)

print(final_result)

def extract_info(egg_list):
    result = []

    for egg in egg_list:
        title = egg_list[0].find("div", {"class":"basicList_title__3P9Q7"}).find("a").string

        price = egg_list[0].find("div",{'class': "basicList_price_area__1UXXR"}).find("span",{'class': "price_num__2WUXn"}).text
        detail_lists = egg_list[0].find("div",{"class":"basicList_detail_box__3ta3h"}).find_all("a")



        detail =[]
        for detail_list in detail_lists:
            detail.append(detail_list.text)

        egg_info = {
        'title': title,
        'price': price,
        'detail': detail,
        }
        result.append(egg_info)

    return result
