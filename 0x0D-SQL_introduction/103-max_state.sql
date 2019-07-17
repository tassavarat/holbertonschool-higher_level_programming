-- Displays the max temperature of each state (ordered by State name)

SELECT state, max(value) AS "max_temp"
FROM temperatures
GROUP BY state
ORDER BY state ASC;
