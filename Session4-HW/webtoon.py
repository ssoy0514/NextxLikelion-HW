def extract_info(webtoon_list):
    result=[]
    
    for webtoon in webtoon_list:
        title = webtoon.find("dl").find("a").string
        author = webtoon.find("dd",{"class":"desc"}).find("a").string
        rating = webtoon.find("div",{"class":"rating_type"}).find("strong").string

        webtoon_info = {
            'title' : title,
            'author' : author,
            'rating' : rating,
        }
        result.append(webtoon_info)
    return result