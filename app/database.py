import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Role(db.Model):
    __tablename__ = 'inventario'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    sell_in = db.Column(db.Integer, nullable=True)
    quality = db.Column(db.Integer, nullable=True)
    users = db.relationship('User', backref='inventario')

    def __repr__(self):
        return '<inventario %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    inventario_id = db.Column(db.Integer, db.ForeignKey('inventario.id'))

    def __repr__(self):
        return '<User %r>' % self.username


if __name__ == "__main__":
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()
