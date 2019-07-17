-- Creates the database hbtn_0d_usa and the table cities
-- cities description:
--	id INT unique, auto generated, can’t be null and is a primary key
--	state_id INT, not null and must be a FOREIGN KEY that references id of states
--	name VARCHAR(256) can’t be null
-- Should not fail if database or table exists

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities
(
	id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
       	FOREIGN KEY (state_id) REFERENCES states(id)
);
