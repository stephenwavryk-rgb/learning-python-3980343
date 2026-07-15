# LinkedIn Learning Python course by Joe Marini
# Example file for working with functions


# define a basic function
# def hello_func():
#   print("hello world!")
#   name = input("What is your name? ")
#   print("Nice to meet you,", name)

# hello_func()

# function that takes parameters
# def hello_func(greeting):
#   print("hello world!")
#   name = input("What is your name? ")
#   print(greeting, name)

# hello_func("How are you doing? ")
# hello_func("Hey what's up? ")

# function that returns a value
# def cube(x):
#   return x*x*x

# result = cube(3) #variable
# print(result) 

# function with default value for an parameter
# def hello_func(greeting, name=None):
#   print("hello world!")
#   if name == None:
#     name = input("What is your name? ")
#   print(greeting, name)

# hello_func("Nice to meet you", "Stephen")

# def hello_func(greeting, name=None):
#   print("hello world!")
#   if name == None:
#     name = input("What is your name? ")
#   print(greeting, name)

# hello_func("Nice to meet you")

# def hello_func(greeting, name=None):
#   print("hello world!")
#   if name == None:
#     name = input("What is your name? ")
#   print(greeting, name)
# # to provide input to the order above
# hello_func(name = "stephen", greeting ="Nice to meet you")

# function with variable number of parameters
# def multi_add(*args): # the * is used when you don't know how many parameters are going to be used
#   result = 0
#   for x in args:
#     result = result + x
#   return result

# # print(multi_add(4, 5, 10, 4))
# print(multi_add(4, 5, 10, 4, 10))


# modify above to start
def multi_add(start, *args): # the * is used when you don't know how many parameters are going to be used
  result = start
  for x in args:
    result = result + x
  return result

print(multi_add(10, 4, 5, 10, 4, 10))
# result is 43

# modify above to start
def multi_add(start, *args): # the * is used when you don't know how many parameters are going to be used
  result = start
  for x in args:
    result = result + x
  return result

print(multi_add(0, 4, 5, 10, 4, 10))
# result is 33

