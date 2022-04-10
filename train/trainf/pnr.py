
import requests
from django.http import HttpResponse
import json
import pandas as pd


def apiCall(pnr):
    url = "https://indianrailways.p.rapidapi.com/index.php"
    querystring = {"pnr": f"{pnr}"}
    headers = {
        'x-rapidapi-host': "indianrailways.p.rapidapi.com",
        'x-rapidapi-key': "cf23647522mshd5acd9e46e038c6p10558bjsn5820f55667fb"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    txt = response.text
    json_object = json.loads(txt)

    df = pd.json_normalize(json_object)
    return df
        

def pnrSearch(pnr):
    # pnr = int(pnr)
    # if pnr <= 7 and pnr >= 4:
    #     pass
    # elif pnr > 7 and pnr <= 10:
    #     pass
    # else:
    #     pass
    
    return pnr
