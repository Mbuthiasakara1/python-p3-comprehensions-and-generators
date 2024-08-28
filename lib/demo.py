# normal for in iteration
squared_minus_one =list()
for n in range (1,11):
    squared_minus_one.append((n ** 2) - 1)
print(squared_minus_one)   

# Using list compreshension
squared_minus_one=[(n**2)-1 for n in range(1,11)]
print(squared_minus_one)

# syntax for list comprehension 
# new_list=[optional_operation (item)for item in old_list if optional_condition == True] 


# Generator Expressions
# are very similar to list comprehensions ,They use almost identical syntax to produce iterable objects in a single line

# example 1

my_list = range(1,4)

squared_list=[n**2 for n in my_list]
# print(squared_list)

squared_generator=(n**2 for n in my_list)
print(squared_list)


def list_com():
    for n in squared_list:
        print(n)
list_com() 

def list_gen():
    for n in squared_generator:
        print(n)
list_gen()        