from flask_app.config.mysqlconnection import connectToMySQL

DB = "dojos_and_ninjas_schema"
# model the class after the friend table from our database
class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod 
    def save(cls, data):
        query = "INSERT INTO ninjas (dojo_id, first_name, last_name, age) VALUES (%(dojo_id)s,%(first_name)s, %(last_name)s,%(age)s);"
        results = connectToMySQL(DB).query_db(query, data)
        return results
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DB).query_db(query)
        # Create an empty list to append our instances of friends
        return results

    @classmethod
    def get_last(cls):
        query = "SELECT * FROM ninjas ORDER BY id DESC limit 1;"
        return connectToMySQL(DB).query_db(query)[0]

    # @classmethod 
    # def get_one(cls, data):
    #     query = "SELECT * FROM ninjas JOIN dojos ON dojos.id = ninjas.dojo_id WHERE dojos.id = %{id}s;"
    #     results = connectToMySQL(DB).query_db(query, data)
    #     return results[0]
