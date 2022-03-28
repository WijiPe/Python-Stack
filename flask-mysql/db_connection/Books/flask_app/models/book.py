from flask_app.config.mysqlconnection import connectToMySQL


DB = "books_schema"

class Book:
    def __init__( self , data ):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL(DB).query_db(query)
        books = []

        for result in results:
            books.append(cls(result))
        return books

    @classmethod 
    def get_book_in_author(cls, data):
        query = "SELECT * FROM authors LEFT JOIN favorite ON favorite.author_id = authors.id LEFT JOIN books ON favorite.book_id = books.id WHERE authors.id = %(id)s;"
        results = connectToMySQL(DB).query_db(query, data)

        books = []

        for result in results:
            books.append(cls(result))
        return books

    @classmethod 
    def save(cls, data):
        query = "INSERT INTO books (title, num_of_pages, created_at, updated_at) VALUES (%(title)s, %(num_of_pages)s,NOW(), NOW());"
        results = connectToMySQL(DB).query_db(query, data)
        return results

    @classmethod
    def add_book_favorite(cls, data):
        query = "INSERT INTO favorite (author_id, book_id, created_at, updated_at) VALUES (%(author_id)s, %(book_id)s, NOW(), NOW())";
        results = connectToMySQL(DB).query_db(query, data)
        return results


    @classmethod
    def get_unfav_book(cls, data):
        query = "SELECT * FROM books WHERE id NOT IN (SELECT book_id FROM favorite WHERE author_id = %(id)s);"
        results = connectToMySQL(DB).query_db(query, data)
        books = []

        for result in results:
            books.append(cls(result))
        return books
