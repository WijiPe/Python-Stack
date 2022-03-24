-- use users_schema;
INSERT INTO users (first_name, last_name, email, create_at, update_at) VALUES ('Noodle', 'Stevens', 'noodle@gmail.com', NOW(), NOW());
INSERT INTO users (first_name, last_name, email, create_at, update_at) VALUES ('Wiji', 'Stevens', 'wiji@gmail.com', NOW(), NOW());
INSERT INTO users (first_name, last_name, email, create_at, update_at) VALUES ('Taco', 'Stevens', 'taco@gmail.com', NOW(), NOW());
INSERT INTO users (first_name, last_name, email, create_at, update_at) VALUES ('Kit', 'Stevens', 'kit@gmail.com', NOW(), NOW());
SELECT * FROM users;
SELECT email FROM users WHERE id = 1;

SELECT * FROM users WHERE email = 'noodle@gmail.com';
SELECT * FROM users WHERE id = 5;
UPDATE users SET last_name = 'PANCAKES' WHERE id = 4;
DELETE FROM users WHERE id = 2;
SELECT * FROM users ORDER BY first_name DESC;

SELECT * FROM users;
