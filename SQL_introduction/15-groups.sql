--list recods with the same score
SELECT score, COUNT(*) as count
FROM second_table
GROUP BY score;
