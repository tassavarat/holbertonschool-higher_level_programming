-- Lists all records of second_table
-- Display both score and name (in that order)
-- Ordered by top score first

SELECT
	score,
	name
FROM
	second_table
ORDER BY
	score DESC;
