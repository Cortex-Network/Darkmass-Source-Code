import json
from app import db
from app.models import Melee, SubtypeMelee, Ranged, SubtypeRanged, OgrynTalents, PsykerTalents, VeteranTalents, ZealotTalents
from app.models import Traits, meleeActions, meleeSpecialActions, Users, rangedActions, rangedSpecialActions, RangedTraits, Classes, curios, curioTraits, Blessings, meleeBars, glossary
from app.models import rangedBars, rangedBarsDetailed, rangedActionsSimple, rangedFire, staffs, perks, baseCrit, Builds, AllTalents
db.create_all()

i = 0
traitData = json.load(open('app/json/traits.json'))
for trait in traitData['traits']:
    trait = Traits(name=traitData['traits'][i]['name'], image=traitData['traits'][i]['image'], description=traitData['traits'][i]['description'])
    blessing = Blessings(name=traitData['traits'][i]['name'], image=traitData['traits'][i]['image'], description=traitData['traits'][i]['description'])
    db.session.add(blessing)
    db.session.add(trait)
    i += 1
    
db.session.commit

i = 0
traitData = json.load(open('app/json/rangedTraits.json'))
for trait in traitData['rangedTraits']:
    trait = RangedTraits(name=traitData['rangedTraits'][i]['name'], image=traitData['rangedTraits'][i]['image'], description=traitData['rangedTraits'][i]['description'])
    blessing = Blessings(name=traitData['rangedTraits'][i]['name'], image=traitData['rangedTraits'][i]['image'], description=traitData['rangedTraits'][i]['description'])
    db.session.add(blessing)
    db.session.add(trait)
    i += 1
    
db.session.commit

i = 0
meleeActionsData = json.load(open('app/json/meleeActions.json'))
for action in meleeActionsData['actions']:
    action = meleeActions(name=meleeActionsData['actions'][i]['name'], image=meleeActionsData['actions'][i]['image'], description=meleeActionsData['actions'][i]['description'], detailedDescription=meleeActionsData['actions'][i]['detailedDescription'])
    db.session.add(action)
    i+=1

db.session.commit()

i = 0
meleeSpecialActionsData = json.load(open('app/json/meleeSpecialActions.json'))
for action in meleeSpecialActionsData['actions']:
    action = meleeSpecialActions(name=meleeSpecialActionsData['actions'][i]['name'], image=meleeSpecialActionsData['actions'][i]['image'], description=meleeSpecialActionsData['actions'][i]['description'], detailedDescription=meleeSpecialActionsData['actions'][i]['detailedDescription'], gif=meleeSpecialActionsData['actions'][i]['gif'])
    db.session.add(action)
    i+=1

db.session.commit()

i = 0
meleeData = json.load(open('app/json/melee.json'))
for melee in meleeData['melee']:
    melee = Melee(name=meleeData['melee'][i]['name'], primaryAction=meleeData['melee'][i]['primaryAction'], secondaryAction=meleeData['melee'][i]['secondaryAction'], specialAction=meleeData['melee'][i]['specialAction'], classes=meleeData['melee'][i]['classes'], traits=meleeData['melee'][i]['traits'], description=meleeData['melee'][i]['description'], tag=meleeData['melee'][i]['tag'], image=meleeData['melee'][i]['image'], bars=meleeData['melee'][i]['bars'])
    db.session.add(melee)
    i+=1

db.session.commit()

i = 0
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

i = 0
rangedData = json.load(open('app/json/ranged.json'))
for ranged in rangedData['ranged']:
    ranged = Ranged(name=rangedData['ranged'][i]['name'], primaryAction=rangedData['ranged'][i]['primaryAction'], secondaryAction=rangedData['ranged'][i]['secondaryAction'], specialAction=rangedData['ranged'][i]['specialAction'], classes=rangedData['ranged'][i]['classes'], traits=rangedData['ranged'][i]['traits'], description=rangedData['ranged'][i]['description'], tag=rangedData['ranged'][i]['tag'], image=rangedData['ranged'][i]['image'], bars=rangedData['ranged'][i]['bars'])
    db.session.add(ranged)
    i+=1

db.session.commit()

i = 0
subtypeRangedData = json.load(open('app/json/subtypeRanged.json'))
for subtypeRanged in subtypeRangedData['subtypeRanged']:
    parentCheck = Ranged.query.filter_by(name=subtypeRangedData['subtypeRanged'][i]['parentName']).first()
    parentID = parentCheck.id
    if parentID == None:
        print("Error: Parent not found")
        break
    subtypeRanged = SubtypeRanged(name=subtypeRangedData['subtypeRanged'][i]['name'], parentID=parentID, codeName=subtypeRangedData['subtypeRanged'][i]['codeName'], primaryAction=subtypeRangedData['subtypeRanged'][i]['primaryAction'], secondaryAction=subtypeRangedData['subtypeRanged'][i]['secondaryAction'], specialAction=subtypeRangedData['subtypeRanged'][i]['specialAction'], classes=subtypeRangedData['subtypeRanged'][i]['classes'], traits=subtypeRangedData['subtypeRanged'][i]['traits'], description=subtypeRangedData['subtypeRanged'][i]['description'], tag=subtypeRangedData['subtypeRanged'][i]['tag'], image=subtypeRangedData['subtypeRanged'][i]['image'])
    db.session.add(subtypeRanged)
    i+=1

db.session.commit()

i = 0
rangedActionsData = json.load(open('app/json/rangedActions.json'))
for action in rangedActionsData['rangedActions']:
    action = rangedActions(name=rangedActionsData['rangedActions'][i]['name'], image=rangedActionsData['rangedActions'][i]['image'])
    db.session.add(action)
    i+=1

db.session.commit()

i = 0
rangedSpecialActionsData = json.load(open('app/json/rangedSpecialActions.json'))
for action in rangedSpecialActionsData['rangedSpecialActions']:
    action = rangedSpecialActions(name=rangedSpecialActionsData['rangedSpecialActions'][i]['name'], image=rangedSpecialActionsData['rangedSpecialActions'][i]['image'], description=rangedSpecialActionsData['rangedSpecialActions'][i]['description'])
    db.session.add(action)
    i+=1

db.session.commit()

i = 0
classes = json.load(open('app/json/classes/classes.json'))
for group in classes['classes']:
    try:
        group = Classes(name=classes['classes'][i]['name'],
                        shortName=classes['classes'][i]['shortName'],
                        metalIcon=classes['classes'][i]['metalIcon'],
                        normalIcon=classes['classes'][i]['normalIcon'],
                        description=classes['classes'][i]['description'], 
                        health=classes['classes'][i]['health'], 
                        toughness=classes['classes'][i]['toughness'], 
                        ability=classes['classes'][i]['ability'],
                        abilityDescription=classes['classes'][i]['abilityDescription'],
                        abilityCooldown=classes['classes'][i]['abilityCooldown'],
                        abilityImage=classes['classes'][i]['abilityImg'],
                        aura=classes['classes'][i]['aura'],
                        auraDescription=classes['classes'][i]['auraDescription'],
                        auraImage=classes['classes'][i]['auraImg'],
                        blitz=classes['classes'][i]['blitz'],
                        blitzDescription=classes['classes'][i]['blitzDescription'],
                        blitzImage=classes['classes'][i]['blitzImg'],
                        iconicName1=classes['classes'][i]['iconicName1'],
                        iconicName1Description=classes['classes'][i]['iconicDescription1'],
                        iconicName1Image=classes['classes'][i]['iconicImg1'],
                        iconicName2=classes['classes'][i]['iconicName2'],
                        iconicName2Description=classes['classes'][i]['iconicDescription2'],
                        iconicName2Image=classes['classes'][i]['iconicImg2'],
                        iconicName3=classes['classes'][i]['iconicName3'],
                        iconicName3Description=classes['classes'][i]['iconicDescription3'],
                        iconicName3Image=classes['classes'][i]['iconicImg3'],
                        level5=classes['classes'][i]['level5'],
                        level10=classes['classes'][i]['level10'],
                        level15=classes['classes'][i]['level15'],
                        level20=classes['classes'][i]['level20'],
                        level25=classes['classes'][i]['level25'],
                        level30=classes['classes'][i]['level30'])
    except KeyError:
        group = Classes(name=classes['classes'][i]['name'],
                        shortName=classes['classes'][i]['shortName'], 
                description=classes['classes'][i]['description'], 
                metalIcon=classes['classes'][i]['metalIcon'],
                normalIcon=classes['classes'][i]['normalIcon'],
                health=classes['classes'][i]['health'], 
                toughness=classes['classes'][i]['toughness'], 
                ability=classes['classes'][i]['ability'],
                abilityDescription=classes['classes'][i]['abilityDescription'],
                abilityCooldown=classes['classes'][i]['abilityCooldown'],
                abilityImage=classes['classes'][i]['abilityImg'],
                aura=classes['classes'][i]['aura'],
                auraDescription=classes['classes'][i]['auraDescription'],
                auraImage=classes['classes'][i]['auraImg'],
                blitz=classes['classes'][i]['blitz'],
                blitzDescription=classes['classes'][i]['blitzDescription'],
                blitzImage=classes['classes'][i]['blitzImg'],
                iconicName1=classes['classes'][i]['iconicName1'],
                iconicName1Description=classes['classes'][i]['iconicDescription1'],
                iconicName1Image=classes['classes'][i]['iconicImg1'],
                iconicName2=classes['classes'][i]['iconicName2'],
                iconicName2Description=classes['classes'][i]['iconicDescription2'],
                iconicName2Image=classes['classes'][i]['iconicImg2'],
                level5=classes['classes'][i]['level5'],
                level10=classes['classes'][i]['level10'],
                level15=classes['classes'][i]['level15'],
                level20=classes['classes'][i]['level20'],
                level25=classes['classes'][i]['level25'],
                level30=classes['classes'][i]['level30'])
    db.session.add(group)
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
veteranTalents = json.load(open('app/json/classes/veteranTalents.json'))
for talent in veteranTalents['veteranTalents']:
    talent = VeteranTalents(name=veteranTalents['veteranTalents'][i]['name'],description=veteranTalents['veteranTalents'][i]['description'],image=veteranTalents['veteranTalents'][i]['image'])
    allTalents = AllTalents(name=veteranTalents['veteranTalents'][i]['name'],description=veteranTalents['veteranTalents'][i]['description'],image=veteranTalents['veteranTalents'][i]['image'])
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

i=0
meleeBarData = json.load(open('app/json/stats/meleeBars.json'))
for bar in meleeBarData['meleeBars']:
    bar = meleeBars(name=meleeBarData['meleeBars'][i]['name'],image=meleeBarData['meleeBars'][i]['image'],description=meleeBarData['meleeBars'][i]['description'],modifiers=meleeBarData['meleeBars'][i]['modifiers'])
    db.session.add(bar)
    i+=1
    
db.session.commit()

i=0
rangedBarData = json.load(open('app/json/stats/rangedBars.json'))
for bar in rangedBarData['rangedBars']:
    bar = rangedBars(name=rangedBarData['rangedBars'][i]['name'],image=rangedBarData['rangedBars'][i]['image'],description=rangedBarData['rangedBars'][i]['description'],modifiers=rangedBarData['rangedBars'][i]['modifiers'])
    db.session.add(bar)
    i+=1
    
db.session.commit()

i=0
rangedBarDetailedData = json.load(open('app/json/stats/rangedBarsDetailed.json'))
for bar in rangedBarDetailedData['rangedBarsDetailed']:
    bar = rangedBarsDetailed(weapon=rangedBarDetailedData['rangedBarsDetailed'][i]['weapon'],
                             image=rangedBarDetailedData['rangedBarsDetailed'][i]['image'],
                             bar1=rangedBarDetailedData['rangedBarsDetailed'][i]['bar1'],
                             bar1Modifiers=rangedBarDetailedData['rangedBarsDetailed'][i]['bar1Modifiers'],
                             bar2=rangedBarDetailedData['rangedBarsDetailed'][i]['bar2'],
                             bar2Modifiers=rangedBarDetailedData['rangedBarsDetailed'][i]['bar2Modifiers'],
                             bar3=rangedBarDetailedData['rangedBarsDetailed'][i]['bar3'],
                             bar3Modifiers=rangedBarDetailedData['rangedBarsDetailed'][i]['bar3Modifiers'],
                             bar4=rangedBarDetailedData['rangedBarsDetailed'][i]['bar4'],
                             bar4Modifiers=rangedBarDetailedData['rangedBarsDetailed'][i]['bar4Modifiers'],
                             bar5=rangedBarDetailedData['rangedBarsDetailed'][i]['bar5'],
                             bar5Modifiers=rangedBarDetailedData['rangedBarsDetailed'][i]['bar5Modifiers'])
    db.session.add(bar)
    i+=1
    
db.session.commit()
    
i=0
rangedActionsSimpleData = json.load(open('app/json/stats/rangedActionsSimple.json'))
for action in rangedActionsSimpleData['rangedActionsSimple']:
    action = rangedActionsSimple(name=rangedActionsSimpleData['rangedActionsSimple'][i]['name'],image=rangedActionsSimpleData['rangedActionsSimple'][i]['image'],description=rangedActionsSimpleData['rangedActionsSimple'][i]['description'],detailedDescription=rangedActionsSimpleData['rangedActionsSimple'][i]['detailedDescription'])
    db.session.add(action)
    i+=1
    
db.session.commit()

i=0
rangedFireData = json.load(open('app/json/stats/rangedFire.json'))
for fm in rangedFireData['rangedFire']:
    fm = rangedFire(firemode=rangedFireData['rangedFire'][i]['firemode'],fmImg=rangedFireData['rangedFire'][i]['fmImg'],fmDesc=rangedFireData['rangedFire'][i]['fmDesc'])
    db.session.add(fm)
    i+=1
    
db.session.commit()

i=0
staffData = json.load(open('app/json/stats/staffs.json'))
for staff in staffData['staffs']:
    staff = staffs(name=staffData['staffs'][i]['name'],primaryAction=staffData['staffs'][i]['primaryAction'],secondaryAction=staffData['staffs'][i]['secondaryAction'],specialAction=staffData['staffs'][i]['specialAction'])
    db.session.add(staff)
    i+=1
    
db.session.commit()

i=0
perksData = json.load(open('app/json/perks.json'))
for perk in perksData['perks']:
    perk = perks(description=perksData['perks'][i]['description'])
    db.session.add(perk)
    i+=1
    
db.session.commit()


i=0
glossaryData = json.load(open('app/json/glossary.json'))
for keyword in glossaryData['glossary']:
    keyword = glossary(name=glossaryData['glossary'][i]['name'],description=glossaryData['glossary'][i]['description'])
    db.session.add(keyword)
    i+=1
    
db.session.commit()

i=0
baseCritData = json.load(open('app/json/baseCrit.json'))
for baseCritical in baseCritData['baseCrit']:
    baseCritical = baseCrit(name=baseCritData['baseCrit'][i]['name'],crit=baseCritData['baseCrit'][i]['crit'])
    db.session.add(baseCritical)
    i+=1
    
db.session.commit()
    


