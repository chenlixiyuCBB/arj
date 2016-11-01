from .. import db


class Product(db.model):
    __tablename__ = "product"
    extend_existing = True

    Id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.VARCHAR(20))
    Detail = db.Column(db.TEXT)
    Image = db.Column(db.VARCHAR(100))
    Price = db.Column(db.Float)
    Inventory = db.Column(db.Integer)

    def __init__(self, name, price, inventory, detail=None, image=None):
        if price <= 0:
            raise ValueError("Product price must be greater than 0")
        if inventory < 0:
            raise ValueError("Product inventory can't be smaller than 0")
        self.Name = name
        self.Price = price
        self.Inventory = inventory
        self.Detail = detail
        self.Image = image

    def __repr__(self):
        return '<Product %r:Name %r,Price %r,Left %r>' % (self.Id, self.Name, self.Price, self.Left)
