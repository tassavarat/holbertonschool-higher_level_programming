-- Dispays the top 3 of cities temperature during July and August
-- ordered by temperature (descending)

SELECT city, avg(value) as "avg_temp"
FROM temperatures
WHERE Month = 7 OR month = 8
GROUP BY city
ORDER BY avg_temp DESC Limit 3;
