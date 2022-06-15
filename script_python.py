from bs4 import BeautifulSoup
from requests import get
from models.database import *

NFL = "https://www.marqueur.com/football/stats/nfl/salaries.php?a=163&e=0&p=0&o="
NBA = "https://www.marqueur.com/basketball/stats/nba/salaries.php?o=1"

def sport_scraper(url, tag_name, selector_name,tag_salary,selector_salry):
    req = get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    players_name= soup.find_all(tag_name, class_=selector_name, limit=300)
    players_salary = soup.find_all(tag_salary, class_=selector_salry, limit=300)

    players=[]
    for data in range(len(players_salary)):
        str_salary = players_salary[data].text
        salary = " ".join(str_salary.split("\xa0"))
        players_data={
            'name' : players_name[data].text,
            'salary' : salary
            }
        players.append(players_data)
    return players

nba_players=sport_scraper(NBA,"a", "t14b_n", "td","t12nr")

nfl_players = sport_scraper( NFL,"div","t10b_n","td","t10nr")

for nfl_player in nfl_players:
    nfl = Players(player_name=nfl_player.get('name'), player_salary=nfl_player.get('salary'), championship="NFL" )
    db.session.add(nfl)

for nba_player in nba_players:
    nba = Players(player_name=nba_player.get('name'), player_salary=nba_player.get('salary'), championship="NBA" )
    db.session.add(nba)

db.session.commit()


