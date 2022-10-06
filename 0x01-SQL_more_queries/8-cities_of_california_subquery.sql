-- lists all cities of california that can be found in database
SELECT id, name
FROM cities WHERE
state_id IN (
    SELECT id
    FROM states
    where name = 'california'
) ORDER BY id ASC;
