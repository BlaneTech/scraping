const lineNba = document.querySelector(".tbody_nba");
const lineNfl = document.querySelector(".tbody_nfl");
const lineLiga = document.querySelector(".tbody_liga")
const linePremierLeague = document.querySelector(".tbody_premier_league")
const lineSerieA = document.querySelector(".tbody_serie_a")
const lineBundesliga = document.querySelector(".tbody_bundesliga")
const lineLigue1 = document.querySelector(".tbody_ligue_1")



function showPlayers(url, tbody_line) {
  let trComp = "";
  fetch(url)
    .then((resp) => resp.json())
    .then((resp) => {
    //   console.log(resp);
      resp.forEach((player) => {
        trComp += `
                    <tr>
                        <td>${player.name}</td>
                        <td>${player.salary}</td>
                    </tr>`;
      });
      tbody_line.innerHTML = trComp;
    });
}

function showTeams(route, line) {
  let trTeam = "";
  fetch(route)
    .then((resp) => resp.json())
    .then((resp) => {
      console.log(resp);
      resp.forEach((team) => {
        trTeam += `
                    <tr>
                        <td>${team.name}</td>
                        <td>${team.market_value} mio &#8364;</td>
                    </tr>`;
      });
      line.innerHTML = trTeam;
    });
}

const NBA = "http://127.0.0.1:5000/players/NBA";
const NFL = "http://127.0.0.1:5000/players/NFL";
const LIGA = "http://127.0.0.1:5000/teams/LIGA"
const PL = "http://127.0.0.1:5000/teams/PREMIER LEAGUE"
const BDL = "http://127.0.0.1:5000/teams/BUNDESLIGA"
const L1 = "http://127.0.0.1:5000/teams/LIGUE 1"
const SERIEA = "http://127.0.0.1:5000/teams/SERIE A"



showPlayers(NBA, lineNba);
showPlayers(NFL, lineNfl);

showTeams(LIGA, lineLiga)
showTeams(PL,linePremierLeague)
showTeams(L1, lineLigue1)
showTeams(BDL, lineBundesliga)
showTeams(SERIEA, lineSerieA)
