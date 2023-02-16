import json
from app import db
from app.models import curios, curioTraits

db.session.query(curios).delete()
db.session.query(curioTraits).delete()
db.session.commit()

i = 0
curioData = json.load(open('app/json/curio.json'))
for curio in curioData['curio']:
    curio = curios(name=curioData['curio'][i]['name'],image=curioData['curio'][i]['image'],codeName=curioData['curio'][i]['codeName'])
    db.session.add(curio)
    i+=1
    db.session.commit()
    
i = 0
curioTraitsData = json.load(open('app/json/curioTraits.json'))
for trait in curioTraitsData['curioTraits']:
    trait = curioTraits(type=curioTraitsData['curioTraits'][i]['type'],description=curioTraitsData['curioTraits'][i]['description'])
    db.session.add(trait)
    i+=1
    db.session.commit()
    
