from .. import db


class BuyCart(db.Model):
    __tablename__ = "buycart"
    extend_existing = True

    Id = db.Column(db.Integer, primary_key=True)
    Count = db.Column(db.Integer)
    User=db.relationship("User",backref=db.backref("BuyCarts"))
    Product=db.relationship("Product",backref=db.backref("BuyCarts"))

    def __init__(self, count):
        if count<=0:
            raise ValueError("BuyCart count must be greater than 0")
        self.Count = count


    def __repr__(self):
        return '<BuyCart %r:User %r,Product %r,Count %r>' % (self.Id, self.User, self.Product,self.Count)
