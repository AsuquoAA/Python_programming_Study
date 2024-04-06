#Sentiment classifier
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(string):
    for i in punctuation_chars:
        if i in string:
            string = string.replace(i, "")
    return string        

# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

def get_pos(string):
    sentence = string.split(" ")
    count = 0
    for word in sentence:
        word = word.lower()
        word = strip_punctuation(word)
        if word in positive_words:
            count = count+1
    return count        

#list of negative words to use
negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def get_neg(string):
    sentence = string.split(" ")
    count = 0
    for word in sentence:
        word = word.lower()
        word = strip_punctuation(word)
        if word in negative_words:
            count = count+1
    return count    

with open("project_twitter_data.csv","r") as fileref:
    file = fileref.readlines()
    
with open("resulting_data.csv","w") as classifier:
    classifier.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
    classifier.write("\n")
    for lin in file[1:]:
        lin = lin.strip()
        line = lin.split(",")
        tweet = line[0]
        number_of_retweets = line[1]
        number_of_replies = line[2]
        row_string = ("{},{},{},{},{}".format(number_of_retweets,number_of_replies,get_pos(tweet),get_neg(tweet),get_pos(tweet)-get_neg(tweet)))
        classifier.write(row_string)
        classifier.write("\n")