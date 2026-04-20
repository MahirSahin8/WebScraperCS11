import os
import json
import requests
from bs4 import BeautifulSoup

product_code = input("Provide product code: ")
page = 1
next = True
headers = {
    "Host": "www.ceneo.pl",
    "Cookie": "sv3=1.0_566eaee8-3cbb-11f1-b935-43a602f95b54; urdsc=1; userCeneo=ID=cf7af9ed-4a9d-4284-882d-dce9c",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0"
}

all_opinions = []
while next:
    url = f"https://www.ceneo.pl/{product_code}/opinie-{page}"
    print(url)
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        page_dom = BeautifulSoup(response.text, 'html.parser')
        product_name = page_dom.find("h1").get_text() if not None else None
        opinions = page_dom.select("div.js-product-review:not(.user-post--highlight)")
        print(len(opinions))
        for opinion in opinions:
            single_opinion = {
                'opinion_id': opinion.get("data-entry-id"),
                'author': opinion.select_one("span.user-post__author-name").get_text().strip(),
                'recommendation': opinion.select_one('span.user-post__author-recomendation > em').get_text().strip() if opinion.select_one('span.user-post__author-recomendation > em') else None,
                'score': opinion.select_one('span.user-post__score-count').get_text(),
                'content': opinion.select_one('div.user-post__text').get_text(),
                'pros': [p.get_text() for p in opinion.select('div.review-feature__item--positive')],
                'cons': [c.get_text() for c in opinion.select('div.review-feature__item--negative')],
                'helpful': opinion.select_one('button.vote-yes > span').get_text(),
                'unhelpful': opinion.select_one('button.vote-no > span').get_text(),
                'publish_date': opinion.select_one('span.user-post__published > time:nth-child(1)[datetime]').get('datetime'),
                'purchase_date': opinion.select_one('span.user-post__published > time:nth-child(2)[datetime]').get('datetime') if opinion.select_one('span.user-post__published > time:nth-child(2)') else None,
            }
            all_opinions.append(single_opinion)
    next = True if page_dom.select_one('button.pagination__next') else False
    page += 1

if not os.path.exists("./opinions"):
    os.mkdir("./opinions")
with open(f'./opinions/{product_code}.json', 'w', encoding="UTF-8") as jf:
    json.dump(all_opinions, jf, indent=4, ensure_ascii=False)