from app import db
from app.models import Users

if __name__ == "__main__":
    Users.query.filter_by(id = 575).delete()
    db.session.commit()
