-- use book_schema;
SELECT * FROM authors;
-- ALTER TABLE authors ADD name VARCHAR(25) NULL ;
INSERT INTO authors (name, create_at, update_at) VALUES ('Jane Austen', NOW(), NOW());
INSERT INTO authors (name, create_at, update_at) VALUES ('Emily Dickinson', NOW(), NOW());
INSERT INTO authors (name, create_at, update_at) VALUES ('Fyodor Dostoevsky', NOW(), NOW());
INSERT INTO authors (name, create_at, update_at) VALUES ('William Shakespeare', NOW(), NOW());
INSERT INTO authors (name, create_at, update_at) VALUES ('Lau Tzu', NOW(), NOW());
INSERT INTO books (title, num_of_pages, create_at, update_at) VALUES ('C Sharp', 30, NOW(), NOW());
INSERT INTO books (title, num_of_pages, create_at, update_at) VALUES ('Java', 40, NOW(), NOW());
INSERT INTO books (title, num_of_pages, create_at, update_at) VALUES ('Python', 50, NOW(), NOW());
INSERT INTO books (title, num_of_pages, create_at, update_at) VALUES ('PHP', 60, NOW(), NOW());
INSERT INTO books (title, num_of_pages, create_at, update_at) VALUES ('Ruby', 70, NOW(), NOW());
SELECT * FROM books;

UPDATE books SET title = 'C#' WHERE id = 1;
UPDATE authors SET name = 'Bill' WHERE id = 4;

SELECT * FROM favorite;
INSERT INTO favorite (author_id, book_id, create_at, update_at) VALUES (1, 1, NOW(), NOW());
INSERT INTO favorite (author_id, book_id, create_at, update_at) VALUES (1, 2, NOW(), NOW());
INSERT INTO favorite (author_id, book_id, create_at, update_at) VALUES (2, 1, NOW(), NOW());
INSERT INTO favorite (author_id, book_id, create_at, update_at) VALUES (2, 2, NOW(), NOW());
INSERT INTO favorite (author_id, book_id, create_at, update_at) VALUES (2, 3, NOW(), NOW());
INSERT INTO favorite (author_id, book_id, create_at, update_at) VALUES (3, 1, NOW(), NOW());
INSERT INTO favorite (author_id, book_id, create_at, update_at) VALUES (3, 2, NOW(), NOW());
INSERT INTO favorite (author_id, book_id, create_at, update_at) VALUES (3, 3, NOW(), NOW());
INSERT INTO favorite (author_id, book_id, create_at, update_at) VALUES (3, 4, NOW(), NOW());
INSERT INTO favorite (author_id, book_id, create_at, update_at) VALUES (4, 1, NOW(), NOW());
INSERT INTO favorite (author_id, book_id, create_at, update_at) VALUES (4, 2, NOW(), NOW());
INSERT INTO favorite (author_id, book_id, create_at, update_at) VALUES (4, 3, NOW(), NOW());
INSERT INTO favorite (author_id, book_id, create_at, update_at) VALUES (4, 4, NOW(), NOW());
INSERT INTO favorite (author_id, book_id, create_at, update_at) VALUES (4, 5, NOW(), NOW());

SELECT * FROM books 
JOIN favorite ON book_id = favorite.book_id
JOIN authors ON author_id = favorite.author_id
WHERE book_id = 3;

DELETE FROM favorite WHERE id = 5 AND author_id = 2;
INSERT INTO favorite (author_id, book_id, create_at, update_at) VALUES (5, 2, NOW(), NOW());
SELECT * FROM authors
JOIN favorite ON author.id = favorite.author_id
JOIN books ON book.id = favorite.book_id
WHERE authors.id = 3;
SELECT * FROM books 
JOIN favorite ON books.id = favorite.book_id
JOIN authors ON authors.id = favorite.author_id
WHERE book_id = 5;