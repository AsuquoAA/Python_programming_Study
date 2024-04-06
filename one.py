#Python Basics
#functions introduction
def time():
    str_seconds = input("Please enter number of seconds: ")
    seconds = int(str_seconds)
    hours = seconds//3600
    remains = seconds%3600
    minutes = remains//60
    remaining_seconds = remains%60
    return ("We have {} hours, {} minutes and {} seconds left".format(hours,minutes,remaining_seconds))

#turtle drawing
import turtle
def draw():
    wn = turtle.Screen()
    wn.bgcolor("red")
    alex = turtle.Turtle()
    alex.pensize(5)
    alex.color("white")
    alex.forward(150)
    alex.left(90)
    alex.forward(70)
    alex.left(90)
    alex.forward(150)
    alex.left(90)
    alex.forward(70)

    john = turtle.Turtle()
    john.pensize(5)
    john.color("black")
    john.left(180)
    john.forward(150)
    john.right(90)
    john.forward(70)
    john.right(90)
    john.forward(150)
    john.right(90)
    john.forward(70)

    james = turtle.Turtle()
    james.pensize(5)
    james.color("gold")
    james.right(90)
    james.forward(200)
    james.shape("turtle")
    james.stamp()
    james.penup()
    distance = 10
    angle = 90
    for _ in range(10):
        james.right(angle)
        james.forward(distance)
        angle+=5
        distance+=5

    wn.exitonclick()

#Indexing
#print the 34th element  of the list
lst = ["hi", "morning", "dog", "506", "caterpillar", "balloons", 106, "yo-yo", "python", "moon", "water", "sleepy", "daffy", 45, "donald", "whiteboard", "glasses", "markers", "couches", "butterfly", "100", "magazine", "door", "picture", "window", ["Olympics", "handle"], "chair", "pages", "readings", "burger", "juggle", "craft", ["store", "poster", "board"], "laptop", "computer", "plates", "hotdog", "salad", "backpack", "zipper", "ring", "watch", "finger", "bags", "boxes", "pods", "peas", "apples", "horse", "guinea pig", "bowl", "EECS"]
print(lst[33])    

#print the last element of the list
lst = "Every chess or checkers game begins from the same position and has a finite number of moves that can be played. While the number of possible scenarios and moves is quite large, it is still possible for computers to calculate that number and even be programmed to respond well against a human player..."
output = lst[-1]

#Slicing
#String slices or substrings
fruit = "banana"
print(fruit[:3])
print(fruit[3:])
#List slices
a_list = ['a', 'b', 'c', 'd', 'e', 'f']
print(a_list[1:3])
print(a_list[:4])
print(a_list[3:])
print(a_list[:])

#Tuple slices
julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
print(julia[2])
print(julia[2:6])
print(len(julia))
julia = julia[:3] + ("Eat Pray Love", 2010) + julia[5:]
print(julia)

#Tricky slice
L = [0.34, '6', 'SI106', 'Python', -2]
print(L[1:-1])
print(len(L[1:-1]))

#using the len function
lst = ["hi", "morning", "dog", "506", "caterpillar", "balloons", 106, "yo-yo", "python", "moon", "water", "sleepy", "daffy", 45, "donald", "whiteboard", "glasses", "markers", "couches", "butterfly", "100", "magazine", "door", "picture", "window", ["Olympics", "handle"], "chair", "pages", "readings", "burger", "juggle", "craft", ["store", "poster", "board"], "laptop", "computer", "plates", "hotdog", "salad", "backpack", "zipper", "ring", "watch", "finger", "bags", "boxes", "pods", "peas", "apples", "horse", "guinea pig", "bowl", "EECS"]
print(len(lst))

#Concatenation
fruit = ["apple","orange","banana","cherry"]
print([6,7] + [8,9])
print(fruit+[6,7,8,9])

#Repetition
food = ["rice,beans,yam,plantain"]
more_food = food * 3
print(more_food)

#Count method: counts the number of times an item appears in a string or list
a = "I have had an apple on my desk before!"
print(a.count("e"))
print(a.count("ha"))

#index method: gives us the index of the first time an item appears in a string or list
music = "Pull out your music and dancing can begin"
print(music.index("m"))
print(music.index("your"))

#split method: to split a string into substrings of a list based on the item placed in the the parenthesis
#with  nothing in the parenthesis
song = "The rain in Spain..."
wds = song.split()
print(wds)

#with an item placed in the parenthesis
song = "The rain in Spain..."
wds = song.split('ai')
print(wds)

#join method: to join substrings into a string
wds = ["red", "blue", "green"]
glue = ';'
s = glue.join(wds)
print(s)
print(wds)

#Accumulator pattern
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
accum = 0
for w in nums:
    accum = accum + w
print(accum)

#Range function
print(range(10))
print(range(2,10))
print(range(0,100,10))
print(list(range(0,99,11)))

#traversal and the dor loop by index
fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']
for n in range(len(fruits)):
    print(n,fruits[n])

#Mutability: lists are mutable, hence they support item reassignment, strings are immutable and do not
fruit = ["banana", "apple", "cherry"]
print(fruit)

fruit[0] = "pear"
fruit[-1] = "orange"
print(fruit)
#note: tuples are also immutable, hence do not support  item reassignment

#del operator: for deleting an item/items from a list
a = ['one', 'two', 'three']
del a[1]
print(a)

alist = ['a', 'b', 'c', 'd', 'e', 'f']
del alist[1:5]
print(alist)

#Referencing
#strings that are equivalent do not point to the same object, hence they have same id
a = "banana"
b = "banana"
print(a is b)
print(id(a))
print(id(b))

#lists that are equivalent do not point to the  same object, hence they have different id
a = [81,82,83]
b = [81,82,83]
print(a is b)
print(a == b)
print(id(a))
print(id(b))

#alias a list: what happens to one list,happens to the other
w = [1,2,3,4,5]
x=w

#cloning a list, each list is independent
q = [6,7,8,9,0]
r = q[:]

#mutating or destructive methods on lists
#1.append method; adds an item to the end of a list
mylist = []
mylist.append(5)
mylist.append(27)
mylist.append(3)
mylist.append(12)
print(mylist)

#2.insert method: inserts an item wherever you tell it to
mylist.insert(1, 12)#insert the value  12 in the index 1
print(mylist)

#3.reverse method: returns the list in reverse 
mylist.reverse()
print(mylist)

#4.index method: gives us the index of the first time an item appears in a list
print(mylist.index(3))

#5.Count method: counts the number of times an item appears in a list
print(mylist.count(12))

#6.sort method: sorts the list
mylist.sort()
print(mylist)

#7.remove method: removes an item from a list
mylist.remove(5)
print(mylist)

#8.pop method: removes the last item on the list
mylist.pop()
print(mylist)

#non-mutating methods on strings
#Upper method: takes the string to uppercase
ss = "Hello, World"
print(ss.upper())

#Lower method: takes the string to lowercase
tt = ss.lower()
print(tt)

#count method: counts the number of times an item appears in a string
yy = "    Hello, World    "
els = yy.count("l")
print(els)

#strip method: removes white space before or after a string
print(yy.strip())

#replace method: replaces a part of a string with any string you chose
news = yy.replace("o", "***")
print(news)

#format method:
scores = [("Rodney Dangerfield", -1), ("Marlon Brando", 1), ("You", 100)]
for person in scores:
    name = person[0]
    score = person[1]
    print("Hello {}. Your score is {}.".format(name, score))


#checking if a string is in reverse(use [::-1])
p_phrase = "was it a car or a cat I saw"
r_phrase = p_phrase[::-1]