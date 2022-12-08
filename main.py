# Language Generator by Zer0 2022

import random
words, final = [], []
ix, x = 0, 1

def getLang():  # Gets names of languages for counting (not pretty)
    print('\n')
    global l1, l2, l3, l4, l5
    l1 = input('  Language 1:  ')
    l2 = input('  Language 2:  ')
    l3 = input('  Language 3:  ')
    l4 = input('  Language 4:  ')
    l5 = input('  Language 5:  ')
    print('\n')

def inW(i1, i2, i3, i4, i5):  # Gets Words
    global ix
    if i1:  # Checks if language is active
        ix += 1  # ix is counter var for reference
        w1 = input('  ' + i1 + ' Word:  ')  # Gets word for lang
        words.append(frag(w1))  # Send word to fragmenter; return as list; add to words
    if i2:
        ix += 1
        w2 = input('  ' + i2 + ' Word:  ')
        words.append(frag(w2))
    if i3:
        ix += 1
        w3 = input('  ' + i3 + ' Word:  ')
        words.append(frag(w3))
    if i4:
        ix += 1
        w4 = input('  ' + i4 + ' Word:  ')
        words.append(frag(w4))
    if i5:
        ix += 1
        w5 = input('  ' + i5 + ' Word:  ')
        words.append(frag(w5))
    return min(len(x) for x in words)

def frag(w):  # Fragments the Words
    temp = []  # Declares list
    for letter in w:  # Finds amount of letters in the word
        temp.append(letter)  # Adds each letter to the list in order
    return temp  # Returns list

def scram(sLen):  # Scrambles the lists into new word list
    for c in range(0, sLen):  # Length of shortest word
        temp = []  # Declares/empties temporary list
        for l in range(0, len(words)):  # Amount of words in
            temp.append(words[l][c])  # Adds set of respectful letters to temp list
        final.append(random.choice(temp))  # Picks letter from temp list; goes to final word list
    return final  # Returns new word list

def defrag(inL):  # Defragments the word list
    outW = ''  # Initializes new word sring
    for i in inL:  # Length of list
        outW += i  # Appending letters to string
    return outW  # Returns word string

print('  LANGUAGE GENERATOR BY ZER0 2022')

while x == 1:
    getLang()
    outL = scram(inW(l1, l2, l3, l4, l5))
    print('  New Word: ' + defrag(outL))
    words, final = [], []
    ix, x = 0, 1
    again = input('  Go Again (y/n)?  ')
    if again == 'n':
        x = 0
