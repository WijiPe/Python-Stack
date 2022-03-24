-- use twitter;

-- gets all users
SELECT * FROM users;

-- get all users first_name, last_name
SELECT first_name, last_name FROM users;

-- get users with id of 3?
SELECT * FROM users WHERE id = 3;

-- get users with fisrt_name Kobe?
SELECT * FROM users WHERE first_name IN ('Kobe', 'Allen');

-- all users sort by alpha
SELECT * FROM users ORDER BY first_name;

-- all first two users in alphabetical order
SELECT * FROM users ORDER BY first_name DESC LIMIT 2 OFFSET 2;

UPDATE users SET first_name ='Jane' WHERE id = 1;
SELECT * FROM users WHERE id = 1;

SELECT * FROM users;

INSERT INTO users (first_name, last_name, handle, birthday, created_at, updated_at) VALUES ('JANE', 'PANCAKE', 'BOSS', '1978-08-23' , NOW(), NOW());

DELETE FROM users WHERE id = 11;

SET SQL_SAFE_UPDATES = 0;
DELETE FROM users WHERE last_name = 'PANCAKE';


