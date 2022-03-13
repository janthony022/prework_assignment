#Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.

def hello_name(user_name):
    print("Hello, " + user_name.title() + "!")

hello_name("anthony")

#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    numbers = list(range(0,101))
    for number in numbers:
        if number % 2 != 0:
            print(number)    

first_odds()

#Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

def max_num_in_list(a_list):
    max_num = a_list[0]
    for a in a_list:
        if a > max_num:
            max_num = a
    return max_num

print(max_num_in_list([1, 5, 4, 56, 7893, 3232, 9999]))

#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):
    if a_year%4 == 0:
        print(a_year, "True")
    elif a_year%400 == 0:
        print(a_year, "True")
    elif a_year%100 !=0:
        print(a_year, "False")
    else:
        print(a_year, "False")

is_leap_year(2022)

#Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list):
    return sorted(a_list) == list(range(min(a_list), max(a_list) + 1))

a_list = [2,3,5,6,7,8,9]
print(is_consecutive(a_list))

def is_consecutive(a_list):
    return sorted(a_list) == list(range(min(a_list), max(a_list) + 1))

a_list = [1,2,3,4,5,6,7]
print(is_consecutive(a_list))