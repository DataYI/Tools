import json
import requests


def download_idioms_json():
    html = requests.get('https://raw.githubusercontent.com/DataYI/chinese-xinhua/master/data/idiom.json')
    with open('CaptionAssisant_2/idioms.json', 'w', encoding='utf-8') as f:
        f.write(html.text)




with open('CaptionAssisant_2/idioms.json', 'r', encoding='utf-8') as f:
    idioms = json.load(f)


def parse_dict(d):
    k = d['word']
    v = d['pinyin'].split(' ')
    return k, v


idiom_pinyin = {parse_dict(d)[0]: parse_dict(d)[1] for d in idioms}

print(idiom_pinyin)

