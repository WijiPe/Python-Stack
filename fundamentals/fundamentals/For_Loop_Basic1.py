#Basic - Print all integers from 0 to 150.

for i in range (151):
    print(i)

#Multiples of Five - Print all the multiples of 5 from 5 to 1,000

for x in range (5, 1001, 5):
    print(x)

#Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".

for j in range (1,101):
    if j%10 == 0:
        print('Coding Dojo')
    elif j%5 == 0:
        print('Coding')
    else:
        print(j)

#Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.

sum = 0
for k in range(0,500001):
    if k%2 == 1:
        sum = sum + k
print (sum)

#Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.

for l in range (2018,1,-4):
        print (l)

"""
#Flexible Counter - Set three variables: lowNum, highNum, mult.
Starting at lowNum and going through highNum, 
print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, 
and mult=3, the loop should print 3, 6, 9 (on successive lines)
"""

v1 = 2
v2 = 9
v3 = 3
for m in range (v1,v2,v3):
    m += 1
    print(m)
