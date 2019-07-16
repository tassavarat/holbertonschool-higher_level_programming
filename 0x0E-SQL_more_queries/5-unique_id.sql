-- Creates the table unique_id
-- unique_id description
--	id INT with default value 1 and unique
-- 	name VARCHAR(256)
-- Script should not fail if table exists

CREATE TABLE IF NOT EXISTS unique_id
(
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
);
