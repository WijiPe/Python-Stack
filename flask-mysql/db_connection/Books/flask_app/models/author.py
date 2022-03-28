from flask_app.config.mysqlconnection import connectToMySQL

DB = "books_schema"

class Author:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod 
    def save(cls, data):
        query = "INSERT INTO authors (name, created_at, updated_at) VALUES (%(name)s,NOW(), NOW());"
        results = connectToMySQL(DB).query_db(query, data)
        return results

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL(DB).query_db(query)
        author = []
        for u in results:
            author.append( cls(u) )
        return author

    @classmethod
    def get_author_in_book(cls, data):
        query = "SELECT * FROM books LEFT JOIN favorite ON favorite.book_id = books.id LEFT JOIN authors ON favorite.author_id = authors.id WHERE books.id = %(id)s ;"
        results = connectToMySQL(DB).query_db(query, data)
        author = []
        for u in results:
            author.append( cls(u) )
        return author

    @classmethod
    def get_author(cls, data):
        query = "SELECT * FROM authors WHERE id = %(id)s;"
        results = connectToMySQL(DB).query_db(query, data)
        return cls(results[0])
    
    @classmethod
    def get_unfav_author(cls, data):
        query = "SELECT * FROM authors WHERE id NOT IN (SELECT author_id FROM favorite WHERE book_id = %(id)s);"
        results = connectToMySQL(DB).query_db(query, data)
        author = []
        for u in results:
            author.append( cls(u) )
        return author

