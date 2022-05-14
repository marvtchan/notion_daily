import requests, json
from credentials import token, databaseID


headers = {
    "Authorization": "Bearer " + token,
    "Accept": "application/json",
    "Notion-Version": "2022-02-22"
}


url = f'https://api.notion.com/v1/databases/{databaseID}'

def readDatabase(headers, databaseID):
    
    url = f'https://api.notion.com/v1/databases/{databaseID}'

    response = requests.get(url, headers=headers)

    data = response.json()

    with open('./db.json', 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False)

    print(response.status_code)
    print(response.text)
    return

def createPage():
    pass

def updatePage():
    pass


readDatabase(headers, databaseID)