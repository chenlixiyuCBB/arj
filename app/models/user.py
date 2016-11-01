from .. import db


class User(db.model):
    __tablename__ = "user"

    Id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.VARCHAR(20), unique=True)
    PassWd = db.Column(db.VARCHAR(15))  # TODO larger
    Phone = db.Column(db.VARCHAR(13), nullable=True)

    def __init__(self, name, pass_wd, phone=None):
        self.Name = name
        self.PassWd = pass_wd
        self.Phone = phone

    def __repr__(self):
        return '<User %r:Name %r>' % (self.Id, self.Name)
