from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:blanetech123@localhost/data_scraping"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)

class Players(db.Model):
    player_id = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String(255) ,nullable=False)
    player_salary = db.Column(db.String(255), nullable=True)
    championship = db.Column(db.String(255), nullable=False)


class Teams(db.Model):
    team_id = db.Column(db.Integer, primary_key = True)
    team_name = db.Column(db.String(255), nullable=False)
    team_value = db.Column(db.String(255), nullable=False)
    championship = db.Column(db.String(255), nullable=False)


if __name__ == '__main__':
    db.drop_all()
    db.create_all()