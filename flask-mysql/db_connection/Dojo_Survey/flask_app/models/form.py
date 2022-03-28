from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

DB = "dojo_survey_schema"

class Form:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.pet = data['pet']
        self.favorite_activity = data['favorite_activity']
        self.comment = data['comment']
        self.ps = data['ps']
        self.confession = data['confession']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def add_info(cls, data):
        query = "INSERT INTO form (name, pet, favorite_activity, comment, ps, confession, updated_at, created_at) VALUES (%(name)s, %(pet)s, %(favorite_activity)s, %(comment)s,%(ps)s, %(confession)s, NOW(), NOW());"
        results = connectToMySQL(DB).query_db(query, data)
        return results

    @classmethod 
    def get_last(cls):
        query = "SELECT * FROM form ORDER BY id DESC LIMIT 1;"
        results = connectToMySQL(DB).query_db(query)
        return results[0]

    @staticmethod
    def is_valid(form):
        is_valid = True
        if len(form['name']) < 1:
            is_valid = False
            flash ('Name must be at least 1 characters.')
        if form['pet'] == "...":
            is_valid = False
            flash ('Must choose a pet.')
        if form['favorite_activity'] == "...":
            is_valid = False
            flash ('Must choose favorite_activity.')
        if len(form['comment']) < 5:
            is_valid = False
            flash ('Comment must be at least 1 characters.')
        if 'ps' not in form:
            is_valid = False
            flash ('Please select..')
        if 'confession' not in form:
            is_valid = False
            flash ('Please select..')
        return is_valid    

