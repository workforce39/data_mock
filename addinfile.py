import xml.etree.ElementTree as ET
import requests, json
context = ET.iterparse("C:\\Users\\anatol\\PycharmProjects\\exp\\hacaton_kadri\\все резюме россии.xml", events=("start", "end"))

is_first = True
k = 0
nne = 1
for event, elem in context:
    urle = f"http://31.31.203.177:9200/elem/_doc/{nne}"
    headers = config.headers
    payloadez = {}
    for l in elem:
        payloadez[l.tag] = l.text
    if payloadez != {}:
        response = requests.request("PUT", urle, headers=headers, data=json.dumps(payloadez, ensure_ascii=False).encode('utf8'))
        print("======================", json.dumps(payloadez).encode('utf8'), response.text.encode('utf8'))
        nne += 1
    if is_first:
        root = elem
        is_first = False
    if event == "end" and elem.tag == "record":
        root.clear()
    k += 1
