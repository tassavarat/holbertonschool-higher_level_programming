-- Lists all records with a score >= 10 in table second_table
-- Display score and name in that order
-- Records should be in descending order

SELECT
	score,
	name
FROM
	second_table
WHERE
	score >= 10
ORDER BY
	score DESC;
