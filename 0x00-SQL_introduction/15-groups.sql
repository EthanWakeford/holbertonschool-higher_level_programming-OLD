-- lists the number of recors with same score
SELECT SCORE, COUNT(score) AS number
    FROM second_table 
    GROUP BY score
    ORDER BY COUNT(score) Desc;
