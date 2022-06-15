from flask import jsonify, render_template
from models.database import *
from flask_cors import CORS

import os
template_dir = os.path.abspath('templates')
app = Flask(__name__, template_folder=template_dir)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:blanetech123@localhost/data_scraping"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
CORS(app)

db.init_app(app)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/players/<string:championship>')
def get_nfl_data(championship):
    all_players_data = []

    championship_data = Players.query.filter_by(
        championship=championship.upper()).limit(30).all()
    for data in championship_data:
        player_data = {
            'name': data.player_name,
            'salary': data.player_salary
        }
        all_players_data.append(player_data)
    return jsonify(all_players_data)


@app.route('/players/total_value')
def get_total_players_value():
    all_players = Players.query.all()
    data_players = []
    total_value_nba = 0
    total_value_nfl = 0
    for player in all_players:
        str_value = player.player_salary
        salary = int(str_value.replace(" ", "").split("$")[0])
        temp = {
            'salary': salary,
            'champ': player.championship
        }
        data_players.append(temp)
    # print(data_players)
    for data in data_players:
        if data.get('champ') == "NBA":
            total_value_nba += data.get('salary')
        elif data.get('champ') == "NFL":
            total_value_nfl += data.get('salary')
    return jsonify({'nba': total_value_nba, 'nfl': total_value_nfl})


@app.route('/teams/<string:championship>')
def get_team_data(championship):
    all_teams_data = []
    championship_teams = Teams.query.filter_by(
        championship=championship.upper()).all()
    for team in championship_teams:
        team_data = {
            'name': team.team_name,
            'market_value': team.team_value
        }
        all_teams_data.append(team_data)
    return jsonify(all_teams_data)


@app.route('/teams/market_value_championship')
def market_value_championship():
    market_value_pl = 0
    market_value_sa = 0
    market_value_bdl = 0
    market_value_l1 = 0
    market_value_lg = 0
    market_values = Teams.query.all()
    for market_value in market_values:
        if market_value.championship == "PREMIER LEAGUE":
            value = market_value.team_value.replace(',', '.')
            market_value_pl += float(value)
        elif market_value.championship == "SERIE A":
            value = market_value.team_value.replace(',', '.')
            market_value_sa += float(value)
        elif market_value.championship == "BUNDESLIGA":
            value = market_value.team_value.replace(',', '.')
            market_value_bdl += float(value)
        elif market_value.championship == "LIGUE 1":
            value = market_value.team_value.replace(',', '.')
            market_value_l1 += float(value)
        elif market_value.championship == "LIGA":
            value = market_value.team_value.replace(',', '.')
            market_value_lg += float(value)
    # print(market_value_lg,"\n",market_value_bdl)
    return {
        'pl': market_value_pl,
        'l1': market_value_l1,
        'bdl': market_value_bdl,
        'lg': market_value_lg,
        'sa': market_value_sa
    }


@app.route('/teams/top_five')
def top_five():
    pl_top_five = Teams.query.filter_by(
        championship="PREMIER LEAGUE").limit(5).all()
    sa_top_five = Teams.query.filter_by(championship="SERIE A").limit(5).all()
    lg_top_five = Teams.query.filter_by(championship="LIGA").limit(5).all()
    bdl_top_five = Teams.query.filter_by(
        championship="BUNDESLIGA").limit(5).all()
    l1_top_five = Teams.query.filter_by(championship="LIGUE 1").limit(5).all()
    top_pl = []
    top_sa = []
    top_lg = []
    top_bdl = []
    top_l1 = []
    for i in range(5):
        val_pl = float(pl_top_five[i].team_value.replace(',', '.'))
        val_sa = float(sa_top_five[i].team_value.replace(',', '.'))
        val_lg = float(lg_top_five[i].team_value.replace(',', '.'))
        val_bdl = float(bdl_top_five[i].team_value.replace(',', '.'))
        val_l1 = float(l1_top_five[i].team_value.replace(',', '.'))

        pl = {
            'name': pl_top_five[i].team_name,
            'value': val_pl
        }
        sa = {
            'name': sa_top_five[i].team_name,
            'value': val_sa
        }
        lg = {
            'name': lg_top_five[i].team_name,
            'value': val_lg
        }
        bdl = {
            'name': bdl_top_five[i].team_name,
            'value': val_bdl
        }
        l1 = {
            'name': l1_top_five[i].team_name,
            'value': val_l1
        }

        top_pl.append(pl)
        top_sa.append(sa)
        top_lg.append(lg)
        top_bdl.append(bdl)
        top_l1.append(l1)
    return {
        'pl':top_pl,
        'sa':top_sa,
        'lg':top_lg,
        'bdl':top_bdl,
        'l1':top_l1
    }


if __name__ == '__main__':
    app.run(debug=True)
