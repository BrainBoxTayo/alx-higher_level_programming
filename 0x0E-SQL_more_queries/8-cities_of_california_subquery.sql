-- cities of california
SELECT cities.id, cities.name
FROM cities, states
WHERE cities.state_id = (SELECT id FROM states WHERE name = 'California')
AND states.name = 'California'
ORDER BY cities.id ASC;
