import requests
import json
import re
import csv


def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Host': 'ru.dotabuff.com',
        'Accept-Language': 'en-US, en; q=0.7, ru; q=0.3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept': '*/*',
        'Cookie': '_hi=1556208674718; _tz=Asia%2FJakarta; _pubcid=751cccac-fed7-4c2f-8d96-f0c390338904; _ga=GA1.2.1341361322.1556208675; _gid=GA1.2.1111864365.1556208675; _gat=1; __qca=P0-859503112-1556208675717; _ym_uid=1556208676843955989; _ym_d=1556208676; _ym_isad=2; _ym_visorc_52686388=w; __gads=ID=69105635be21983a:T=1556208678:S=ALNI_MbbpRlwh4J_eSzHmR3n770-CsghJA'
    }
    response = requests.get(url, headers=headers)
    return response.text


def get_all_heroes():
    response = requests.get("https://api.opendota.com/api/heroes")
    heroes = json.loads(response.text)
    for hero in heroes:
        hero["localized_name"] = hero["localized_name"].lower().replace(" ", "-")
    return heroes


def parse_hero(heroes, patch):
    for hero in heroes:
        html = get_html("https://ru.dotabuff.com/heroes/" + hero["localized_name"] + "/counters?date=" + patch)
        print(html)
        pattern = r'<a class="link-type-hero" href="\/heroes\/' + re.escape(hero["localized_name"]) +\
                  r'">.*?<\/a><\/td><td data-value="(.*?)">'
        print(pattern)
        rating = re.findall(pattern, html, re.M)
        print(rating)


heroes = get_all_heroes()
patch = "patch_7.21"
parse_hero(heroes, patch)
