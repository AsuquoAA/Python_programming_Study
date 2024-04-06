#python functions and dictionaries
#dictionary
#creating a dictionary
medals = {"gold":33,"silver":17,"bronze":12}
print(medals)

#adding key-value pairs to a dictionary
places = {"Australia":2000, "Greece":2004, "China":2008, "England":2012}
places["Brazil"] = 2016
print(places)

#dictionary operations
#delete a key-value pair from a dictionary
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
del inventory['pears']
print(inventory)

#update the value of a dictionary's key
swimmers = {'Manuel':4, 'Lochte':12, 'Adrian':7, 'Ledecky':5, 'Dirado':4, 'Phelps':23}
swimmers["Phelps"] = 28
print(swimmers)

#dictionary methods
#.keys:gives the keys of the  dictionary
#.values: gives the values of a dictionary
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
print(list(inventory.values()))
for v in inventory.values():
    print("Got", v)

#.items: gives the key-value pairs of a dictionary as a tuple
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
print(list(inventory.items()))
for k, v in inventory.items():
    print("Got", k, "that maps to", v)

#safely retrieving values from a dictionary
#1.using in and not in operators
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
print('apples' in inventory)
print('cherries' in inventory)
if 'bananas' in inventory:
    print(inventory['bananas'])
else:
    print("We have no bananas")
        
#2.get: gets the value of a key from the dictionary, if key not in dictionary, it returns None
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
print(inventory.get("apples"))
print(inventory.get("cherries"))
print(inventory.get("cherries",0))

#function parameter passing
def hello2(s):
    print("Hello " + s)
    print("Glad to meet you")

hello2("Iman" + " and Jackie")
hello2("Class " * 3)

#function that accumulates
def total(lst):
    tot = 0
    for num in lst:
        tot = tot + num
    return tot 

#local variables in functions
def square(x):
    y = x * x
    return y

z = square(10)

#global variables in functions
def badsquare(x):
    y = x ** power
    return y

power = 2
result = badsquare(10)
print(result)
#note python checks if the variable is found in the local scope before going to check for it in the global scope

#function composition
def most_common_letter(s):
    frequencies = count_freqs(s)
    return best_key(frequencies)

def count_freqs(st):
    d = {}
    for c in st:
        if c not in d:
             d[c] = 0
        d[c] = d[c] + 1
    return d

def best_key(dictionary):
    ks = dictionary.keys()
    best_key_so_far = list(ks)[0]  # Have to turn ks into a real list before using [] to select an item
    for k in ks:
        if dictionary[k] > dictionary[best_key_so_far]:
            best_key_so_far = k
    return best_key_so_far

print(most_common_letter("abbbbbbbbbbbccccddddd"))

#tuple packing
def circle(x):
    c = 2*3.142*x
    a = 3.142*x*x
    return(c,a)
print(circle(7))

#Tuple assignment with unpacking
julia = "Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia"
name, surname, birth_year, movie, movie_year, profession, birth_place = julia
print(name)

#Unpacking tuples as an argument with the help of *
def add(x, y):
    return x + y

print(add(3, 4))
z = (5, 4)
print(add(*z)) # this line will cause the values to be unpacked

#while statement: hybrid of for and if statements
counter = 0
eve_nums = []
while counter<=15:
    if counter%2==0:
        eve_nums.append(counter)
    counter = counter + 1 

#another example opf while statements
def stop_at_four(lst):
    new_lst = []
    idx = 0
    while idx<len(lst):
        if lst[idx] != 4:
            new_lst.append(lst[idx])
        else:    
            return new_lst
        idx = idx + 1    
    return new_lst

#listener loop: you input a value or word for the while loop to end
#1.example: simple example
theSum = 0
x = -1
while (x != 0):
    x = int(input("next number to add up (enter 0 if no more numbers): "))
    theSum = theSum + x

print(theSum)

#2.example: complex example
def get_yes_or_no(message):
    valid_input = False
    while not valid_input:
        answer = input(message)
        answer = answer.upper() # convert to upper case
        if answer == 'Y' or answer == 'N':
            valid_input = True
        else:
            print('Please enter Y for yes or N for no.')
    return answer

response = get_yes_or_no('Do you like lima beans? Y)es or N)o: ')
if response == 'Y':
    print('Great! They are very healthy.')
else:
    print('Too bad. If cooked right, they are quite tasty.')

#Break: breaks out of the  while loop and goes to the next line of code
while True:
    print("this phrase will always print")
    break
    print("Does this phrase print?")

print("We are done with the while loop.")

#Continue: breaks out of the while loop but continues at the beginning of the while loop again
x = 0
while x < 10:
    print("we are incrementing x")
    if x % 2 == 0:
        x += 3
        continue
    if x % 3 == 0:
        x += 5
    x += 1
print("Done with our loop! X has the value: " + str(x))

#functions: optional parameters
def str_mult(string,x=3):
    return string * x
#note: a value for the optional parameter is always given

#keyword parameters
def multiply(string,mult_int=10):
    return string * mult_int
#here mult_int is the keyword

#Using def vs using lambda
#using def
def last_char(s):
    return s[-1]

#using lambda
last_char = lambda s: s[-1]

#Sort method vs sorted function
#sort method: mutates the list returning no new value instead sorting that particular list and it  does not work on strings
L1 = [1, 7, 4, -2, 3]
L1.sort()
print(L1)

#sorted function: it does not mutate the list, it returns a new list and leaves the other list unchanged, works on strings too
L2 = ["Cherry", "Apple", "Blueberry"]
L3 = sorted(L2)
print(L3)
print(L2) # unchanged

#optional reverse parameter: reverse the order of sorting
L2 = ["Cherry", "Apple", "Blueberry"]
print(sorted(L2, reverse=True))

#optional key parameter: you can sort a list  based on a function e.g absolute
L1 = [1, 7, 4, -2, 3]
def absolute(x):
    if x >= 0:
        return x
    else:
        return -x
L2 = sorted(L1, key=absolute)
print(L2)
#or in reverse order
print(sorted(L1, reverse=True, key=absolute))

#sorting a dictionary
L = ['E', 'F', 'B', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D']
d = {}
for x in L:
    if x in d:
        d[x] = d[x] + 1
    else:
        d[x] = 1
y = sorted(d.keys(), key=lambda k: d[k], reverse=True)
for k in y:
    print("{} appears {} times".format(k, d[k]))

#Breaking ties, second sorting
fruits = ['peach', 'kiwi', 'apple', 'blueberry', 'papaya', 'mango', 'pear']
new_order = sorted(fruits, key=lambda fruit_name: (len(fruit_name), fruit_name), reverse=True)
for fruit in new_order:
    print(fruit)

#in case we want to reverse the number of letters but not the fruit name
fruits = ['peach', 'kiwi', 'apple', 'blueberry', 'papaya', 'mango', 'pear']
new_order = sorted(fruits, key=lambda fruit_name: (-len(fruit_name), fruit_name))
for fruit in new_order:
    print(fruit)    