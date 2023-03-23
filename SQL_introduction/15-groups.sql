--list recods with the same score
SELECT score, COUNT(*) as number
FROM second_table
GROUP BY score;
