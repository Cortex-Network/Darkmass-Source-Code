from app import db
from app.models import Builds, curioTraits, perks 
from flask import request
import secrets

def validateBuild(classSelected, userID):
    buildName = request.form.get('build-name')
    visibility =  request.form.get('visibilitySelected')
    meleeWeapon = request.form.get('weaponSelected')
    userID = userID
    classSelected = classSelected
    
    meleeWeaponPerkOne = request.form.get('meleePerkOneSelected')
    meleeWeaponPerkOneCheck = perks.query.filter_by(description=meleeWeaponPerkOne).first()
    meleeWeaponPerkOne = meleeWeaponPerkOneCheck.id
    
    meleeWeaponPerkTwo = request.form.get('meleePerkTwoSelected')
    meleeWeaponPerkTwoCheck = perks.query.filter_by(description=meleeWeaponPerkTwo).first()
    meleeWeaponPerkTwo = meleeWeaponPerkTwoCheck.id
    
    meleeWeaponBlessingOne = request.form.get('meleeBlessingOneSelected')
    meleeWeaponBlessingTwo = request.form.get('meleeBlessingTwoSelected')
    
    rangedWeapon = request.form.get('rangedSelected')
    
    rangedWeaponPerkOne = request.form.get('rangedPerkOneSelected')
    rangedWeaponPerkOneCheck = perks.query.filter_by(description=rangedWeaponPerkOne).first()
    rangedWeaponPerkOne = rangedWeaponPerkOneCheck.id
    
    rangedWeaponPerkTwo = request.form.get('rangedPerkTwoSelected')
    rangedWeaponPerkTwoCheck = perks.query.filter_by(description=rangedWeaponPerkTwo).first()
    rangedWeaponPerkTwo = rangedWeaponPerkTwoCheck.id
    
    rangedWeaponBlessingOne = request.form.get('rangedBlessingOneSelected')
    rangedWeaponBlessingTwo = request.form.get('rangedBlessingTwoSelected')
    curioNameOne = request.form.get('curioOneSelected')
    
    curioBlessingOne = request.form.get('curioOneBlessingSelected')
    curioBlessingOneCheck = curioTraits.query.filter_by(description=curioBlessingOne).first()
    curioBlessingOne = curioBlessingOneCheck.id
    
    curioPerkOneOne = request.form.get('curioOnePerkOneSelected')
    curioPerkOneOneCheck = curioTraits.query.filter_by(description=curioPerkOneOne).first()
    curioPerkOneOne = curioPerkOneOneCheck.id
    
    curioPerkOneTwo = request.form.get('curioOnePerkTwoSelected')
    curioPerkOneTwoCheck = curioTraits.query.filter_by(description=curioPerkOneTwo).first()
    curioPerkOneTwo = curioPerkOneTwoCheck.id
    
    curioPerkOneThree = request.form.get('curioOnePerkThreeSelected')
    curioPerkOneThreeCheck = curioTraits.query.filter_by(description=curioPerkOneThree).first()
    curioPerkOneThree = curioPerkOneThreeCheck.id
    
    curioNameTwo = request.form.get('curioTwoSelected')
    
    curioBlessingTwo = request.form.get('curioTwoBlessingSelected')
    curioBlessingTwoCheck = curioTraits.query.filter_by(description=curioBlessingTwo).first()
    curioBlessingTwo = curioBlessingTwoCheck.id
    
    curioPerkTwoOne = request.form.get('curioTwoPerkOneSelected')
    curioPerkTwoOneCheck = curioTraits.query.filter_by(description=curioPerkTwoOne).first()
    curioPerkTwoOne = curioPerkTwoOneCheck.id
    
    curioPerkTwoTwo = request.form.get('curioTwoPerkTwoSelected')
    curioPerkTwoTwoCheck = curioTraits.query.filter_by(description=curioPerkTwoTwo).first()
    curioPerkTwoTwo = curioPerkTwoTwoCheck.id
    
    curioPerkTwoThree = request.form.get('curioTwoPerkThreeSelected')
    curioPerkTwoThreeCheck = curioTraits.query.filter_by(description=curioPerkTwoThree).first()
    curioPerkTwoThree = curioPerkTwoThreeCheck.id
    
    curioNameThree =  request.form.get('curioThreeSelected')
    
    curioBlessingThree = request.form.get('curioThreeBlessingSelected')
    curioBlessingThreeCheck = curioTraits.query.filter_by(description=curioBlessingThree).first()
    curioBlessingThree = curioBlessingThreeCheck.id
    
    curioPerkThreeOne = request.form.get('curioThreePerkOneSelected')
    curioPerkThreeOneCheck = curioTraits.query.filter_by(description=curioPerkThreeOne).first()
    curioPerkThreeOne = curioPerkThreeOneCheck.id
    
    curioPerkThreeTwo = request.form.get('curioThreePerkTwoSelected')
    curioPerkThreeTwoCheck = curioTraits.query.filter_by(description=curioPerkThreeTwo).first()
    curioPerkThreeTwo = curioPerkThreeTwoCheck.id
    
    curioPerkThreeThree = request.form.get('curioThreePerkThreeSelected')
    curioPerkThreeThreeCheck = curioTraits.query.filter_by(description=curioPerkThreeThree).first()
    curioPerkThreeThree = curioPerkThreeThreeCheck.id
    
    description = request.form.get('quillEditor')
    level5Talent = request.form.get('level5Selected')
    level10Talent = request.form.get('level10Selected')
    level15Talent = request.form.get('level15Selected')
    level20Talent = request.form.get('level20Selected')
    level25Talent = request.form.get('level25Selected')
    level30Talent = request.form.get('level30Selected')
    urlHASH = secrets.token_urlsafe(32)
    
    build = Builds(buildName=buildName,
                   UserID=userID,
                   visibility=visibility,
                   meleeWeapon=meleeWeapon,
                   selectedClass=classSelected,
                   meleeWeaponPerkOne=meleeWeaponPerkOne, 
                   meleeWeaponPerkTwo=meleeWeaponPerkTwo,
                   meleeWeaponBlessingOne=meleeWeaponBlessingOne,
                   meleeWeaponBlessingTwo=meleeWeaponBlessingTwo,
                   rangedWeapon=rangedWeapon, 
                   rangedWeaponPerkOne=rangedWeaponPerkOne,
                   rangedWeaponPerkTwo=rangedWeaponPerkTwo,
                   rangedWeaponBlessingOne=rangedWeaponBlessingOne,
                   rangedWeaponBlessingTwo=rangedWeaponBlessingTwo,
                   curioNameOne=curioNameOne, 
                   curioBlessingOne=curioBlessingOne,
                   curioPerkOneOne=curioPerkOneOne, 
                   curioPerkOneTwo=curioPerkOneTwo, 
                   curioPerkOneThree=curioPerkOneThree,
                   curioNameTwo=curioNameTwo, 
                   curioBlessingTwo=curioBlessingTwo, 
                   curioPerkTwoOne=curioPerkTwoOne,
                   curioPerkTwoTwo=curioPerkTwoTwo, 
                   curioPerkTwoThree=curioPerkTwoThree,
                   curioNameThree=curioNameThree,
                   curioBlessingThree=curioBlessingThree,
                   curioPerkThreeOne=curioPerkThreeOne, 
                   curioPerkThreeTwo=curioPerkThreeTwo,
                   curioPerkThreeThree=curioPerkThreeThree, 
                   description=description, 
                   level5Talent=level5Talent,
                   level10Talent=level10Talent,
                   level15Talent=level15Talent, 
                   level20Talent=level20Talent,
                   level25Talent=level25Talent,
                   level30Talent=level30Talent,
                   urlHASH=urlHASH)
    db.session.add(build)
    db.session.commit()