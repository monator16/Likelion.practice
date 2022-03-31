import requests
from bs4 import BeautifulSoup

# 우리가 정보를 얻고 싶어하는 URL
EGG_URL = f"https://search.shopping.naver.com/search/all?pagingIndex=2&pagingSize=80&query=반숙란"
# get 요청을 통해 해당 페이지 정보를 저장
egg_html = requests.get(EGG_URL)
# bs4 라이브러리를 통해 불러온 html을 우리가 원하는 형태로 파싱
egg_soup = BeautifulSoup(egg_html.text,"html.parser")
print(egg_soup)
