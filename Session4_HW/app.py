def extract_info(webtoonlist):

    result= []

    for webtoon in webtoonlist:
        webtoontitle = webtoon.find("dt").find("a").text
        webtoonauthor =webtoon.find("dd",{"class":"desc"}).find("a").text
        webtoonrating =webtoon.find("div",{"class":"rating_type"}).find("strong").text


        webtooninfo = {
            'webtoontitle':webtoontitle,
            'webtoonauthor': webtoonauthor,
            'webtoonrating': webtoonrating,
        }

        result.append(webtooninfo)

    return result