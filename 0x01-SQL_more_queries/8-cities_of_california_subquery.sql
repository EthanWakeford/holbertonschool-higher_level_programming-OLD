-- lists all cities of california that can be found in database
SELECT id, name
FROM cities WHERE
state_id IN (
    SELECT id
    FROM states
    WHERE NAME = 'california'
) ORDER BY id ASC;
