import json
from app import db
from app.models import Ranged, SubtypeRanged

db.session.query(Ranged).delete()
db.session.query(SubtypeRanged).delete()
db.session.commit()

i = 0
rangedData = json.load(open('app/json/ranged.json'))
for ranged in rangedData['ranged']:
    ranged = Ranged(name=rangedData['ranged'][i]['name'], primaryAction=rangedData['ranged'][i]['primaryAction'], secondaryAction=rangedData['ranged'][i]['secondaryAction'], specialAction=rangedData['ranged'][i]['specialAction'], classes=rangedData['ranged'][i]['classes'], traits=rangedData['ranged'][i]['traits'], description=rangedData['ranged'][i]['description'], tag=rangedData['ranged'][i]['tag'], image=rangedData['ranged'][i]['image'], bars=rangedData['ranged'][i]['bars'])
    db.session.add(ranged)
    i+=1
    db.session.commit()
    
i=0
subtypeRangedData = json.load(open('app/json/subtypeRanged.json'))
for subtypeRanged in subtypeRangedData['subtypeRanged']:
    parentCheck = Ranged.query.filter_by(name=subtypeRangedData['subtypeRanged'][i]['parentName']).first()
    try:
        parentID = parentCheck.id
        if parentID == None:
            print("Error: Parent not found - Parent Name: " + subtypeRangedData['subtypeRanged'][i]['parentName'])
            break
    except Exception as e:
        print("Error: Parent not found - Parent Name: " + subtypeRangedData['subtypeRanged'][i]['parentName'])
        break
    subtypeRanged = SubtypeRanged(name=subtypeRangedData['subtypeRanged'][i]['name'], parentID=parentID, codeName=subtypeRangedData['subtypeRanged'][i]['codeName'], primaryAction=subtypeRangedData['subtypeRanged'][i]['primaryAction'], secondaryAction=subtypeRangedData['subtypeRanged'][i]['secondaryAction'], specialAction=subtypeRangedData['subtypeRanged'][i]['specialAction'], classes=subtypeRangedData['subtypeRanged'][i]['classes'], traits=subtypeRangedData['subtypeRanged'][i]['traits'], description=subtypeRangedData['subtypeRanged'][i]['description'], tag=subtypeRangedData['subtypeRanged'][i]['tag'], image=subtypeRangedData['subtypeRanged'][i]['image'])
    db.session.add(subtypeRanged)
    i+=1
    db.session.commit()