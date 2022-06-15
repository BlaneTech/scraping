const { Pool } = require("pg")

const pool = new Pool({
    user: "postgres",
    database: "data_scraping",
    password: "blanetech123",
    port: 5432,
    host: "127.0.0.1"   
})

module.exports = { pool }