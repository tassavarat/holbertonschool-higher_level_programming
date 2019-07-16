-- Lists the number of records with the same score in the table second_table
-- of the specified database
-- Results should display:
-- 	score
--	number of records for this score with the label number
-- Sorted in descending order of number of records

SELECT
	score, COUNT(*) 'number'
FROM
	second_table
GROUP BY
	score
ORDER BY
	score DESC;
