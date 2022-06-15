let puppeteer = require('puppeteer')
const { pool } = require("./db")


let links = {
    PL: "https://www.transfermarkt.fr/premier-league/marktwerteverein/wettbewerb/GB1",

    L1 : "https://www.transfermarkt.fr/ligue-1/marktwerteverein/wettbewerb/FR1",
    SA : "https://www.transfermarkt.fr/serie-a/marktwerteverein/wettbewerb/IT1",
    LIGA : "https://www.transfermarkt.fr/laliga/marktwerteverein/wettbewerb/ES1",
    BDL : "https://www.transfermarkt.fr/bundesliga/marktwerteverein/wettbewerb/L1"
}

async function getFootTeamData(url, competition){
    const browser = await puppeteer.launch()
    const page = await browser.newPage()
    await page.goto(url)

    let data = await page.evaluate(()=>{

        let listOfTeam= new Array()
        const tab = document.querySelector(".responsive-table")
        let champs = tab.querySelectorAll(".rechts.hauptlink")
        champs.forEach(element => {
            let data_team={}
            data_team.teamName = element.lastElementChild.title
            let val = element.lastElementChild.textContent.split('mio. €')
            data_team.teamValue = val[0].trim()
            
            listOfTeam.push(data_team)
        });
        return listOfTeam
    })

    for (const element of data) {
        const elt = element;
        await pool.query(`INSERT INTO teams (team_name, team_value, championship) VALUES  ('${elt.teamName}', '${elt.teamValue}', '${competition.toUpperCase()}') ON CONFLICT DO NOTHING; `)
    }
    await browser.close()
}


let championships = ["PL", "SA", "LIGA", "L1", "BDL"]
let competition =""
for (const champ of championships) {
    if (champ === "PL") {
        competition = "Premier League"
    }else if (champ === "SA") {
        competition = "Serie A"
    }else if (champ === "LIGA") {
        competition = "Liga"
    }else if (champ === "BDL") {
        competition = "Bundesliga"
    }else{
        competition = "Ligue 1"

    }
    getFootTeamData(links[champ], competition)

}
