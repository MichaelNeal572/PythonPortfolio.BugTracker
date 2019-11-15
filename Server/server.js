const http = require('http');
const sqlite3 = require('sqlite3').verbose();

class DBHandler{
	constructor(){

	}
	database_connect(){
	this.db = new sqlite3.Database(':memory:', (err) => {
		if (err) {
			return console.error(err.message);
		}
		});
	}

	database_disconnect(){
		this.db.close((err) =>{
		if(err) {
			return console.error(err.message);
		}
		console.log('Close the database connection')
		});
	}

}

class HttpRequestHandler{
	constructor(){
		this.hostname = '127.0.0.1';
		this.port = 3000;
	}

	start(){
		const server = http.createServer((req, res) => {
			res.statusCode = 200;
			res.setHeader('Content-Type', 'text/plain');
			res.end('Hello World\n');
		});

		server.listen(this.port, this.hostname, () => {
			console.log(`Server running at http://${this.hostname}:${this.port}/`);
		});
	}
}

class Controller{
	constructor(){
		this.dbh = new DBHandler();
		this.hrh = new HttpRequestHandler();
	}
	start(){
		this.dbh.database_connect();
		this.hrh.start();
		console.log('test')
	}
}

main = new Controller()
main.start()



