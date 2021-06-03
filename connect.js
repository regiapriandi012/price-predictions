const { Pool } = require('pg')
const pool = new Pool({
  user: 'regiapriandi',
  host: '912.168.10.105',
  database: 'tubes',
  password: 'sinheul24',
  port: 5432,
})
pool.query('SELECT * FROM emas', (err, res) => {
  console.log(err, res) 
  pool.end() 
})