from app import db
from app.models import Builds, perks, curioTraits


for build in Builds.query.all():
    for perk in perks.query.all():
        if build.meleeWeaponPerkOne == perk.description:
            Builds.query.filter_by(id=build.id).update({"meleeWeaponPerkOne": perk.id})
            db.session.commit()
        if build.meleeWeaponPerkTwo == perk.description:
            Builds.query.filter_by(id=build.id).update({"meleeWeaponPerkTwo": perk.id})
            db.session.commit()
        if build.rangedWeaponPerkOne == perk.description:
            Builds.query.filter_by(id=build.id).update({"rangedWeaponPerkOne": perk.id})
            db.session.commit()
        if build.rangedWeaponPerkTwo == perk.description:
            Builds.query.filter_by(id=build.id).update({"rangedWeaponPerkTwo": perk.id})
            db.session.commit()
    for curiotrait in curioTraits.query.all():
        if build.curioBlessingOne == curiotrait.description:
            Builds.query.filter_by(id=build.id).update({"curioBlessingOne": curiotrait.id})
            db.session.commit()
        if build.curioBlessingTwo == curiotrait.description:
            Builds.query.filter_by(id=build.id).update({"curioBlessingTwo": curiotrait.id})
            db.session.commit() 
        if build.curioBlessingThree == curiotrait.description:
            Builds.query.filter_by(id=build.id).update({"curioBlessingThree": curiotrait.id})
            db.session.commit()
        if build.curioPerkOneOne == curiotrait.description:
            Builds.query.filter_by(id=build.id).update({"curioPerkOneOne": curiotrait.id})
            db.session.commit()
        if build.curioPerkOneTwo == curiotrait.description:
            Builds.query.filter_by(id=build.id).update({"curioPerkOneTwo": curiotrait.id})
            db.session.commit()
        if build.curioPerkOneThree == curiotrait.description:
            Builds.query.filter_by(id=build.id).update({"curioPerkOneThree": curiotrait.id})
            db.session.commit()
            
        if build.curioPerkTwoOne == curiotrait.description:
            Builds.query.filter_by(id=build.id).update({"curioPerkTwoOne": curiotrait.id})
            db.session.commit()
        if build.curioPerkTwoTwo == curiotrait.description:
            Builds.query.filter_by(id=build.id).update({"curioPerkTwoTwo": curiotrait.id})
            db.session.commit()
        if build.curioPerkTwoThree == curiotrait.description:
            Builds.query.filter_by(id=build.id).update({"curioPerkTwoThree": curiotrait.id})
            db.session.commit()
            
        if build.curioPerkThreeOne == curiotrait.description:
            Builds.query.filter_by(id=build.id).update({"curioPerkThreeOne": curiotrait.id})
            db.session.commit()
        if build.curioPerkThreeTwo == curiotrait.description:
            Builds.query.filter_by(id=build.id).update({"curioPerkThreeTwo": curiotrait.id})
            db.session.commit()
        if build.curioPerkThreeThree == curiotrait.description:
            Builds.query.filter_by(id=build.id).update({"curioPerkThreeThree": curiotrait.id})
            db.session.commit()                       
