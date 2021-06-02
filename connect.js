var pg = require('pg');

var connectionString = "postgres://regiapriandi:sinheul24@192.168.10.105:5432/tubes";

var pgClient = new pg.Client(connectionString);

pgClient.connect();


var query = pgClient.query("SELECT * FROM emas");

query.on("row", function(row,result){

result.addRow(row);

});

