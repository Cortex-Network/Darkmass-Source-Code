import pathlib
import os
from flask import render_template, url_for, request, redirect, send_from_directory, flash
from flask_login import logout_user, login_required, current_user
from sqlalchemy import delete
import app.scripts.buildEditor as be
import app.scripts.editBuild as eb
import app.scripts.shop as sc
from app import app, db
from app.models import Melee, SubtypeMelee, Ranged, SubtypeRanged, Traits, meleeActions, meleeSpecialActions, rangedActions
from app.models import curios, curioTraits, Blessings, meleeBars, glossary, baseCrit, perks, rangedActionsSimple, rangedBars, rangedBarsDetailed, rangedFire, staffs
from app.models import rangedSpecialActions, RangedTraits, Classes, OgrynTalents, PsykerTalents, VeteranTalents, ZealotTalents, Users, Builds, AllTalents



@app.context_processor
def utility_processor():
    def get_stem(image_path):
        return pathlib.Path(image_path).name
    return dict(get_stem=get_stem)

@app.route('/')
def home():
    title = "Home ~ Darkmass"
    return render_template('home.html', title=title)

@app.route('/shopchecker')
@login_required
def shopChecker():
    title = "Shop Checker ~ Darkmass"
    userList  = Users.query.all()
    SubtypeMeleeList = SubtypeMelee.query.all()
    SubtypeRangedList = SubtypeRanged.query.all()
    curioList = curios.query.all()
    userID = current_user.id
    user = Users.query.filter_by(id = userID).first()
    if user.accountID == None or user.refreshToken == None:
        return render_template('shopChecker.html', title=title, userList=userList, userID=userID)
    else:
        getDetails = sc.getDetails(userID)
        if getDetails == False:
            flash("Issue with getting player characters, please try again later or contact an admin on discord!", "danger")
            return redirect(url_for('home'))
        else:
            j = len(getDetails)
            k = 1
            while k <= j:
                for i in getDetails:
                    if k == 1:
                        character1 = sc.hourlyShop(i[1], i[2], userID)
                        k += 1
                    elif k == 2:
                        character2 = sc.hourlyShop(i[1], i[2], userID)
                        k += 1
                    elif k == 3:
                        character3 = sc.hourlyShop(i[1], i[2], userID)
                        k += 1
                    elif k == 4:
                        character4 = sc.hourlyShop(i[1], i[2], userID)
                        k += 1
                    elif k == 5:
                        character5 = sc.hourlyShop(i[1], i[2], userID)
                        k += 1
                    else:
                        flash("Issue with getting player characters, please try again later or contact an admin on discord!", "danger")
                        return redirect(url_for('home'))
            if j == 1:
                character2 = None
                character3 = None
                character4 = None
                character5 = None
                return render_template('shopChecker.html', title="Shop Checker Results", 
                                        getDetails=getDetails,
                                        character1=character1, 
                                        character2=character2,
                                        character3=character3,
                                        character4=character4,
                                        character5=character5,
                                        userList=userList, 
                                        userID=userID,
                                        SubtypeMeleeList=SubtypeMeleeList,
                                        SubtypeRangedList=SubtypeRangedList,
                                        curioList=curioList)
            elif j == 2:
                character3 = None
                character4 = None
                character5 = None
                return render_template('shopChecker.html', title="Shop Checker Results", 
                                        getDetails=getDetails,
                                        character1=character1, 
                                        character2=character2,
                                        character3=character3,
                                        character4=character4,
                                        character5=character5,
                                        userList=userList, 
                                        userID=userID,
                                        SubtypeMeleeList=SubtypeMeleeList,
                                        SubtypeRangedList=SubtypeRangedList,
                                        curioList=curioList)
            elif j == 3:
                character4 = None
                character5 = None
                return render_template('shopChecker.html', title="Shop Checker Results", 
                                        getDetails=getDetails,
                                        character1=character1, 
                                        character2=character2,
                                        character3=character3,
                                        character4=character4,
                                        character5=character5,
                                        userList=userList, 
                                        userID=userID,
                                        SubtypeMeleeList=SubtypeMeleeList,
                                        SubtypeRangedList=SubtypeRangedList,
                                        curioList=curioList)
            elif j == 4:
                character5 = None
                return render_template('shopChecker.html', title="Shop Checker Results", 
                                        getDetails=getDetails,
                                        character1=character1, 
                                        character2=character2,
                                        character3=character3,
                                        character4=character4,
                                        character5=character5,
                                        userList=userList, 
                                        userID=userID,
                                        SubtypeMeleeList=SubtypeMeleeList,
                                        SubtypeRangedList=SubtypeRangedList,
                                        curioList=curioList)
            elif j == 5:
                return render_template('shopChecker.html', title="Shop Checker Results", 
                        getDetails=getDetails,
                        character1=character1, 
                        character2=character2,
                        character3=character3,
                        character4=character4,
                        character5=character5,
                        userList=userList, 
                        userID=userID,
                        SubtypeMeleeList=SubtypeMeleeList,
                        SubtypeRangedList=SubtypeRangedList,
                        curioList=curioList)
            else:
                flash("Issue with getting player characters, please try again later or contact an admin on discord!", "danger")
                return redirect(url_for('home'))
                

@app.route('/shopchecker/submit/', methods=['POST'])
@login_required
def shopTest():
    userID = current_user.id
    value = sc.shopSubmit(userID)
    if value:
        flash("Successfully verified token!", "success")
        return redirect(url_for('shopChecker'))
    else:
        flash("Incorrect or unable to verify token / account ID!", "danger")
        return redirect(url_for('shopChecker'))

@app.route('/buildeditor/submit/<classSelected>', methods=['POST'])
@login_required
def buildEditorSubmit(classSelected):
    userID = current_user.id
    be.validateBuild(classSelected, userID)
    return redirect(url_for('builds'))

@app.route('/editbuild/submit/<classSelected>/<urlHASH>', methods=['POST'])
@login_required
def editBuildSubmit(classSelected, urlHASH):
    userID = current_user.id
    build = Builds.query.filter_by(urlHASH=urlHASH).first()
    if build.UserID != userID:
        flash("You do not own this build!", "danger")
        return redirect(url_for('builds'))
    else:
        print("Class: " + classSelected)
        print("URL: " + urlHASH)
        print("User: " + str(userID))
        eb.editBuild(classSelected, userID, urlHASH)
        return redirect(url_for('builds'))

@app.route('/buildeditor/<classSelected>', methods=['GET', 'POST'])
def buildEditor(classSelected):
    title = "Build Editor ~ Darkmass"
    if classSelected == "Ogryn":
        meleeSubtypeByClass = SubtypeMelee.query.filter(SubtypeMelee.classes.ilike('%' + "Ogryn" + '%')).all()
        rangedSubtypeByClass = SubtypeRanged.query.filter(SubtypeRanged.classes.ilike('%' + "Ogryn" + '%')).all()
        perksList = perks.query.all()
        curiosList = curios.query.all()
        curioTraitList = curioTraits.query.all()
        blessingList = Blessings.query.all()
        classList = Classes.query.all()
        model = Classes.query.filter_by(shortName=classSelected).first()
        talentList = OgrynTalents.query.all()
        return render_template('buildeditor.html', title=title, meleeSubtypeList=meleeSubtypeByClass, shortName=classSelected, rangedSubtypeList=rangedSubtypeByClass,
                            perksList=perksList, curiosList=curiosList, blessingList=blessingList, curioTraitList=curioTraitList, talentList=talentList, model=model, classList=classList)
    elif classSelected == "Psyker":
        meleeSubtypeByClass = SubtypeMelee.query.filter(SubtypeMelee.classes.ilike('%' + "Psyker" + '%')).all()
        rangedSubtypeByClass = SubtypeRanged.query.filter(SubtypeRanged.classes.ilike('%' + "Psyker" + '%')).all()
        perksList = perks.query.all()
        curiosList = curios.query.all()
        curioTraitList = curioTraits.query.all()
        blessingList = Blessings.query.all()
        classList = Classes.query.all()
        model = Classes.query.filter_by(shortName=classSelected).first()
        talentList = PsykerTalents.query.all()
        return render_template('buildeditor.html', title=title, meleeSubtypeList=meleeSubtypeByClass, shortName=classSelected, rangedSubtypeList=rangedSubtypeByClass,
                            perksList=perksList, curiosList=curiosList, blessingList=blessingList, curioTraitList=curioTraitList, talentList=talentList, model=model, classList=classList)
    elif classSelected == "Veteran":
        meleeSubtypeByClass = SubtypeMelee.query.filter(SubtypeMelee.classes.ilike('%' + "Veteran" + '%')).all()
        rangedSubtypeByClass = SubtypeRanged.query.filter(SubtypeRanged.classes.ilike('%' + "Veteran" + '%')).all()
        perksList = perks.query.all()
        curiosList = curios.query.all()
        curioTraitList = curioTraits.query.all()
        blessingList = Blessings.query.all()
        classList = Classes.query.all()
        model = Classes.query.filter_by(shortName=classSelected).first()
        talentList = VeteranTalents.query.all()
        return render_template('buildeditor.html', title=title, meleeSubtypeList=meleeSubtypeByClass, shortName=classSelected, rangedSubtypeList=rangedSubtypeByClass,
                            perksList=perksList, curiosList=curiosList, blessingList=blessingList, curioTraitList=curioTraitList, talentList=talentList, model=model, classList=classList)
    elif classSelected == "Zealot":
        meleeSubtypeByClass = SubtypeMelee.query.filter(SubtypeMelee.classes.ilike('%' + "Zealot" + '%')).all()
        rangedSubtypeByClass = SubtypeRanged.query.filter(SubtypeRanged.classes.ilike('%' + "Zealot" + '%')).all()
        perksList = perks.query.all()
        curiosList = curios.query.all()
        curioTraitList = curioTraits.query.all()
        blessingList = Blessings.query.all()
        classList = Classes.query.all()
        model = Classes.query.filter_by(shortName=classSelected).first()
        talentList = ZealotTalents.query.all()
        return render_template('buildeditor.html', title=title, meleeSubtypeList=meleeSubtypeByClass, shortName=classSelected, rangedSubtypeList=rangedSubtypeByClass,
                            perksList=perksList, curiosList=curiosList, blessingList=blessingList, curioTraitList=curioTraitList, talentList=talentList, model=model, classList=classList)

@app.route('/buildeditor/buildeditor/blessings/melee/<weapon>', methods=['GET', 'POST'])
def _fragment_melee(weapon):
    q_blessing = Blessings.all_as_dict()
    q_melee = SubtypeMelee.query.filter_by(id=weapon).first()

    blessings = {}
    if q_melee:
        for value in q_melee.traits:
            if value in q_blessing:
                blessings[value] = q_blessing[value]

        return render_template('buildEditor/_fragment_melee.jinja', blessings=blessings)

    return "No Weapon Found"

@app.route('/buildeditor/buildeditor/blessings/melee/two/<weapon>', methods=['GET', 'POST'])
def _fragment_melee_two(weapon):
    q_blessingTwo = Blessings.all_as_dict()
    q_meleeTwo = SubtypeMelee.query.filter_by(id=weapon).first()

    blessingsTwo = {}
    if q_meleeTwo:
        for value in q_meleeTwo.traits:
            if value in q_blessingTwo:
                blessingsTwo[value] = q_blessingTwo[value]

        return render_template('buildEditor/_fragment_melee_two.jinja', blessings=blessingsTwo)

    return "No Weapon Found"

@app.route('/buildeditor/buildeditor/blessings/ranged/<weapon>', methods=['GET', 'POST'])
def _fragment_ranged(weapon):
    q_blessing = Blessings.all_as_dict()
    q_ranged = SubtypeRanged.query.filter_by(id=weapon).first()
    
    blessings = {}
    if q_ranged:
        for value in q_ranged.traits:
            if value in q_blessing:
                blessings[value] = q_blessing[value]

        return render_template('buildEditor/_fragment_ranged.jinja', blessings=blessings)
    
@app.route('/buildeditor/buildeditor/blessings/ranged/two/<weapon>', methods=['GET', 'POST'])
def _fragment_ranged_two(weapon):
    q_blessingTwo = Blessings.all_as_dict()
    q_rangedTwo = SubtypeRanged.query.filter_by(id=weapon).first()
    
    blessingsTwo = {}
    if q_rangedTwo:
        for value in q_rangedTwo.traits:
            if value in q_blessingTwo:
                blessingsTwo[value] = q_blessingTwo[value]

        return render_template('buildEditor/_fragment_ranged_two.jinja', blessings=blessingsTwo)
    
@app.route('/builds')
def builds():
    title = "Builds ~ Darkmass"
    userList = Users.query.all()
    buildsList = Builds.query.filter_by(visibility="public").all()
    subtypeRangedList = SubtypeRanged.query.all()
    subtypeMeleeList = SubtypeMelee.query.all()
    talentsList = AllTalents.query.all()
    return render_template('builds.html', title=title, buildsList=buildsList, userList=userList, subtypeRangedList=subtypeRangedList, subtypeMeleeList=subtypeMeleeList, talentsList=talentsList)

@app.route('/builds/<urlHASH>/<buildName>/delete')
@login_required
def deleteBuilds(urlHASH, buildName):
    userID = current_user.id
    user = Users.query.filter_by(id=userID).first()
    if user.discordID == "254337614256144384":
        Builds.query.filter(Builds.urlHASH == urlHASH).delete()
        db.session.commit()
        flash('Build Deleted', 'success')
        return redirect(url_for('home'))
    elif user.discordID == "143357379197665280":
        Builds.query.filter(Builds.urlHASH == urlHASH).delete()
        db.session.commit()
        flash('Build Deleted', 'success')
        return redirect(url_for('home'))
    else:
        flash('You do not have permission to delete builds!', 'danger')
        return redirect(url_for('home'))

@app.route('/builds/<urlHASH>/<buildName>/edit')
@login_required
def updateBuild(urlHASH, buildName):
    userID = current_user.id
    user = Users.query.filter_by(id=userID).first()
    build = Builds.query.filter_by(urlHASH=urlHASH).first()
    title = "Edit Build ~ Darkmass"
    if user.id == build.UserID:
        if build.selectedClass == "Ogryn":
            meleeSubtypeByClass = SubtypeMelee.query.filter(SubtypeMelee.classes.ilike('%' + "Ogryn" + '%')).all()
            rangedSubtypeByClass = SubtypeRanged.query.filter(SubtypeRanged.classes.ilike('%' + "Ogryn" + '%')).all()
            perksList = perks.query.all()
            curiosList = curios.query.all()
            curioTraitList = curioTraits.query.all()
            blessingList = Blessings.query.all()
            classList = Classes.query.all()
            model = Classes.query.filter_by(shortName=build.selectedClass).first()
            talentList = OgrynTalents.query.all()
            return render_template('editbuild.html', build=build, title=title, meleeSubtypeList=meleeSubtypeByClass, shortName=build.selectedClass, rangedSubtypeList=rangedSubtypeByClass,
                                perksList=perksList, curiosList=curiosList, blessingList=blessingList, curioTraitList=curioTraitList, talentList=talentList, model=model, classList=classList, urlHASH=urlHASH)
        elif build.selectedClass == "Psyker":
            meleeSubtypeByClass = SubtypeMelee.query.filter(SubtypeMelee.classes.ilike('%' + "Psyker" + '%')).all()
            rangedSubtypeByClass = SubtypeRanged.query.filter(SubtypeRanged.classes.ilike('%' + "Psyker" + '%')).all()
            perksList = perks.query.all()
            curiosList = curios.query.all()
            curioTraitList = curioTraits.query.all()
            blessingList = Blessings.query.all()
            classList = Classes.query.all()
            model = Classes.query.filter_by(shortName=build.selectedClass).first()
            talentList = PsykerTalents.query.all()
            return render_template('editbuild.html', title=title, build=build,meleeSubtypeList=meleeSubtypeByClass, shortName=build.selectedClass, rangedSubtypeList=rangedSubtypeByClass,
                                perksList=perksList, curiosList=curiosList, blessingList=blessingList, curioTraitList=curioTraitList, talentList=talentList, model=model, classList=classList, urlHASH=urlHASH)
        elif build.selectedClass == "Veteran":
            meleeSubtypeByClass = SubtypeMelee.query.filter(SubtypeMelee.classes.ilike('%' + "Veteran" + '%')).all()
            rangedSubtypeByClass = SubtypeRanged.query.filter(SubtypeRanged.classes.ilike('%' + "Veteran" + '%')).all()
            perksList = perks.query.all()
            curiosList = curios.query.all()
            curioTraitList = curioTraits.query.all()
            blessingList = Blessings.query.all()
            classList = Classes.query.all()
            model = Classes.query.filter_by(shortName=build.selectedClass).first()
            talentList = VeteranTalents.query.all()
            return render_template('editbuild.html', title=title, build=build, meleeSubtypeList=meleeSubtypeByClass, shortName=build.selectedClass, rangedSubtypeList=rangedSubtypeByClass,
                                perksList=perksList, curiosList=curiosList, blessingList=blessingList, curioTraitList=curioTraitList, talentList=talentList, model=model, classList=classList, urlHASH=urlHASH)
        elif build.selectedClass == "Zealot":
            meleeSubtypeByClass = SubtypeMelee.query.filter(SubtypeMelee.classes.ilike('%' + "Zealot" + '%')).all()
            rangedSubtypeByClass = SubtypeRanged.query.filter(SubtypeRanged.classes.ilike('%' + "Zealot" + '%')).all()
            perksList = perks.query.all()
            curiosList = curios.query.all()
            curioTraitList = curioTraits.query.all()
            blessingList = Blessings.query.all()
            classList = Classes.query.all()
            model = Classes.query.filter_by(shortName=build.selectedClass).first()
            talentList = ZealotTalents.query.all()
            return render_template('editbuild.html', title=title, build=build, meleeSubtypeList=meleeSubtypeByClass, shortName=build.selectedClass, rangedSubtypeList=rangedSubtypeByClass,
                                perksList=perksList, curiosList=curiosList, blessingList=blessingList, curioTraitList=curioTraitList, talentList=talentList, model=model, classList=classList, urlHASH=urlHASH)
    else:
        flash("You do not have permission to edit this build.", "danger")
        return redirect(url_for('home'))
    
@app.route('/builds/<urlHASH>/<buildName>/buildeditor/blessings/melee/<weapon>', methods=['GET', 'POST'])
def _fragment_melee_edit(weapon, urlHASH, buildName):
    q_blessing = Blessings.all_as_dict()
    q_melee = SubtypeMelee.query.filter_by(id=weapon).first()

    blessings = {}
    if q_melee:
        for value in q_melee.traits:
            if value in q_blessing:
                blessings[value] = q_blessing[value]

        return render_template('editBuild/_fragment_melee.jinja', blessings=blessings)

    return "No Weapon Found"

@app.route('/builds/<urlHASH>/<buildName>/buildeditor/blessings/melee/two/<weapon>', methods=['GET', 'POST'])
def _fragment_melee_two_edit(weapon, urlHASH, buildName):
    q_blessingTwo = Blessings.all_as_dict()
    q_meleeTwo = SubtypeMelee.query.filter_by(id=weapon).first()

    blessingsTwo = {}
    if q_meleeTwo:
        for value in q_meleeTwo.traits:
            if value in q_blessingTwo:
                blessingsTwo[value] = q_blessingTwo[value]

        return render_template('editBuild/_fragment_melee_two.jinja', blessings=blessingsTwo)

    return "No Weapon Found"

@app.route('/builds/<urlHASH>/<buildName>/buildeditor/blessings/ranged/<weapon>', methods=['GET', 'POST'])
def _fragment_ranged_edit(weapon, urlHASH, buildName):
    q_blessing = Blessings.all_as_dict()
    q_ranged = SubtypeRanged.query.filter_by(id=weapon).first()
    
    blessings = {}
    if q_ranged:
        for value in q_ranged.traits:
            if value in q_blessing:
                blessings[value] = q_blessing[value]

        return render_template('editBuild/_fragment_ranged.jinja', blessings=blessings)
    
@app.route('/builds/<urlHASH>/<buildName>/buildeditor/blessings/ranged/two/<weapon>', methods=['GET', 'POST'])
def _fragment_ranged_two_edit(weapon, urlHASH, buildName):
    q_blessingTwo = Blessings.all_as_dict()
    q_rangedTwo = SubtypeRanged.query.filter_by(id=weapon).first()
    
    blessingsTwo = {}
    if q_rangedTwo:
        for value in q_rangedTwo.traits:
            if value in q_blessingTwo:
                blessingsTwo[value] = q_blessingTwo[value]

        return render_template('editBuild/_fragment_ranged_two.jinja', blessings=blessingsTwo)


@app.route('/builds/<classSelected>')
def buildsClassFilter(classSelected):
    title = "Builds ~ Darkmass"
    userList = Users.query.all()
    subtypeRangedList = SubtypeRanged.query.all()
    subtypeMeleeList = SubtypeMelee.query.all()
    talentsList = AllTalents.query.all()
    if classSelected == "Ogryn":
        buildsList = Builds.query.filter_by(selectedClass=classSelected,visibility="public").all()
        return render_template('builds.html', title=title, buildsList=buildsList, userList=userList, subtypeRangedList=subtypeRangedList, subtypeMeleeList=subtypeMeleeList, talentsList=talentsList)
    elif classSelected == "Veteran":
        buildsList = Builds.query.filter_by(selectedClass=classSelected,visibility="public").all()
        return render_template('builds.html', title=title, buildsList=buildsList, userList=userList, subtypeRangedList=subtypeRangedList, subtypeMeleeList=subtypeMeleeList, talentsList=talentsList)
    elif classSelected == "Psyker":
        buildsList = Builds.query.filter_by(selectedClass=classSelected,visibility="public").all()
        return render_template('builds.html', title=title, buildsList=buildsList, userList=userList, subtypeRangedList=subtypeRangedList, subtypeMeleeList=subtypeMeleeList, talentsList=talentsList)
    elif classSelected == "Zealot":
        buildsList = Builds.query.filter_by(selectedClass=classSelected,visibility="public").all()
        return render_template('builds.html', title=title, buildsList=buildsList, userList=userList, subtypeRangedList=subtypeRangedList, subtypeMeleeList=subtypeMeleeList, talentsList=talentsList)
    else:
        return render_template('error.html')
    
@app.route('/builds/social/<socialName>', methods=['GET'])
def buildsSocialFilter(socialName):
    title = socialName + " ~ Darkmass"
    userList = Users.query.all()
    subtypeRangedList = SubtypeRanged.query.all()
    subtypeMeleeList = SubtypeMelee.query.all()
    talentsList = AllTalents.query.all()
    if socialName == "Claysthetics":
        clay = Users.query.filter_by(discordID="133715304235794432").first()
        buildsList = Builds.query.filter_by(UserID=clay.id,visibility="public").all()
        return render_template('builds.html', title=title, buildsList=buildsList, userList=userList, subtypeRangedList=subtypeRangedList, subtypeMeleeList=subtypeMeleeList, talentsList=talentsList)
    else:
        return url_for('home')
    
@app.route('/buildsearch', methods=['POST', 'GET'])
def buildSearch():
    title = "Builds ~ Darkmass"
    searchQuery = request.form['searchQuery']
    searchQuery = searchQuery.replace("%20", " ")
    buildsList = Builds.query.filter(Builds.buildName.like('%' + searchQuery + '%'), Builds.visibility == "public").all()
    userList = Users.query.all()
    subtypeRangedList = SubtypeRanged.query.all()
    subtypeMeleeList = SubtypeMelee.query.all()
    talentsList = AllTalents.query.all()
    return render_template('builds.html', title=title, buildsList=buildsList, userList=userList, subtypeRangedList=subtypeRangedList, subtypeMeleeList=subtypeMeleeList, talentsList=talentsList)
    
@app.route('/builds/<urlHASH>/<buildName>')
def selectedBuild(urlHASH, buildName):
    title = "Build ~ Darkmass"
    meleeList = Melee.query.all()
    subtypeMeleeList = SubtypeMelee.query.all()
    rangedList = Ranged.query.all()
    subtypeRangedList = SubtypeRanged.query.all()
    blessingList = Blessings.query.all()
    perksList = perks.query.all()
    curioList = curios.query.all()
    curioTraitsList = curioTraits.query.all()
    classesList = Classes.query.all()
    talentList = AllTalents.query.all()
    try:
        selectedBuild = Builds.query.filter_by(urlHASH=urlHASH).first()
        nameCheck = selectedBuild.buildName
        if nameCheck == buildName:
            if selectedBuild.visibility == "public" or selectedBuild.visibility == "link-only":
                return render_template('selectedBuild.html', title=title, selected=selectedBuild, meleeList=meleeList, subtypeMeleeList=subtypeMeleeList, blessingList=blessingList, perksList=perksList, rangedList=rangedList, subtypeRangedList=subtypeRangedList, curioList=curioList, curioTraitsList=curioTraitsList, classesList=classesList, talentList=talentList)
            elif selectedBuild.visibility == "private":
                if current_user.is_authenticated:
                    if current_user.id == selectedBuild.UserID:
                        return render_template('selectedBuild.html', title=title, selected=selectedBuild, meleeList=meleeList, subtypeMeleeList=subtypeMeleeList, blessingList=blessingList, perksList=perksList, rangedList=rangedList, subtypeRangedList=subtypeRangedList, curioList=curioList, curioTraitsList=curioTraitsList, classesList=classesList, talentList=talentList)
                    else:
                        return render_template('error.html')
                else:
                    return render_template('error.html')
        else: 
            return render_template('error.html')
    except Exception as e:
        return render_template('error.html')
    
@app.route('/robots.txt')
@app.route('/sitemap.xml')
@app.route('/ads.txt')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])


@app.route('/auth/discord', methods=['GET', 'POST'])
def discordAuth():
    code = request.args.get('code')
    discordAuthResult = da.discordAuthFunction(code)
    if discordAuthResult == True:
        return redirect(url_for("home"))
    elif discordAuthResult == False:
        return redirect(url_for("home"))


@app.route('/search', methods=['POST'])
def Search():
    title = "Search Results ~ Darkmass"
    weaponName = request.form.get('weaponName')
    meleeList = Melee.query.filter(Melee.name.ilike('%' + weaponName + '%')).all()
    meleeSubtypeList = SubtypeMelee.query.filter(SubtypeMelee.name.ilike('%' + weaponName + '%')).all()
    rangedList = Ranged.query.filter(Ranged.name.ilike('%' + weaponName + '%')).all()
    rangedSubtypeList = SubtypeRanged.query.filter(SubtypeRanged.name.ilike('%' + weaponName + '%')).all()
    allRangedWeapons = Ranged.query.all()
    allMeleeWeapons = Melee.query.all()
    return render_template('results.html', title=title, allRangedWeapons=allRangedWeapons, allMeleeWeapons=allMeleeWeapons, meleeList=meleeList,
                           meleeSubtypeList=meleeSubtypeList, rangedList=rangedList, rangedSubtypeList=rangedSubtypeList, searchQuery=weaponName,
                           lenmeleeSubtypeList=len(meleeSubtypeList), lenrangedSubtypeList=len(rangedSubtypeList), lenmeleeList=len(meleeList),
                           lenrangedList=len(rangedList))


@app.route('/login', methods=['GET', 'POST'])
def login():
    flaskDebug = os.environ.get('FLASK_DEBUG')
    if str(flaskDebug) == "1":
        return redirect("",
                        code=302)
    else:
        return redirect(
            "",code=302)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/profile')
@login_required
def profile():
    title = "Profile ~ Darkmass"
    getUsersBuilds = Builds.query.filter_by(UserID=current_user.id).all()
    return render_template('profile.html', title=title, userBuilds=getUsersBuilds)


@app.route('/weapons')
def weapons():
    title = "Weapons ~ Darkmass"
    meleeList = Melee.query.all()
    subtypeMeleeList = SubtypeMelee.query.all()
    rangedList = Ranged.query.all()
    subtypeRangedList = SubtypeRanged.query.all()
    totalWeapons = len(meleeList) + len(rangedList)
    totalSubtypes = len(subtypeMeleeList) + len(subtypeRangedList)
    return render_template('weapons.html', totalWeapons=totalWeapons, totalSubtypes=totalSubtypes, title=title)


@app.route('/weapons/melee')
def melee():
    title = "Melee Weapons ~ Darkmass"
    meleeList = Melee.query.all()
    subtypeMeleeList = SubtypeMelee.query.all()
    return render_template('melee.html', title=title, meleeList=meleeList, meleeCount=len(meleeList), subtypeMeleeList=subtypeMeleeList,
                           subtypeMeleeCount=len(subtypeMeleeList))


@app.route('/weapons/melee/<name>')
def meleeItem(name):
    title = name + " ~ Darkmass"
    meleeWeapon = Melee.query.filter_by(name=name).first()
    if meleeWeapon == None:
        return render_template('error.html')
    SubtypeMeleeList = SubtypeMelee.query.filter_by(parentID=meleeWeapon.id).all()
    traitList = Traits.query.all()
    meleeActionsList = meleeActions.query.all()
    meleeSpecialActionsList = meleeSpecialActions.query.all()
    return render_template('meleeItem.html', title=title, meleeWeapon=meleeWeapon, SubtypeMeleeList=SubtypeMeleeList, traitList=traitList,
                           meleeActionsList=meleeActionsList, meleeSpecialActionsList=meleeSpecialActionsList)


@app.route('/weapons/melee/<name>/<subtype>')
def meleeSubtypeItem(name, subtype):
    title = subtype + " ~ Darkmass"
    meleeWeapon = Melee.query.filter_by(name=name).first()
    if meleeWeapon == None:
        return render_template('error.html')
    subtypeWeapon = SubtypeMelee.query.filter_by(name=subtype).first()
    if subtypeWeapon == None:
        return render_template('error.html')
    traitList = Traits.query.all()
    meleeActionList = meleeActions.query.all()
    meleeSpecialActionsList = meleeSpecialActions.query.all()
    return render_template('meleeSubtypeItem.html', title=title, meleeWeapon=meleeWeapon, subtypeWeapon=subtypeWeapon, traitList=traitList,
                           meleeActionList=meleeActionList, meleeSpecialActionsList=meleeSpecialActionsList)


@app.route('/weapons/ranged')
def ranged():
    title = "Ranged Weapons ~ Darkmass"
    rangedList = Ranged.query.all()
    SubtypeRangedList = SubtypeRanged.query.all()
    return render_template('ranged.html', title=title, rangedList=rangedList, rangedCount=len(rangedList), SubtypeRangedList=SubtypeRangedList,
                           SubtypeRangedCount=len(SubtypeRangedList))


@app.route('/weapons/ranged/<name>')
def rangedItem(name):
    title = name + " ~ Darkmass"
    rangedWeapon = Ranged.query.filter_by(name=name).first()
    if rangedWeapon == None:
        return render_template('error.html')
    rangedSubtypeList = SubtypeRanged.query.filter_by(parentID=rangedWeapon.id).all()
    traitList = RangedTraits.query.all()
    rangedActionsList = rangedActions.query.all()
    rangedSpecialActionsList = rangedSpecialActions.query.all()
    return render_template('rangedItem.html', title=title, rangedWeapon=rangedWeapon, rangedSubtypeList=rangedSubtypeList, rangedActionsList=rangedActionsList,
                           rangedSpecialActionsList=rangedSpecialActionsList, traitList=traitList)


@app.route('/weapons/ranged/<name>/<subtype>')
def rangedSubtypeItem(name, subtype):
    title = subtype + " ~ Darkmass"
    rangedWeapon = Ranged.query.filter_by(name=name).first()
    if rangedWeapon == None:
        return render_template('error.html')
    subtypeWeapon = SubtypeRanged.query.filter_by(name=subtype).first()
    if subtypeWeapon == None:
        return render_template('error.html')
    traitList = RangedTraits.query.all()
    rangedActionList = rangedActions.query.all()
    rangedSpecialActionList = rangedSpecialActions.query.all()
    return render_template('rangedSubtypeItem.html', title=title, rangedWeapon=rangedWeapon, subtypeWeapon=subtypeWeapon, traitList=traitList,
                           rangedActionList=rangedActionList, rangedSpecialActionList=rangedSpecialActionList)


@app.route('/classes')
def classes():
    title = "Classes ~ Darkmass"
    return render_template('classes.html', title=title)


@app.route('/class/<name>')
def classSelection(name):
    title = name + " ~ Darkmass"
    model = Classes.query.filter_by(name=name).first()
    if model == None:
        title = "Error ~ Darkmass"
        return render_template('error.html', title=title)
    if name == "Ogryn Skullbreaker":
        talentList = OgrynTalents.query.all()
    elif name == "Psyker Psykinetic":
        talentList = PsykerTalents.query.all()
    elif name == "Veteran Sharpshooter":
        talentList = VeteranTalents.query.all()
    elif name == "Zealot Preacher":
        talentList = ZealotTalents.query.all()
    return render_template('class.html', title=title, model=model, talentList=talentList)


@app.route('/curios')
def curio():
    title = "Curios ~ Darkmass"
    curiosList = curios.query.all()
    curioTraitList = curioTraits.query.all()
    return render_template('curios.html', title=title, curiosList=curiosList, curioTraitList=curioTraitList)


@app.route('/blessings')
def blessing():
    title = "Blessings ~ Darkmass"
    blessingList = Blessings.query.order_by(Blessings.name)
    subtypeRangedList = SubtypeRanged.query.all()
    subtypeMeleeList = SubtypeMelee.query.all()
    rangedList = Ranged.query.all()
    meleeList = Melee.query.all()
    return render_template('blessings.html', title=title, blessingList=blessingList, subtypeRangedList=subtypeRangedList, subtypeMeleeList=subtypeMeleeList,
                           rangedList=rangedList, meleeList=meleeList)


@app.route('/perks')
def perk():
    title = "Perks ~ Darkmass"
    perkList = perks.query.all()
    return render_template('perks.html', title=title, perkList=perkList)

@app.route('/statsbreakdown')
def stats():
    title = "Stats Breakdown ~ Darkmass"
    return render_template('statsBreakdown.html', title=title)


@app.route('/glossary')
@app.route('/statsbreakdown/glossary')
def glossaryPage():
    title = "Darktide Glossary ~ Darkmass"
    glossaryList = glossary.query.all()
    baseCritList = baseCrit.query.order_by(baseCrit.name)
    return render_template('glossary.html', title=title, glossaryList=glossaryList, baseCritList=baseCritList)


@app.route('/meleestats')
@app.route('/statsbreakdown/meleestats')
def meleeStats():
    title = "Darktide Melee Stats ~ Darkmass"
    meleeTable = Melee.query.all()
    meleeActionsList = meleeActions.query.all()
    meleeSpecialActionsList = meleeSpecialActions.query.all()
    meleeBarsList = meleeBars.query.all()
    return render_template('meleeStats.html', title=title, meleeActionsList=meleeActionsList, meleeSpecialActionsList=meleeSpecialActionsList,
                           meleeBarsList=meleeBarsList, meleeTable=meleeTable)

@app.route('/rangedstats')
@app.route('/statsbreakdown/rangedstats')
def rangedStats():
    title = "Darktide Ranged Stats ~ Darkmass"
    rangedTable = Ranged.query.all()
    rangedActionsList = rangedActions.query.all()
    rangedSpecialActionsList = rangedSpecialActions.query.all()
    rangedBarsList = rangedBars.query.all()
    rangedBarsDetailedList = rangedBarsDetailed.query.all()
    rangedActionsSimpleList = rangedActionsSimple.query.all()
    rangedFireList = rangedFire.query.all()
    staffsList = staffs.query.all()
    return render_template('rangedStats.html', title=title, rangedActionsList=rangedActionsList, rangedSpecialActionsList=rangedSpecialActionsList, rangedTable=rangedTable, rangedBarsList=rangedBarsList, rangedBarsDetailedList=rangedBarsDetailedList, rangedActionsSimpleList=rangedActionsSimpleList, rangedFireList=rangedFireList, staffsList=staffsList)

@app.route('/privacy')
def privacy():
    title = "Privacy ~ Darkmass"
    return render_template('components/privacypolicy.html', title=title)


@app.route('/disclaimer')
def disclaimer():
    title = "Disclaimer ~ Darkmass"
    return render_template('components/disclaimer.html', title=title)


@app.route('/termsofuse')
def tou():
    title = "Terms of Use ~ Darkmass"
    return render_template('components/termsofuse.html', title=title)


@app.errorhandler(404)
def error404(e):
    title = "Error 404 ~ Darkmass"
    return render_template('error.html', title=title), 404


@app.errorhandler(500)
def error500(e):
    title = "Error 500 ~ Darkmass"
    return render_template('error.html', title=title), 500