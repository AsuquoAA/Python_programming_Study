import random

VOWEL_COST = 250
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS = 'AEIOU'

# Write the WOFPlayer class definition (part A) here
class WOFPlayer:
    def __init__(self,name):
        self.name=name
        self.prizeMoney=0
        self.prizes=[]
     
    def addMoney(self,amt):
        self.prizeMoney = self.prizeMoney + amt
    
    def goBankrupt(self):
        self.prizeMoney = 0
    
    def addPrize(self,prize):
        return self.prizes.append(prize)
    
    def __str__(self):
        return "{} (${})".format(self.name,self.prizeMoney)
# Write the WOFHumanPlayer class definition (part B) here
class WOFHumanPlayer(WOFPlayer):
    def __init__(self,name):
        WOFPlayer.__init__(self,name)
            
    def getMove(self,category, obscuredPhrase, guessed): 
        print("{} has ${}".format(self.name,self.prizeMoney))
        print("")
        print("Category: {}".format(category))
        print("Phrase:  {}".format(obscured_phrase))
        print("Guessed: {}".format(guessed))
        print("")
        move = input("Guess a letter, phrase, or type 'exit' or 'pass':")
        return move
# Write the WOFComputerPlayer class definition (part C) here
class WOFComputerPlayer(WOFPlayer):
    SORTED_FREQUENCIES = "ZQXJKVBPYGFWMUCLDRHSNIOATE"

    def __init__(self, name, difficulty):
        WOFPlayer.__init__(self, name)
        self.difficulty = difficulty

    def smartCoinFlip(self):
        num = random.randint(1, 10)
        return num <= self.difficulty

    def getPossibleLetters(self, guessed):
        if self.prizeMoney<VOWEL_COST:
            return [letter for letter in "BCDFGHJKLMNPQRSTVWXYZ" if letter not in guessed]
        if self.prizeMoney>=250:
            return [letter for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if letter not in guessed]

    def getMove(self, category, obscuredPhrase, guessed):
        SORTED_FREQUENCIES = "ZQXJKVBPYGFWMUCLDRHSNIOATE"
        gp = self.getPossibleLetters(guessed)
        if gp == [] or gp == "pass":
            return "pass"
        scf = self.smartCoinFlip()
        if scf == True:
            for item in SORTED_FREQUENCIES[::-1]:
                if item in gp:
                    return item
        else:
            return random.choice(gp)
                    
