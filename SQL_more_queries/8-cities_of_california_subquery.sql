-- LIST ALL name cities of cali
USE hbtn_0d_usa
SELECT name
FROM cities
WHERE state_id = 1
ORDER BY name ASC;
