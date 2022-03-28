from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

DB = "email_address_schema"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.%]+@[a-zA-Z0-9.!&]+\.[a-zA-Z]+$')

class Email:
    def __init__( self , data ):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def add_email(cls, data):
        query = "INSERT INTO email_address (email, created_at, updated_at) VALUES (%(email)s, NOW(), NOW());"
        results = connectToMySQL(DB).query_db(query, data)
        return results

    @classmethod 
    def get_all(cls):
        query = "SELECT * FROM email_address;"
        results = connectToMySQL(DB).query_db(query)
        return results
    
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM email_address WHERE id = %(id)s ;"
        results = connectToMySQL(DB).query_db(query, data)
        return results
    
    @classmethod 
    def get_duplicate(cls, data):
        query = "SELECT * FROM email_address WHERE email = %(email)s;"
        results = connectToMySQL(DB).query_db(query, data)
        return results

    @staticmethod
    def is_valid(email):
        is_valid = True
        if not EMAIL_REGEX.match(email['email']):
            flash ("Invalid email address!")
        return is_valid

