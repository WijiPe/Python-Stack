from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

DB = "car_dealz_schema"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.%]+@[a-zA-Z0-9.!&]+\.[a-zA-Z]+$')
PASSWORD_REGEX1 = re.compile (r'^.*[A-Z].*[0-9].*|.*[0-9].*[A-Z].*')

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def register(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password, updated_at, created_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());"
        results = connectToMySQL(DB).query_db(query, data)
        return results

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(DB).query_db(query,data)
        if results:
            one_user = cls(results[0])
            print('this is the dictionary', results[0])
            print('this is the object', one_user)
            return one_user

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(DB).query_db(query,data)
        if results:
            one_user = cls(results[0])
            print('this is the dictionary', results[0])
            print('this is the object', one_user)
            return one_user

    @staticmethod
    def is_valid(user):
        is_valid = True
        if len(user['first_name']) < 3:
            is_valid = False
            flash ('First Name must be at least 1 characters.','register')
        if len(user['last_name']) < 3:
            is_valid = False
            flash ('Last Name must be at least 1 characters.','register')
        if not EMAIL_REGEX.match(user['email']):
            flash ("Invalid email address!")
        if len(user['password']) < 8:
            is_valid = False
            flash ('Password must be at least 8 charactors.','register')
        elif not PASSWORD_REGEX1.match(user['password']):
            is_valid = False
            flash ('Password must include uppercase letter.','register')
        return is_valid    

