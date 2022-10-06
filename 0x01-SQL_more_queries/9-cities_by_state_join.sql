-- lists all cities in database
SELECT id, name, state_id IN (states) AS name FROM cities;
