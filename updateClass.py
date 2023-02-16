import json
from app import db
from app.models import PsykerTalents, AllTalents, ZealotTalents, VeteranTalents, OgrynTalents

db.session.query(PsykerTalents).delete()
db.session.query(ZealotTalents).delete()
db.session.query(VeteranTalents).delete()
db.session.query(OgrynTalents).delete()
db.session.query(AllTalents).delete()
db.session.commit()

i = 0
psykerTalents = json.load(open('app/json/classes/psykerTalents.json'))
for talent in psykerTalents['psykerTalents']:
    talent = PsykerTalents(name=psykerTalents['psykerTalents'][i]['name'],description=psykerTalents['psykerTalents'][i]['description'],image=psykerTalents['psykerTalents'][i]['image'])
    allTalents = AllTalents(name=psykerTalents['psykerTalents'][i]['name'],description=psykerTalents['psykerTalents'][i]['description'],image=psykerTalents['psykerTalents'][i]['image'])
    db.session.add(allTalents)
    db.session.add(talent)
    i+=1
    db.session.commit()
    
i = 0
zealotTalents = json.load(open('app/json/classes/zealotTalents.json'))
for talent in zealotTalents['zealotTalents']:
    talent = ZealotTalents(name=zealotTalents['zealotTalents'][i]['name'],description=zealotTalents['zealotTalents'][i]['description'],image=zealotTalents['zealotTalents'][i]['image'])
    allTalents = AllTalents(name=zealotTalents['zealotTalents'][i]['name'],description=zealotTalents['zealotTalents'][i]['description'],image=zealotTalents['zealotTalents'][i]['image'])
    db.session.add(allTalents)
    db.session.add(talent)
    i+=1
    db.session.commit()

i = 0
veteranTalents = json.load(open('app/json/classes/veteranTalents.json'))
for talent in veteranTalents['veteranTalents']:
    talent = VeteranTalents(name=veteranTalents['veteranTalents'][i]['name'],description=veteranTalents['veteranTalents'][i]['description'],image=veteranTalents['veteranTalents'][i]['image'])
    allTalents = AllTalents(name=veteranTalents['veteranTalents'][i]['name'],description=veteranTalents['veteranTalents'][i]['description'],image=veteranTalents['veteranTalents'][i]['image'])
    db.session.add(allTalents)
    db.session.add(talent)
    i+=1
    db.session.commit()
    
i = 0
ogrynTalents = json.load(open('app/json/classes/ogrynTalents.json'))
for talent in ogrynTalents['ogrynTalents']:
    talent = OgrynTalents(name=ogrynTalents['ogrynTalents'][i]['name'],description=ogrynTalents['ogrynTalents'][i]['description'],image=ogrynTalents['ogrynTalents'][i]['image'])
    allTalents = AllTalents(name=ogrynTalents['ogrynTalents'][i]['name'],description=ogrynTalents['ogrynTalents'][i]['description'],image=ogrynTalents['ogrynTalents'][i]['image'])
    db.session.add(allTalents)
    db.session.add(talent)
    i+=1
    db.session.commit()