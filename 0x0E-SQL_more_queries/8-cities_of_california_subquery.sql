-- inner join 
SELECT cities.id, cities.name 
FROM states 
INNER JOIN cities ON cities.state_id = states.id
ORDER BY cities.id ASC;
