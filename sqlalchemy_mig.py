
from flask import Flask

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Person(db.Model):
    id = db.column(db.Integer, primary_key=True)
