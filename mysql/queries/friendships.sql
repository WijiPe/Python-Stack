-- use friendship_schema;
INSERT INTO users (first_name, last_name, create_at, update_at) 
VALUES ('Saifa', 'Axie', NOW(), NOW()),
('K', 'Axie', NOW(), NOW()),
('C', 'Axie', NOW(), NOW()),
('Ball', 'Axie', NOW(), NOW()),
('Aoom', 'Axie', NOW(), NOW()),
('Fluke', 'Axie', NOW(), NOW());
SELECT * FROM users; 

INSERT INTO friendships (user_id, friend_id, create_at, update_at)
VALUE ('1', '3', NOW(), NOW()), ('1', '5', NOW(), NOW()), ('1', '7', NOW(), NOW()),
('3', '1', NOW(), NOW()), ('3', '4', NOW(), NOW()), ('3', '6', NOW(), NOW()),
('4', '3', NOW(), NOW()), ('4', '6', NOW(), NOW()), ('5', '4', NOW(), NOW()),
('6', '1', NOW(), NOW()), ('6', '7', NOW(), NOW()), ('7', '3', NOW(), NOW()),
('7', '4', NOW(), NOW());

SELECT * FROM friendships; 

SELECT users.first_name as name, users.last_name as last_name, users2.first_name as friend_first_name, users2.last_name as friend_last_name FROM users
JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users as users2 ON users2.id = friendships.friend_id;

SELECT users.first_name as name, users.last_name as last_name, users2.first_name as friend_first_name, users2.last_name as friend_last_name FROM users
JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users as users2 ON users2.id = friendships.friend_id
WHERE user_id = 1 OR friend_id = 1;

SELECT COUNT(users.first_name) as number_of_friends,  users.first_name FROM users
JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users as users2 ON users2.id = friendships.friend_id
GROUP BY users.first_name
ORDER BY number_of_friends DESC
LIMIT 1;

SELECT users2.first_name as friend_first_name FROM users
JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users as users2 ON users2.id = friendships.friend_id
WHERE users.id = 3
ORDER BY users2.first_name;




