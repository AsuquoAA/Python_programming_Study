#Python files
#opening a file
fileref = open("olympics.txt", "r")
fileref.close()

#reading a file as a string
fileref = open("school_prompt2.txt","r")
file = fileref.read()

#reading the file as a list  of lines
fileref = open("travel_plans.txt","r")
file = fileref.readlines()

#writing to a file
filename = "squared_numbers.txt"
outfile = open(filename, "w")
for number in range(1, 13):
    square = number * number
    outfile.write(str(square) + "\n")  
outfile.close()

#checking if the file has been created
infile = open(filename, "r")
print(infile.read()[:10])
infile.close()

#using with to open files
with open('mydata.txt', 'r') as md:
    for line in md:
        print(line)

#writing to a csv file
olympians = [("John Aalberg", 31, "Cross Country Skiing, 15KM"),
             ("Minna Maarit Aalto", 30, "Sailing"),
             ("Win Valdemar Aaltonen", 54, "Art Competitions"),
             ("Wakako Abe", 18, "Cycling")]

outfile = open("reduced_olympics2.csv", "w")
# output the header row
outfile.write('"Name","Age","Sport"')
outfile.write('\n')
# output each of the rows:
for olympian in olympians:
    row_string = '"{}", "{}", "{}"'.format(olympian[0], olympian[1], olympian[2])
    outfile.write(row_string)
    outfile.write('\n')
outfile.close()

#Accumulating multiple results in a dictionary
f = open('scarlet.txt', 'r')
txt = f.read()
letter_counts = {}
for c in txt:
    if c not in letter_counts:
        letter_counts[c] = 0
    letter_counts[c] = letter_counts[c] + 1