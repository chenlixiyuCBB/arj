from app import db

Collect = db.Table("collect",
                   db.Column("Id",db.Integer,primary_key=True),
                   db.Column("UId", db.ForeignKey("user.Id")),
                   db.Column("PId", db.ForeignKey("product.Id")),
                   extend_existing=True)


class Product_Order(db.Model):
    __tablename__ = "product_order"
    # extend_existing = True

    Id = db.Column(db.Integer, primary_key=True)
    PId = db.Column(db.Integer, db.ForeignKey("product.Id"))
    OId = db.Column(db.Integer, db.ForeignKey("order.Id"))
    Count = db.Column(db.Integer)
    Product = db.relationship("Product", backref=db.backref("Product_Orders"))
    Order = db.relationship("Order", backref=db.backref("Product_Orders"))

    def __init__(self, count):
        if count <= 0:
            raise ValueError("count must be greater than 0")
        self.Count = count

    def __repr__(self):
        return '<Product_Order %r:Product %r,Order %r,Count %r>' % (self.Id, self.Product, self.Order, self.Count)


class Order(db.Model):
    __tablename__ = "order"
    # extend_existing = True

    Id = db.Column(db.Integer, primary_key=True)
    UId = db.Column(db.Integer, db.ForeignKey("user.Id"))
    Date = db.Column(db.VARCHAR(45))
    Address = db.Column(db.VARCHAR(45))  # TODO change to text
    Phone = db.Column(db.VARCHAR(13))
    Status = db.Column(db.Integer)
    Sum = db.Column(db.Integer)
    Name = db.Column(db.VARCHAR(15))
    User = db.relationship("User", backref=db.backref("Orders"))

    def __init__(self, date, address, phone, status, sum_, name):
        if sum_ < 0:
            raise ValueError("Order Sum can't be smaller than 0")

        self.Name = name
        self.Date = date
        self.Address = address
        self.Phone = phone
        self.Status = status
        self.Sum = sum_

    def __repr__(self):
        return '<Order %r:User %r>' % (self.Id, self.User)


class Product(db.Model):
    __tablename__ = "product"
    # extend_existing = True

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
        return '<Product %r:Name %r,Price %r,Inventory %r>' % (self.Id, self.Name, self.Price, self.Inventory)


class Address(db.Model):
    __tablename__ = "address"
    # extend_existing = True

    Id = db.Column(db.Integer, primary_key=True)
    UId = db.Column(db.Integer, db.ForeignKey("user.Id"))
    Address = db.Column(db.VARCHAR(45))
    Phone = db.Column(db.Integer)
    User = db.relationship('User', backref=db.backref('Addresses'))

    def __init__(self, address, phone):
        self.Address = address
        self.Phone = phone

    def __repr__(self):
        return '<Address %r:Address %r,Phone %r>' % (self.Id, self.Address, self.Phone)


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


class BuyCart(db.Model):
    __tablename__ = "buycart"
    # extend_existing = True

    Id = db.Column(db.Integer, primary_key=True)
    UId = db.Column(db.Integer, db.ForeignKey("user.Id"))
    PId = db.Column(db.Integer, db.ForeignKey("product.Id"))
    Count = db.Column(db.Integer)
    User = db.relationship("User", backref=db.backref("BuyCarts"))
    Product = db.relationship("Product", backref=db.backref("BuyCarts"))

    def __init__(self, count):
        if count <= 0:
            raise ValueError("BuyCart count must be greater than 0")
        self.Count = count

    def __repr__(self):
        return '<BuyCart %r:User %r,Product %r,Count %r>' % (self.Id, self.User.Id, self.Product.Id, self.Count)


class Kind(db.Model):
    __tablename__ = "kind"
    # extend_existing = True

    Id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.VARCHAR(20))  # TODO larger
    PId = db.Column(db.Integer, db.ForeignKey("product.Id"))
    Product = db.relationship("Product", backref=db.backref("Kinds"))

    def __init__(self, name):
        self.Name = name

    def __repr__(self):
        return '<Kind %r:Name %r>' % (self.Id, self.Name)


class User(db.Model):
    __tablename__ = "user"

    Id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.VARCHAR(20), unique=True)
    PassWd = db.Column(db.VARCHAR(15))  # TODO larger
    Phone = db.Column(db.VARCHAR(13), nullable=True)
    collect_products = db.relationship("Product", secondary=Collect, backref="Users")

    def __init__(self, name, pass_wd, phone=None):
        self.Name = name
        self.PassWd = pass_wd
        self.Phone = phone

    def __repr__(self):
        return '<User %r:Name %r>' % (self.Id, self.Name)
