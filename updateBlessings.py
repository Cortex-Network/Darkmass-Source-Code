import json
from app import db
from app.models import Traits, RangedTraits, Blessings, rangedActions

db.session.query(Blessings).delete()
db.session.query(Traits).delete()
db.session.query(RangedTraits).delete()
db.session.commit()

i = 0
traitData = json.load(open('app/json/traits.json'))
for trait in traitData['traits']:
    trait = Traits(name=traitData['traits'][i]['name'], image=traitData['traits'][i]['image'], description=traitData['traits'][i]['description'])
    blessing = Blessings(name=traitData['traits'][i]['name'], image=traitData['traits'][i]['image'], description=traitData['traits'][i]['description'])
    db.session.add(blessing)
    db.session.add(trait)
    i += 1
    db.session.commit()
    
i = 0
traitData = json.load(open('app/json/rangedTraits.json'))
for trait in traitData['rangedTraits']:
    trait = RangedTraits(name=traitData['rangedTraits'][i]['name'], image=traitData['rangedTraits'][i]['image'], description=traitData['rangedTraits'][i]['description'])
    blessing = Blessings(name=traitData['rangedTraits'][i]['name'], image=traitData['rangedTraits'][i]['image'], description=traitData['rangedTraits'][i]['description'])
    db.session.add(blessing)
    db.session.add(trait)
    i += 1
    db.session.commit()

