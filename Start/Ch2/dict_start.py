# LinkedIn Learning Python course by Joe Marini
# Example file for complex types


# Dictionary: a key-value data structure
mydict = {
  "one" : 1,
  "two" : 2,
  3 : "three",
  4.5 : ["four","point","five"]
}

# print(mydict)

# dictionaries are accessed via keys
# print(mydict["one"])
# print(mydict[3])

# you can also set dictionary data by creating a new key
# mydict["seven"] = 7
# print(mydict)

# Trying to access a nonexistent key will produce an error
# print(mydict["blarg"]) # get an error as we have no key with "blarg" in it

# To avoid this, you can use the "in" operator to see if a key exists
# print("two" in mydict)
# print("blarg" in mydict)

# You can retrieve all of the keys and values from a dictionary
# by using the appropriately named functions
# print(mydict.keys())
# print(mydict.values())
# these are not technically Python lists, they're a dict_keys and dict_values lists, special dictionary types, specfic


# You can also iterate over all the items in a dictionary, "for" is a loop
for key, val in mydict.items():   # creates a tuple
  print(key, val)
  