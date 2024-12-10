from flask import Flask
from app import app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy(app)


class Buku(db.Model):
    __tablename__ = "buku"
    id = db.Column(db.Integer, primary_key=True)
    judul = db.Column(db.String(100),nullable=False)
    pengarang = db.Column(db.String(100),nullable=False)
    penerbit = db.Column(db.String(100),nullable=False)
    genre = db.Column(db.String(100),nullable=False)
    jenis_buku = db.Column(db.String(100),nullable=False)