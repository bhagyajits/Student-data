# Write a python program to reverse a string with out using inbuilt function ?

'''def rev_string(input_string):
    rev_string = ""
    for i in range(len(input_string) - 1, -1, -1):
        rev_string += input_string[i]
    return rev_string

input_string = input("Enter a string: ")
rev_string = rev_string(input_string)
print("Reversed string:", rev_string)'''

# Write a Python program to find the unique number in list with out using inbuilt function?

'''def unique_num(list1):
    unique_list = []
    for i in list1:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list

list1 = [76, 43, 75, 76, 92, 46, 46, 43, 643, 683, 642]

print(unique_num(list1))'''

# WAP in list comprehension for create even number 1 to 50?

'''even_numbers = [i for i in range(1, 51) if i % 2 == 0]
print(even_numbers)'''

# Write Fibonacci series first 15 number using for and while loop– write two program.
'''def fibonacci_for(n):
    x = 0
    y = 1
    fibonacci_series = []
    for i in range(n):
        fibonacci_series.append(x)
        x, y = y, x + y
    return fibonacci_series

print(fibonacci_for(15))
def fibonacci_while(n):
    x = 0
    y = 1
    fibonacci_series = []
    while n > 0:
        fibonacci_series.append(x)
        x, y = y, x + y
        n -= 1
    return fibonacci_series
print(fibonacci_while(15))'''

# Write a prime number without using inbuilt function

'''def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
if is_prime(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")'''

# li1 = [1,2,3,4]
# Li2 = [‘A’,’B’,’C’,’D’]
# Output:- {1:’A’,2:’B’,3:’C’,4:’D}


'''li1 = [1, 2, 3, 4]
li2 = ['A', 'B', 'C', 'D']

dict = {li1[i]: li2[i] for i in range(min(len(li1), len(li2)))}

print(dict)'''

# Li = [a, b, c, a, b, c, a, b, c]
# Output: - {‘a’:3,’b’:3,’c’:3}

'''Li = ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']

dict = {}
for item in Li:
    if item in dict:
        dict[item] += 1
    else:
        dict[item] = 1
print(dict)'''

# Explain Logical Operators in Python
'''Python's logical operators are essential for working with boolean data because they enable the execution of logical operations. 
In Python, Logical operators are used on conditional statements.

There are 3 types of Logical Operaters.

and = Returns True if both statements are true
or = Returns True if one of the statements is true
not = Reverse the result, returns False if the result is true.'''

# Python Program to find largest element in an list
'''In Python, the membership operators are used to test whether a value exists within a sequence or not.
such as a list, tuple, string, or dictionary.
if a sequence is not present in any object, We get the output in the form of a boolean value that is True or False.

There are two types of operaters
1. in	By using the in operator, If the specified variable/literal is found, it will return true, otherwise, it will return false.
2. not in	By using the, not in operator, If the specified variable/literal is found, it will return false, otherwise it will return true.'''

# Python Program to find largest element in an list

'''def lar(list):
    lar = list[0]
    for i in list:
        if i > lar:
            lar = i
    return lar

list = [78, 92, 543, 59851, 2, 98, 87521, 933218]
print("Largest element is:", lar(list))'''

# slicing

'''Name = 'Subhas Deshmukh'
DOB = '22/12/1997'

name_first = Name[:4]
dob_last = DOB[-4:]
password = name_first + dob_last

print("Password:", password)'''

# Write lambda expression using map , filter and reduce

'''my_list = [13, 42, 63, 74, 55]
doubled_list = list(map(lambda x: x * 2, my_list))
print(doubled_list)

my_list = [43, 53, 71, 78, 97, 92]
odd_numbers = filter(lambda x: x % 2 != 0, my_list)
print(list(odd_numbers))

from functools import reduce
my_list = [76, 21, 33, 74, 94]
sum_of_list = reduce(lambda x, y: x + y, my_list)
print(sum_of_list)'''

# Write program break, continue and pass with example?

'''for i in range(20):
  if i == 5:
    break
  print(i)


for i in range(15):
  if i == 5:
    continue
  print(i)


for i in range(20):
  pass'''

# What is split in python?
'''The split() method in Python is a string method that splits a string into a list.'''

# What is join in python?
'''The join(sequence) method joins elements and returns the combined string.'''
