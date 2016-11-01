from .. import db


class Product_Order(db.model):
    __tablename__ = "product_order"
    extend_existing = True

    Id = db.Column(db.Integer, primary_key=True)
    Count = db.Column(db.Integer)
    Product = db.relationship("Product", backref=db.backref("Product_Orders"))
    Order = db.relationship("Order", backref=db.backref("Product_Orders"))

    def __init__(self, count):
        if count <= 0:
            raise ValueError("count must be greater than 0")
        self.Count = count

    def __repr__(self):
        return '<Product_Order %r:Product %r,Order %r,Count %r>' % (self.Id, self.Product, self.Order, self.Count)
