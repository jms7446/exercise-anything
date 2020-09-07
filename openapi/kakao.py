import json

import requests


def main():
    url = 'https://dapi.kakao.com/v3/search/book'
    querystring = {'query': '윤웅식'}
    header = {'authorization': 'KakaoAK 00a31bd929735053728eeb0fa8851b5a'}
    r = requests.get(url, headers=header, params=querystring)

    for d in (json.loads(r.text)['documents']):
        print(d)


if __name__ == '__main__':
    main()
