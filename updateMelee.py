import json
from app import db
from app.models import Melee, SubtypeMelee

db.session.query(Melee).delete()
db.session.query(SubtypeMelee).delete()
db.session.commit()

i = 0
meleeData = json.load(open('app/json/melee.json'))
for melee in meleeData['melee']:
    melee = Melee(name=meleeData['melee'][i]['name'], primaryAction=meleeData['melee'][i]['primaryAction'], secondaryAction=meleeData['melee'][i]['secondaryAction'], specialAction=meleeData['melee'][i]['specialAction'], classes=meleeData['melee'][i]['classes'], traits=meleeData['melee'][i]['traits'], description=meleeData['melee'][i]['description'], tag=meleeData['melee'][i]['tag'], image=meleeData['melee'][i]['image'], bars=meleeData['melee'][i]['bars'])
    db.session.add(melee)
    i+=1
    db.session.commit()

i=0
subtypeMeleeData = json.load(open('app/json/subtypeMelee.json'))
for subtypeMelee in subtypeMeleeData['subtypeMelee']:
    parentCheck = Melee.query.filter_by(name=subtypeMeleeData['subtypeMelee'][i]['parentName']).first()
    try:
        parentID = parentCheck.id
        if parentID == None:
            print("Error: Parent not found - Parent Name: " + subtypeMeleeData['subtypeMelee'][i]['parentName'])
            break
    except Exception as e:
        print("Error: Parent not found - Parent Name: " + subtypeMeleeData['subtypeMelee'][i]['parentName'])
        break
    subtypeMelee = SubtypeMelee(name=subtypeMeleeData['subtypeMelee'][i]['name'], parentID=parentID, codeName=subtypeMeleeData['subtypeMelee'][i]['codeName'], primaryAction=subtypeMeleeData['subtypeMelee'][i]['primaryAction'], secondaryAction=subtypeMeleeData['subtypeMelee'][i]['secondaryAction'], specialAction=subtypeMeleeData['subtypeMelee'][i]['specialAction'], classes=subtypeMeleeData['subtypeMelee'][i]['classes'], traits=subtypeMeleeData['subtypeMelee'][i]['traits'], description=subtypeMeleeData['subtypeMelee'][i]['description'], tag=subtypeMeleeData['subtypeMelee'][i]['tag'], image=subtypeMeleeData['subtypeMelee'][i]['image'], lightCombo=subtypeMeleeData['subtypeMelee'][i]['lightCombo'], heavyCombo=subtypeMeleeData['subtypeMelee'][i]['heavyCombo'])
    db.session.add(subtypeMelee)
    i+=1
    db.session.commit()