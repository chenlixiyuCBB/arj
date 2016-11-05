from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object("config.config")
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://arj:@123.207.137.55:3306/arj'
db = SQLAlchemy(app)

import views
