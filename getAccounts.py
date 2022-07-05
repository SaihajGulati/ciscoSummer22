import requests
import json 
import base64 
import pprint 
					
url = "https://restapi20.jasper.com/rws/api/v1/accounts"
USERNAME = "AdiTMOUSSPTechSupport"
API_KEY = "4f61628d-012e-4536-b3d0-c136faa911fd"
myResponse = requests.get(url,auth=(USERNAME,API_KEY))
# For successful API call, response code will be 200 (OK)
if(myResponse.ok):
    # Loading the response data into a dict variable
    # json.loads takes in only binary or string variables so using content to fetch binary content
    # Loads (Load String) takes a Json file and converts into python data structure (dict or list, depending on JSON)
    jData = json.loads(myResponse.content)
    pp=pprint.PrettyPrinter(indent=4)
    pp.pprint(jData)
else:
    # If response code is not ok (200), print the resulting http error code with description
    print("Failure")
    myResponse.raise_for_status()