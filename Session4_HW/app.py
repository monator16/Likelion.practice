import requests
from bs4 import BeautifulSoup

WEBTOON_URL = f'https://comic.naver.com/webtoon/weekdayList?week=sat'

webtoon_html = requests.get(WEBTOON_URL)
webtoon_soup = BeautifulSoup(webtoon_html.text, "html parser")

webtoonbox = webtoon_soup.find("ul",{"class":"img_list"})
webtoonlist= webtoonbox.find_all("li")
result= []

for webtoon in webtoonlist:
    webtoontitle = webtoon.find("dl").find("dt").find("a").string
    webtoonauthor =webtoon.find("dl").find("dd",{"class":"desc"}).string
    webtoonrating =webtoon.find("dl").find("dd",{"class":"rating_type"}).find("strong").string


webtooninfo = {
    'webtoontitle':webtoontitle,
    'webtoonauthor': webtoonauthor,
    'webtoonrating': webtoonrating,
}

result.append(webtooninfo)
print(result)