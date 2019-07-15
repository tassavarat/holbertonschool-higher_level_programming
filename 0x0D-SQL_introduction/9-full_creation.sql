-- Creates second_table and adds multiple rows
-- second_table description:
--	id INT
--	name VARCHAR(256)
--	score INT
-- Script should not fail if second_table exists
-- Select and SHOW forbidden
-- Creates these records:
--	id = 1, name = “John”, score = 10
--	id = 2, name = “Alex”, score = 3
--	id = 3, name = “Bob”, score = 14
--	id = 4, name = “George”, score = 8

CREATE TABLE IF NOT EXISTS second_table (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(256), score INT);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUE (NULL, "John", "10");
INSERT INTO `second_table` (`id`, `name`, `score`) VALUE (NULL, "Alex", "3");
INSERT INTO `second_table` (`id`, `name`, `score`) VALUE (NULL, "Bob", "14");
INSERT INTO `second_table` (`id`, `name`, `score`) VALUE (NULL, "George", "8");
