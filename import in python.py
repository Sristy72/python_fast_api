from cmath import sqrt

from imports.grade_average_service import calculate_homework
import random
import math

homework_assignment_grades ={
    'homework 1' : 86,
    'homework 2' : 90,
    'homework 3' : 91,
}



calculate_homework(homework_assignment_grades)

types_of_drinks = ['soda', 'water', 'coffee', 'tea']
print(random.choice(types_of_drinks))

print(random.randint(0, 10))

print(math.sqrt(79))