import requests
import json 
import base64 
import pprint 
					
url = "https://restapi1.jasper.com/rws/api/v1/accounts"
TMOBILE_USERNAME = "AdiTMOUSSPTechSupport"
ROGERS_USERNAME = "AKSPAdminRogers"
TMOBILE_API_KEY = "4f61628d-012e-4536-b3d0-c136faa911fd"
ROGERS_API_KEY = "d75bbcfb-8424-4e1e-a7fa-9030aa81f259"

##what page to get accounts from
myPageNumber = 1

##store account details
tempArray = []

##total number of accounts counter
totalLen = 0

##boolean to check if have reaches last page of accounts list
isItLastPage = False

##runs until past last page
while (not isItLastPage):
    parameters= {'pageNumber': myPageNumber}
    myResponse = requests.get(url,auth=(ROGERS_USERNAME,ROGERS_API_KEY), params=parameters)
    # For successful API call, response code will be 200 (OK)
    if(myResponse.ok):
        # Loading the response data into a dict variable
        # json.loads takes in only binary or string variables so using content to fetch binary content
        # Loads (Load String) takes a Json file and converts into python data structure (dict or list, depending on JSON)
        jData = json.loads(myResponse.content)
        pp=pprint.PrettyPrinter(indent=4)
        tempAccounts = jData["accounts"]
        tempArray.append(tempAccounts)
        isItLastPage = jData["lastPage"]
        totalLen += len(tempAccounts)
        print(totalLen)
        myPageNumber += 1
        # pp.pprint(jData.count("accountId"))
    else:
        # If response code is not ok (200), print the resulting http error code with description
        print("Failure")
        myResponse.raise_for_status()