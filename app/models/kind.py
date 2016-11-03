from app import db


class Kind(db.Model):
    __tablename__ = "kind"
    extend_existing = True

    Id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.VARCHAR(20))  # TODO larger
    Product=db.relationship("Product",backref=db.backref("Kinds"))

    def __init__(self, name):
        self.Name = name

    def __repr__(self):
        return '<Kind %r:Name %r>' % (self.Id, self.Name)
