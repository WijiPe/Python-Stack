-- use dojo_and_ninjas_schema;
SELECT * FROM dojos;
SELECT * FROM ninjas;
INSERT INTO dojos (name, create_at, update_at) VALUES ('Noodle', NOW(), NOW());
INSERT INTO dojos (name, create_at, update_at) VALUES ('Taco', NOW(), NOW());
INSERT INTO dojos (name, create_at, update_at) VALUES ('Wiji', NOW(), NOW());
DELETE FROM dojos WHERE id IN (1,2,3);
INSERT INTO dojos (name, create_at, update_at) VALUES ('Noodle', NOW(), NOW());
INSERT INTO dojos (name, create_at, update_at) VALUES ('Taco', NOW(), NOW());
INSERT INTO dojos (name, create_at, update_at) VALUES ('Wiji', NOW(), NOW());
INSERT INTO ninjas (first_name, last_name, age, create_at, update_at, dojo_id) VALUES ('Jaja', 'Jojo', '18', NOW(), NOW(), '4');
INSERT INTO ninjas (first_name, last_name, age, create_at, update_at, dojo_id) VALUES ('Jayay', 'Jojo', '20', NOW(), NOW(), '4');
INSERT INTO ninjas (first_name, last_name, age, create_at, update_at, dojo_id) VALUES ('Joojoo', 'Jojo', '25', NOW(), NOW(), '4');
INSERT INTO ninjas (first_name, last_name, age, create_at, update_at, dojo_id) VALUES ('Kookoo', 'Kaka', '18', NOW(), NOW(), '5');
INSERT INTO ninjas (first_name, last_name, age, create_at, update_at, dojo_id) VALUES ('Kaykay', 'Kaka', '20', NOW(), NOW(), '5');
INSERT INTO ninjas (first_name, last_name, age, create_at, update_at, dojo_id) VALUES ('Kookoo', 'Kaka', '25', NOW(), NOW(), '5');
INSERT INTO ninjas (first_name, last_name, age, create_at, update_at, dojo_id) VALUES ('Papa', 'Poopoo', '18', NOW(), NOW(), '6');
INSERT INTO ninjas (first_name, last_name, age, create_at, update_at, dojo_id) VALUES ('Paypay', 'Poopoo', '20', NOW(), NOW(), '6');
INSERT INTO ninjas (first_name, last_name, age, create_at, update_at, dojo_id) VALUES ('Peepee', 'Poopoo', '25', NOW(), NOW(), '6');

SELECT * FROM ninjas WHERE dojo_id = 4;
SELECT * FROM ninjas WHERE dojo_id = 6;

SELECT * FROM ninjas ORDER BY Id DESC LIMIT 1;