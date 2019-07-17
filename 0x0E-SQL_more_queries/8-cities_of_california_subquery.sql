-- Lists all cities of California that can be found in the database
-- states table contains only one record where name / California
-- Results must be sorted in ascending order by cities.id
-- JOIN forbidden

SELECT id, name
FROM cities 
WHERE state_id = 1;
