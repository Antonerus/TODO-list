DROP TABLE IF EXISTS item;

CREATE TABLE item (
	id INTEGER PRIMARY KEY AUTOINCREMENT, 
	topic TEXT NOT NULL,
	created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	completed TEXT NOT NULL
);







