from flask_login import UserMixin

from app import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    discriminator = db.Column(db.String(100), nullable=False)
    discordID = db.Column(db.String(100), unique=True, nullable=False)
    avatar = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    mfaEnabled = db.Column(db.String(100), nullable=False)
    premiumType = db.Column(db.String(100), nullable=False)
    accountID = db.Column(db.String(100), nullable=True)
    refreshToken = db.Column(db.String(100), nullable=True)
    accessToken = db.Column(db.String(100), nullable=True)
    children = db.relationship('Builds', backref='parent', lazy=True)

    def __repr__(self):
        return f"User('{self.discriminator}', '{self.discordID}', '{self.avatar}', '{self.location}', '{self.mfaEnabled}', '{self.premiumType}', '{self.accountID}', '{self.refreshToken})"


class Builds(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    UserID = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    buildName = db.Column(db.String(100), nullable=False)
    visibility = db.Column(db.String(100), nullable=False)
    # Need Threat Levels
    threatLevel = db.Column(db.String(100), nullable=True)
    selectedClass = db.Column(db.String(100), nullable=False)
    meleeWeapon = db.Column(db.String(100), nullable=False)
    meleeWeaponPerkOne = db.Column(db.String(100), nullable=False)
    meleeWeaponPerkTwo = db.Column(db.String(100), nullable=False)
    meleeWeaponBlessingOne = db.Column(db.String(100), nullable=False)
    meleeWeaponBlessingTwo = db.Column(db.String(100), nullable=False)
    rangedWeapon = db.Column(db.String(100), nullable=False)
    rangedWeaponPerkOne = db.Column(db.String(100), nullable=False)
    rangedWeaponPerkTwo = db.Column(db.String(100), nullable=False)
    rangedWeaponBlessingOne = db.Column(db.String(100), nullable=False)
    rangedWeaponBlessingTwo = db.Column(db.String(100), nullable=False)
    curioNameOne = db.Column(db.String(100), nullable=False)
    curioBlessingOne = db.Column(db.String(100), nullable=False)
    curioPerkOneOne = db.Column(db.String(100), nullable=False)
    curioPerkOneTwo = db.Column(db.String(100), nullable=False)
    curioPerkOneThree = db.Column(db.String(100), nullable=False)
    curioNameTwo = db.Column(db.String(100), nullable=False)
    curioBlessingTwo = db.Column(db.String(100), nullable=False)
    curioPerkTwoOne = db.Column(db.String(100), nullable=False)
    curioPerkTwoTwo = db.Column(db.String(100), nullable=False)
    curioPerkTwoThree = db.Column(db.String(100), nullable=False)
    curioNameThree = db.Column(db.String(100), nullable=False)
    curioBlessingThree = db.Column(db.String(100), nullable=False)
    curioPerkThreeOne = db.Column(db.String(100), nullable=False)
    curioPerkThreeTwo = db.Column(db.String(100), nullable=False)
    curioPerkThreeThree = db.Column(db.String(100), nullable=False)
    level5Talent = db.Column(db.String(100), nullable=False)
    level10Talent = db.Column(db.String(100), nullable=False)
    level15Talent = db.Column(db.String(100), nullable=False)
    level20Talent = db.Column(db.String(100), nullable=False)
    level25Talent = db.Column(db.String(100), nullable=False)
    level30Talent = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    youtubeLink = db.Column(db.String(100), nullable=True)
    urlHASH = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Builds('{self.buildName}', '{self.visibility}', '{self.threatLevel}', '{self.selectedClass}', '{self.meleeWeapon}', '{self.meleeWeaponPerkOne}', '{self.meleeWeaponPerkTwo}', '{self.meleeWeaponBlessingOne}', '{self.meleeWeaponBlessingTwo}', '{self.rangedWeapon}', '{self.rangedWeaponPerkOne}', '{self.rangedWeaponPerkTwo}', '{self.rangedWeaponBlessingOne}', '{self.rangedWeaponBlessingTwo}', '{self.curioNameOne}', '{self.curioBlessingOne}', '{self.curioPerkOneOne}', '{self.curioPerkOneTwo}', '{self.curioPerkOneThree}', '{self.curioNameTwo}', '{self.curioBlessingTwo}', '{self.curioPerkTwoOne}', '{self.curioPerkTwoTwo}', '{self.curioPerkTwoThree}', '{self.curioNameThree}', '{self.curioBlessingThree}', '{self.curioPerkThreeOne}', '{self.curioPerkThreeTwo}', '{self.curioPerkThreeThree}', '{self.level5Talent}', '{self.level10Talent}', '{self.level15Talent}', '{self.level20Talent}', '{self.level25Talent}', '{self.level30Talent}', '{self.description}', '{self.youtubeLink}', '{self.urlHASH}')"


class Traits(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Traits('{self.name}', '{self.primaryAction}', '{self.secondaryAction}')"


class RangedTraits(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Ranged Traits('{self.name}', '{self.primaryAction}', '{self.secondaryAction}')"


class Blessings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Blessings('{self.name}', '{self.primaryAction}', '{self.secondaryAction}')"

    @classmethod
    def all_as_dict(cls) -> dict:
        q = cls.query.all()
        rdict = dict()
        for val in q:
            rdict.update({val.name: {"id": val.id, "name": val.name, "image": val.image, "description": val.description}})
        return rdict


class meleeActions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    detailedDescription = db.Column(db.JSON, nullable=False)

    def __repr__(self):
        return f"Melee Actions ('{self.name}', '{self.image}'), '{self.description}')"


class meleeSpecialActions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    detailedDescription = db.Column(db.JSON, nullable=False)
    gif = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Melee Special Actions ('{self.name}', '{self.image}')"


class rangedActions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Ranged Actions ('{self.name}', '{self.image}')"


class rangedSpecialActions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return f"Ranged Special Actions ('{self.name}', '{self.image}')"


class Melee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    primaryAction = db.Column(db.String(100), nullable=False)
    secondaryAction = db.Column(db.String(100), nullable=False)
    specialAction = db.Column(db.String(100), nullable=False)
    children = db.relationship('SubtypeMelee', backref='parent', lazy=True)
    classes = db.Column(db.String(100), nullable=False)
    traits = db.Column(db.JSON, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    tag = db.Column(db.JSON, nullable=False)
    image = db.Column(db.String(100), nullable=False)
    bars = db.Column(db.JSON, nullable=False)

    def __repr__(self):
        return f"Melee('{self.name}', '{self.primaryAction}', '{self.secondaryAction}', '{self.specialAction}', '{self.classes}', '{self.traits}')"


class SubtypeMelee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    parentID = db.Column(db.Integer, db.ForeignKey('melee.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    codeName = db.Column(db.String(100), nullable=False, server_default='Placeholder')
    primaryAction = db.Column(db.String(100), nullable=False)
    secondaryAction = db.Column(db.String(100), nullable=False)
    specialAction = db.Column(db.String(100), nullable=False)
    classes = db.Column(db.String(100), nullable=False)
    traits = db.Column(db.JSON, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    tag = db.Column(db.JSON, nullable=False)
    image = db.Column(db.String(100), nullable=False)
    lightCombo = db.Column(db.JSON, nullable=True)
    heavyCombo = db.Column(db.JSON, nullable=True)

    def __repr__(self):
        return f"SubtypeMelee('{self.name}', '{self.primaryAction}', '{self.secondaryAction}', '{self.specialAction}', '{self.classes}', '{self.traits}')"


class Ranged(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    primaryAction = db.Column(db.String(100), nullable=False)
    secondaryAction = db.Column(db.String(100), nullable=False)
    specialAction = db.Column(db.String(100), nullable=False)
    children = db.relationship('SubtypeRanged', backref='parent', lazy=True)
    classes = db.Column(db.String(100), nullable=False)
    traits = db.Column(db.JSON, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    tag = db.Column(db.JSON, nullable=False)
    image = db.Column(db.String(100), nullable=False)
    bars = db.Column(db.JSON, nullable=False)
    
    def __repr__(self):
        return f"Ranged('{self.name}', '{self.primaryAction}', '{self.secondaryAction}', '{self.specialAction}', '{self.classes}', '{self.traits}')"


class SubtypeRanged(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    parentID = db.Column(db.Integer, db.ForeignKey('ranged.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    codeName = db.Column(db.String(100), nullable=False, server_default='Placeholder')
    primaryAction = db.Column(db.String(100), nullable=False)
    secondaryAction = db.Column(db.String(100), nullable=False)
    specialAction = db.Column(db.String(100), nullable=False)
    classes = db.Column(db.String(100), nullable=False)
    traits = db.Column(db.JSON, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    tag = db.Column(db.JSON, nullable=False)
    image = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"SubtypeRanged('{self.name}', '{self.primaryAction}', '{self.secondaryAction}', '{self.specialAction}', '{self.classes}', '{self.traits}')"


class Classes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    metalIcon = db.Column(db.String(100), nullable=False)
    normalIcon = db.Column(db.String(100), nullable=False)
    shortName = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    health = db.Column(db.String(100), nullable=False)
    toughness = db.Column(db.String(100), nullable=False)
    ability = db.Column(db.String(100), nullable=False)
    abilityDescription = db.Column(db.String(500), nullable=False)
    abilityCooldown = db.Column(db.String(100), nullable=False)
    abilityImage = db.Column(db.String(100), nullable=False)
    aura = db.Column(db.String(100), nullable=False)
    auraDescription = db.Column(db.String(500), nullable=False)
    auraImage = db.Column(db.String(100), nullable=False)
    blitz = db.Column(db.String(100), nullable=False)
    blitzDescription = db.Column(db.String(500), nullable=False)
    blitzImage = db.Column(db.String(100), nullable=False)
    iconicName1 = db.Column(db.String(100), nullable=False)
    iconicName1Description = db.Column(db.String(500), nullable=False)
    iconicName1Image = db.Column(db.String(100), nullable=False)
    iconicName2 = db.Column(db.String(100), nullable=False)
    iconicName2Description = db.Column(db.String(500), nullable=False)
    iconicName2Image = db.Column(db.String(100), nullable=False)
    iconicName3 = db.Column(db.String(100), nullable=True)
    iconicName3Description = db.Column(db.String(500), nullable=True)
    iconicName3Image = db.Column(db.String(100), nullable=True)
    level5 = db.Column(db.JSON, nullable=False)
    level10 = db.Column(db.JSON, nullable=False)
    level15 = db.Column(db.JSON, nullable=False)
    level20 = db.Column(db.JSON, nullable=False)
    level25 = db.Column(db.JSON, nullable=False)
    level30 = db.Column(db.JSON, nullable=False)

    def __repr__(self):
        return f"Classes('{self.name}', '{self.metalIcon}', '{self.normalIcon}','{self.description}', '{self.health}', '{self.toughness}', '{self.ability}', '{self.abilityDescription}', '{self.abilityCooldown}', '{self.abilityImage}', '{self.aura}', '{self.auraDescription}', '{self.auraImage}', '{self.blitz}', '{self.blitzDescription}', '{self.blitzImage}', '{self.iconicName1}', '{self.iconicName1Description}', '{self.iconicName1Image}', '{self.iconicName2}', '{self.iconicName2Description}', '{self.iconicName2Image}', '{self.iconicName3}', '{self.iconicName3Description}', '{self.iconicName3Image}', '{self.level5}', '{self.level10}', '{self.level15}', '{self.level20}', '{self.level25}', '{self.level30}')"



class AllTalents(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"AllTalents('{self.name}', '{self.description}', '{self.image}')"

class OgrynTalents(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"OgrynTalents('{self.name}', '{self.description}', '{self.image}')"


class PsykerTalents(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"PsykerTalents('{self.name}', '{self.description}', '{self.image}')"


class VeteranTalents(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"VeteranTalents('{self.name}', '{self.description}', '{self.image}')"


class ZealotTalents(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"ZealotTalents('{self.name}', '{self.description}', '{self.image}')"


class curios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    codeName = db.Column(db.JSON, nullable=False, server_default='Placeholder')
    image = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"curios('{self.name}', '{self.image}', '{self.codeName}')"


class curioTraits(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f"curioTraits('{self.type}', '{self.description}')"


class meleeBars(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    modifiers = db.Column(db.JSON, nullable=False)

    def __repr__(self):
        return f"meleeBars('{self.name}', '{self.image}', '{self.description}', '{self.modifiers}')"
    
class rangedBars(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    modifiers = db.Column(db.JSON, nullable=False)
    
class rangedBarsDetailed(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    weapon = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    bar1 = db.Column(db.String(100), nullable=False)
    bar1Modifiers = db.Column(db.JSON, nullable=False)
    bar2 = db.Column(db.String(100), nullable=False)
    bar2Modifiers = db.Column(db.JSON, nullable=False)
    bar3 = db.Column(db.String(100), nullable=False)
    bar3Modifiers = db.Column(db.JSON, nullable=False)
    bar4 = db.Column(db.String(100), nullable=False)
    bar4Modifiers = db.Column(db.JSON, nullable=False)
    bar5 = db.Column(db.String(100), nullable=False)
    bar5Modifiers = db.Column(db.JSON, nullable=False)
    
class rangedActionsSimple(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    detailedDescription = db.Column(db.JSON, nullable=False)
    
class rangedFire(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firemode = db.Column(db.String(100), nullable=False)
    fmImg = db.Column(db.String(100), nullable=False)
    fmDesc = db.Column(db.String(500), nullable=False)
    
class staffs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    primaryAction = db.Column(db.String(100), nullable=False)
    secondaryAction = db.Column(db.String(100), nullable=False)
    specialAction = db.Column(db.String(100), nullable=False)
       
class glossary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f"glossary('{self.name}', '{self.description}')"

class baseCrit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    crit = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"baseCrit('{self.name}', '{self.crit}')"

class perks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f"perks('{self.description}')"
    
    
