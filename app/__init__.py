from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object("config.config")
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://arj:@123.207.137.55:3306/arj'
db = SQLAlchemy(app)

from models.user import User
from models.address import Address
from models.admin import Admin
from models.buycart import BuyCart
from models.kind import Kind
from models.order import Order
from models.product import Product
from models.product_order import Product_Order
