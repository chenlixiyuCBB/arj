from .. import db


class Address(db.model):
    __tablename__ = "address"
    extend_existing = True

    Id = db.Column(db.Integer, primary_key=True)
    Address = db.Column(db.VARCHAR(45))
    Phone = db.Column(db.Integer)
    User = db.relationship('User', backref=db.backref('Addresses'))

    def __init__(self, address, phone):
        self.Address = address
        self.Phone = phone

    def __repr__(self):
        return '<Address %r:Address %r,Phone %r>' % (self.Id, self.Address, self.Phone)
