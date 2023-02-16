import requests
import json
import schedule
import time
from flask import request
from app import db, login_manager
from app.models import Users

auth_url = 'https://bsp-auth-prod.atoma.cloud/queue/refresh'
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'

def shopSubmit(userID):
    try:
        accountID = request.form.get("accountID")
        refreshToken = request.form.get("refreshToken")
    except:
        return False
    try:
        response = requests.get(auth_url, headers={'Authorization': 'Bearer ' + refreshToken,'user-agent': user_agent})
        auth_json = json.loads(response.content.decode())
        refreshToken = auth_json['RefreshToken']
        accessToken = auth_json['AccessToken']
        db.session.query(Users).filter(Users.id == userID).update({Users.accountID: accountID, Users.refreshToken: refreshToken, Users.accessToken: accessToken})
        db.session.commit()
        return True
    except:
        return False
        
def getDetails(userID):
    try:
        user = Users.query.filter_by(id = userID).first()
        response = requests.get('https://bsp-td-prod.atoma.cloud/web/' + user.accountID + '/summary', headers={'Authorization': 'Bearer ' + user.accessToken,'user-agent': user_agent})
        details_json = json.loads(response.content.decode())
        characters = []
        for i in details_json['characters']:
            characters.append((i['name'], i['id'], i['archetype'],i['level']))
        return characters
    except:
        return False
        
def hourlyShop(characterID, characterClass, userID):
    user = Users.query.filter_by(id = userID).first()
    try:
        response = requests.get('https://bsp-td-prod.atoma.cloud/store/storefront/credits_store_' + characterClass + '?accountId=' + user.accountID + '&personal=true&characterId=' + characterID, headers={'Authorization': 'Bearer ' + user.accessToken,'user-agent': user_agent})
        shop_json = json.loads(response.content.decode())
        data = []
        for i in shop_json['personal']:
            weaponID = i['description']['id']
            try:
                bar1 = i['description']['overrides']['base_stats'][0]['name']
                bar1Value = i['description']['overrides']['base_stats'][0]['value']
                bar2 = i['description']['overrides']['base_stats'][1]['name']
                bar2Value = i['description']['overrides']['base_stats'][1]['value']
                bar3 = i['description']['overrides']['base_stats'][2]['name']
                bar3Value = i['description']['overrides']['base_stats'][2]['value']
                bar4 = i['description']['overrides']['base_stats'][3]['name']
                bar4Value = i['description']['overrides']['base_stats'][3]['value']
                bar5 = i['description']['overrides']['base_stats'][4]['name']
                bar5Value = i['description']['overrides']['base_stats'][4]['value']
            except:
                bar1 = 'None'
                bar1Value = 'None'
                bar2 = 'None'
                bar2Value = 'None'
                bar3 = 'None'
                bar3Value = 'None'
                bar4 = 'None'
                bar4Value = 'None'
                bar5 = 'None'
                bar5Value = 'None'
            try: 
                perkID = i['description']['overrides']['perks'][0]['id']
                perkID = perkID.rsplit('/', 1)[1]
            except:
                perkID = 'None'
            try:
                traitID = i['description']['overrides']['traits'][0]['id']
                traitID = traitID.rsplit('/', 1)[1]
            except:
                traitID = 'None'
            data.append((weaponID.rsplit('/', 1)[1], 
                         i['price']['amount']['amount'], 
                         i['description']['overrides']['itemLevel'], 
                         perkID, traitID, 
                         bar1, bar1Value, 
                         bar2, bar2Value,
                         bar3, bar3Value,
                         bar4, bar4Value,
                         bar5, bar5Value,
                         i['description']['overrides']['baseItemLevel'], ))
        return data
    except:
        print('Failed to get hourly shop.')
        
# def testSchedule():
#     print('Test Schedule')
        
#     schedule.every(5).seconds.do(testSchedule)
#     while True:
#         schedule.run_pending()
#         time.sleep(1)
        