-- create a second table
CREATE TABLE IF NOT EXISTS second_table(id INT, name VARCHAR(256), score INT);
INSERT INTO second_table (id, name, score) 
VALUES
(1, 'JOHN', 10),
(2, 'ALEX', 3),
(3, 'BOB', 14),
(4, 'GEORGE', 8);
