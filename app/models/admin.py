from app import db


class Admin(db.Model):
    __tablename__ = "admin"
    extend_existing = True

    Id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.VARCHAR(20), unique=True)
    PassWd = db.Column(db.VARCHAR(15))  # TODO larger

    def __init__(self, name, pass_wd):
        self.Name = name
        self.PassWd = pass_wd

    def __repr__(self):
        return '<Admin %r:Name %r>' % (self.Id, self.Name)
