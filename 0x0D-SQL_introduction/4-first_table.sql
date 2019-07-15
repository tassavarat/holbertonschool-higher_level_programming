-- Creates a table called first_table in the current database
-- first_table description:
-- 	id INT
--	name VARCHAR(256)
-- Database name will be passed as an argument of the mysql command
-- If first_table already exists, script should not fail
-- Do not use SELECT or SHOW

CREATE TABLE IF NOT EXISTS first_table (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(256));
