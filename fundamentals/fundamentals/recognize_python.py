num1 = 42 #variable declaration num1 is 42
num2 = 2.3 #variable declaration num2 is 2.3
boolean = True #Boolean
string = 'Hello World' #Strings Hello World
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] 
"""
Data Type: Composite: List of pizza_toppings: 'Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'
"""
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} 
"""
Data Type: Composite: Dictionary of person: 'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding'

Boolean: False

"""
fruit = ('blueberry', 'strawberry', 'banana') 
"""
Data Type: Composite: Tuple of fruit: blueberry, strawberry, banana
"""

print(type(fruit)) #result is: ('blueberry', 'strawberry', 'banana') 
print(pizza_toppings[1]) #result is: Sausage
pizza_toppings.append('Mushrooms') #result is: ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives', 'mushroom'] 
print(person['name']) #result is: John
person['name'] = 'George' #result is person = {'name': 'George', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
person['eye_color'] = 'blue' # AttributeError: 'tuple' object has no attribute 'append'
print(fruit[2]) #result is: banana
"""
result is: 'blueberry', 'strawberry', 'banana',
'blueberry', 'strawberry', 'banana'

"""

if num1 > 45:
    print("It's greater")
else:
    print("It's lower")
"""
Conditional: num1 < 45
result is: It's lower

"""


if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

"""
conditional: length of the string is greater than 5 but less than 15
result is: Just right!


"""


for x in range(5):
    print(x)
'''
range of 5 is 0,1,2,3,4
'''
for x in range(2,5):
    print(x)
'''
range 2,5 is 2,3,4

'''

for x in range(2,10,3):
    print(x)

'''
range 2,10,3 is 2,3,4,5,6,7,8,9

'''

x = 0
while(x < 5):
    print(x)
    x += 1
"""
while loop 
while x=0 and x<5 x=0
0+1 = 1
1+1 = 2
2+1 = 3
3+1 = 4
4+1 = 5 but 5=5 

so the result is 0,1,2,3,4


"""


pizza_toppings.pop() 
'''
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] 
after pop
pizza_toppings.pop() ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese']

'''
pizza_toppings.pop(1)
'''
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese']
after pop(1)
pizza_toppings = ['Pepperoni', 'Jalepenos', 'Cheese']

'''



print(person) # person = {'name': 'George', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} 
person.pop('eye_color') #TypeError: 'tuple' object does not support item assignment
print(person) # person = {'name': 'George', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} 

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break
'''
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese'] 

'''


def print_hello_ten_times():
    for num in range(10):
        print('Hello')
'''
function print_hello_ten_times:
'Hello', 'Hello' , 'Hello' , 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello' 


'''

print_hello_ten_times()
'''
'Hello', 'Hello' , 'Hello' , 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello'

'''



def print_hello_x_times(x):
    for num in range(x):
        print('Hello')


print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')
'''
'Hello', 'Hello' , 'Hello' , 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello'
'''

print_hello_x_or_ten_times()
'''
'Hello', 'Hello' , 'Hello' , 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello'
'''
print_hello_x_or_ten_times(4)
'''
'Hello', 'Hello' , 'Hello' , 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello'
'Hello', 'Hello' , 'Hello' , 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello'
'Hello', 'Hello' , 'Hello' , 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello'
'Hello', 'Hello' , 'Hello' , 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello'

'''


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)