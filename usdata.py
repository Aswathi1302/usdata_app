import requests
import json
import sys


data=requests.get("https://datausa.io/api/data?drilldowns=Nation&measures=Population").text
data_info=json.loads(data)
print(data_info)