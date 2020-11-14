import requests, json, config
from random import randrange
from random import normalvariate

if config.load_people:
    for i in range(config.start_people, config.start_people+ config.count_people, 1):
        url = f"http://31.31.203.177:9200/{config.index_people}/_doc/{i}"
        payload = f'{{' \
                  f'"fio": "Иванов{i}", ' \
                  f'"age": "{int((normalvariate(1, 1)+3)*10)}", ' \
                  f'"citizenship": "{config.citizenship[randrange(0, len(config.citizenship), 1)]}", '\
                  f'"profession": "{config.profession[randrange(0, len(config.profession), 1)]}", ' \
                  f'"education": "{config.education[randrange(0, len(config.education), 1)]}", ' \
                  f'"floor": "{config.floor[randrange(0, len(config.floor), 1)]}", ' \
                  f'"org": "{config.org[randrange(0, len(config.org), 1)]}{randrange(0, 8, 1)}"' \
                  f'}}'
        response = requests.request("PUT", url, headers=config.headers, data=payload.encode('utf-8'))
        print(i, response.text.encode('utf8'), payload)

if config.load_org:
    for i in range(config.start_org, config.start_org + config.count_org, 1):
        url = f"http://31.31.203.177:9200/{config.index_org}/_doc/{i}"
        payload = f'{{' \
                  f'"name": "{config.org[randrange(0, len(config.org), 1)]}{randrange(0, 8, 1)}", ' \
                  f'"okved": "{randrange(1, 22, 1)}", ' \
                  f'"employees": {randrange(1, 30, 1)}' \
                  f'}}'
        response = requests.request("PUT", url, headers=config.headers, data=payload.encode('utf-8'))
        print(i, response.text.encode('utf8'), payload)