from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.user import User


DB = "car_dealz_schema"

class Car:
    def __init__( self , data ):
        self.id = data['id']
        self.model = data['model']
        self.make = data['make']
        self.year = data['year']
        self.price = data['price']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.sold = data['sold']
        if 'first_name' in data:
            self.first_name = data['first_name']
        
        
        self.users = []

    @classmethod
    def get_cars_show_owner(cls):
        query = "SELECT * FROM cars JOIN users ON users.id = cars.user_id;"
        results = connectToMySQL(DB).query_db(query)
        print(results)
        car = []
        for result in results:
            car.append(cls(result))
        return car


    @classmethod
    def add_car(cls,data):
        query = """
            INSERT INTO cars (model, make, year, price, description, created_at, updated_at, user_id) 
            VALUE (%(model)s,%(make)s, %(year)s, %(price)s, %(description)s, NOW(), NOW(), %(user_id)s);
        """
        results = connectToMySQL(DB).query_db(query,data)
        return results

    @classmethod
    def get_one_car(cls,data):
        query = "SELECT * FROM cars WHERE id = %(id)s;"
        results = connectToMySQL(DB).query_db(query,data)
        return cls(results[0])


    @classmethod
    def edit_car(cls,data):
        query = """
            UPDATE cars SET model = %(model)s, make=%(make)s, price=%(price)s, description=%(description)s, year=%(year)s, 
            created_at =NOW(), updated_at= NOW() WHERE id = %(id)s;
        """
        results = connectToMySQL(DB).query_db(query,data)
        return results

    @classmethod
    def delete_car(cls,data):
        query = "DELETE FROM cars WHERE id =  %(id)s;"
        results = connectToMySQL(DB).query_db(query,data)
        return results
    
    @classmethod
    def get_one_car_show_owner(cls,data):
        query = "SELECT * FROM cars LEFT JOIN users ON cars.user_id = users.id WHERE cars.id = %(id)s;"
        results = connectToMySQL(DB).query_db(query,data)
        car = cls(results[0])
        return car

    @classmethod
    def get_car_from_owner(cls,data):
        query = "SELECT * FROM cars LEFT JOIN users ON users.id = cars.user_id WHERE users.id = %(id)s;"
        results = connectToMySQL(DB).query_db(query,data)
        
        car = cls(results[0])

        for row_from_db in results:
            seller_data = {
                "id" : row_from_db["users.id"],
                "first_name" : row_from_db["first_name"],
                "last_name" : row_from_db["last_name"],
                "email" : row_from_db["email"],
                "password" : row_from_db["password"],
                "created_at" : row_from_db["users.created_at"],
                "updated_at" : row_from_db["users.updated_at"]
            }
            car.users.append(User(seller_data))
        return car


    @staticmethod
    def is_valid(car):
        is_valid = True
        if len(car['model']) < 2:
            is_valid = False
            flash ('Model must be at least 3 characters.','name')
        if len(car['description']) < 3:
            is_valid = False
            flash ('Description must be at least 3 characters.','name')
        if len(car['make']) < 3:
            is_valid = False
            flash ('Make must be at least 3 charactors.','name')
        if 'year' not in car:
            is_valid = False
            flash ('Please select the year','name')
        if 'price' not in car:
            is_valid = False
            flash ('Please select the price','name')
        return is_valid

    @classmethod
    def purchase_car(cls,data):
        query = """
            UPDATE cars SET user_id = %(user_id)s, sold=1 WHERE id = %(id)s;
        """
        results = connectToMySQL(DB).query_db(query,data)
        return results

    @classmethod 
    def get_last(cls):
        query = "SELECT * FROM cars ORDER BY id DESC LIMIT 1;"
        results = connectToMySQL(DB).query_db(query)
        cars = []
        for car in results:
            cars.append( cls(car) )
        return cars