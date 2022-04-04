import requests

def checkMission(text,team,mission):
    API_URL=f'http://honored-thunder-ketch.glitch.me/test?text={text}&team={team}&mission={mission}'
    httpHeaders = {}
    body = {}
    data=requests.post(url=API_URL, json=body, headers=httpHeaders)
    return data.text
