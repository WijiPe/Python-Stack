# import the function that will return an instance of a connection
from flask_app.models.ninja import Ninja
from flask_app.config.mysqlconnection import connectToMySQL

DB = "dojos_and_ninjas_schema"
# model the class after the friend table from our database
class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.ninja = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DB).query_db(query)
        # Create an empty list to append our instances of friends
        dojos = []
        # Iterate over the db results and create instances of friends with cls.
        for u in results:
            dojos.append( cls(u) )
        return dojos

    @classmethod 
    def get_one(cls, data):
        query = "SELECT * FROM  dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL(DB).query_db(query, data)

        dojo = cls (results[0])
        for row_from_db in results:

            ninja_data = {
                "id" : row_from_db['ninjas.id'],
                "first_name" : row_from_db['first_name'],
                "last_name" : row_from_db['last_name'],
                "age" : row_from_db['age'],
                "created_at" : row_from_db['created_at'],
                "updated_at" : row_from_db['updated_at'],
            }
            dojo.ninja.append(Ninja(ninja_data))
        return dojo
    
    @classmethod 
    def save(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        results = connectToMySQL(DB).query_db(query, data)
        return results

    # @classmethod
    # def get_dojo(cls, data):
    #     query = "SELECT * FROM dojos WHERE id = %(id)s;"
    #     results = connectToMySQL(DB).query_db(query, data)
    #     return results[0]

    # @classmethod 
    # def get_one(cls, data):
    #     query = "SELECT * FROM ninjas WHERE id = %(id)s;"
    #     results = connectToMySQL(DB).query_db(query, data)
    #     return results[0]

    # Now we use class methods to query our database
    # @classmethod
    # def get_all(cls):
    #     query = "SELECT * FROM ninjas;"
    #     # make sure to call the connectToMySQL function with the schema you are targeting.
    #     results = connectToMySQL(DB).query_db(query)
    #     # Create an empty list to append our instances of friends
    #     ninjas = []
    #     # Iterate over the db results and create instances of friends with cls.
    #     for u in results:
    #         ninjas.append( cls(u) )
    #     return ninjas

    # 


    # @classmethod 
    # def update(cls, data):
    #     query = "UPDATE users SET first_name =%(first_name)s, last_name = %(last_name)s, email = %(email)s, updated_at = NOW() WHERE id = %(id)s;"
    #     print(query, data)
    #     return connectToMySQL('users_schema').query_db(query, data)
        

    # @classmethod 
    # def delete(cls, data):
    #     query = "DELETE FROM users WHERE id = %(id)s;"
    #     return connectToMySQL('users_schema').query_db(query, data)

    # @classmethod
    # def get_last(cls):
    #     query = "SELECT * FROM users ORDER BY id DESC limit 1;"
    #     return connectToMySQL('users_schema').query_db(query)[0]
