
import requests

import datetime


def main():
    url = 'https://hooks.slack.com/services/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'
    text = '테스트 메세지: ' + str(datetime.datetime.now())
    payload = {
        'text': text
    }
    requests.post(url, json=payload)


if __name__ == '__main__':
    main()
