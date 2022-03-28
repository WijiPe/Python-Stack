from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

DB = "login_and_registration_schema"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.%]+@[a-zA-Z0-9.!&]+\.[a-zA-Z]+$')
PASSWORD_REGEX1 = re.compile (r'^.*[A-Z].*')
PASSWORD_REGEX2 = re.compile (r'^.*[0-9].*')
class Registration:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.gender = data['gender']
        self.confession = data['confession']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def register(cls, data):
        query = "INSERT INTO registration (first_name, last_name, email, password, gender, confession, updated_at, created_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, %(gender)s,  %(confession)s, NOW(), NOW());"
        results = connectToMySQL(DB).query_db(query, data)
        return results


    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM registration WHERE email = %(email)s;"
        result = connectToMySQL(DB).query_db(query,data)
        if result:
            return cls(result[0])


    @staticmethod
    def is_valid(registration):
        is_valid = True
        if len(registration['first_name']) < 1:
            is_valid = False
            flash ('First Name must be at least 1 characters.','register')
        if len(registration['last_name']) < 1:
            is_valid = False
            flash ('Last Name must be at least 1 characters.','register')
        if not EMAIL_REGEX.match(registration['email']):
            flash ("Invalid email address!")
        if len(registration['password']) < 8:
            is_valid = False
            flash ('Password must be at least 8 charactors.','register')
        elif not PASSWORD_REGEX1.match(registration['password']):
            is_valid = False
            flash ('Password must include uppercase letter.','register')
        elif not PASSWORD_REGEX2.match(registration['password']):
            is_valid = False
            flash ('Password must include number.','register')
        if 'gender' not in registration:
            is_valid = False
            flash ('Please select the gender','register')
        if 'confession' not in registration:
            is_valid = False
            flash ('Please select the confession','register')
        return is_valid    
