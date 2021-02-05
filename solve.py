import re
import os
import sys

#import dictionary file
with open(os.path.join(sys.path[0],"dictionary.txt"),"r") as f:
    words = f.read()

notDone = True

def printWord(myWord):
    for i in myWord:
        print(i,end=" ")

def getWords(myReg,words=words):
    reg = re.compile(r'%s'%myReg)
    mo = reg.findall(words)
    return mo
        
def removeWords(words,notThere):
    finalWords = []
    for word in words:
        isThere = False
        for letter in notThere:
            if letter in word:
                isThere = True
                break
        if not isThere:
            finalWords.append(word)
    return finalWords

def showWords(words,notThere):
    print('available words are: ')
    print(notThere)
    print(words)

def stringToRegex(myWord):
    myreg = []
    for i in myWord:
        if i == '_':
            myreg.append(r'\w')
        else:
            myreg.append(i)
    return myreg


numberOfChar = int(input("please enter number of chars : "))
myWord = ['_'] * numberOfChar


while notDone:
    guess = input("show me your guesses (put an ' _ ' where u dont know the letters): ")
    notThere = []
    letters = input("what letters are not there? ")
    for letter in letters:
        notThere.append(letter)
    for i in range(len(guess)):
        myWord[i] = guess[i]
    myWordstr = ''.join(myWord)
    printWord(myWordstr)
    print('\n')
    if '_' not in myWordstr:
        notDone =False
    myReg = stringToRegex(myWordstr)
    print(myWordstr)
    print(myReg)

    myWords = getWords(''.join(myReg))

    finalW = removeWords(myWords,notThere)
    showWords(finalW,notThere)


