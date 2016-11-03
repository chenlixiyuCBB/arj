from app import db


class Order(db.Model):
    __tablename__ = "order"
    extend_existing = True

    Id = db.Column(db.Integer, primary_key=True)
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
