#!/usr/bin/python

# www.sthurlow.com/python/

#printing out 

## fuctions
def hello():
	print "hello"
	return 1234

def sentence_function(first_word,second_word):
	print "The sentence created is: " +first_word +second_word
	return first_word + second_word

def calc_menu():
	print "Welcome to calculator.py"
	print "your options are: "
	print " "
	print "1) Addition"
	print "2) Subtraction"
	print "3) Multiplication"
	print "4) Division"
	print "5) Quit calculator.py"
	print " "
	
	choice = input("Choose your option: ")
	return choice

def calc_act(choice):
	loop = 1
	if choice == 1:
		add1 = input("Add this: ")
		add2 = input("to this: ")
		print add1, "+", add2, "=", add1 + add2
	elif choice == 2:
		sub2 = input("Subtract this: ")
		sub1 = input("from this: ")
		print sub1, "-", sub2, "=", sub1 - sub2
	elif choice == 3:
		mul1 = input("Multiply this: ")
		mul2 = input("with this: ")
		print mul1, "*", mul2, "=", mul1 * mul2
	elif choice == 4:
		div1 = input("Divide this: ")
		div2 = input("by this: ")
		print div1, "/", div2, "=", div1 / div2
	elif choice == 5:
		loop=0
	return loop

#calculator program
def simple_calc():
	loop = 1
	while loop == 1:
		choice = calc_menu()
		loop = calc_act(choice)
	
	print "Thankyou for using calculator.py!"
	print " "
	return


## main program
print "Mary had a little lamb,	"
print "it's fleece was white as snow;"
print "and everywhere that Mary went",
print "her lamb was sure to go."

#varaiables
print " "
v=1
print "The value of v is now", v
v=v+1
print "v equals to now v+1=", v
print " "

#strings
word1 = "Good"
word2 = "morning"
word3 = "Askim"
word4 = word1 + " " +word2 + " to you too! "

sentence = word1 + " "+ word2 +" "+ word3
print sentence
print word4
print " "

#loops
a=0
print "a is equal to ", a
print "Let us put the variable a into a while loop a=a+1 until a<10"
while a<10:
      a=a+1
      print a
print "And now the loop has ended."
print " "

#if statement
print "Show the even numbers between 0 and 20"
n =0
while n <= 20:
	if n % 2 == 0:
		print n
	n=n+1
print "there, done"
print " "

b=10
while b>0:
	print "b is equal to", b
	if b>5 :
            print "Big number!"
	elif b % 2 !=0 :
	    print "This is an odd number"
	    print "It isn't greater than five, either"
	else :
	    print "this number isn't greater than 5"
	    print "nor is it odd"
	
	b=b-1
	print "I just made 'b' less than what it was"
print "loop is over"
print " "

#functions
c = raw_input("type your input: ") # raw_input takes a string!
print c
print " "


first_word  = raw_input("type your first word ")
second_word = raw_input("type your second word ")
print sentence_function(first_word,second_word)

simple_calc()

#lists,tuples,dictionaries
# list are modifiable, tubples not!
months = ('January','February','March','April','May','June',\
'July','August','September','October','November','  December')

cats = ['Tom', 'Snappy', 'Kitty', 'Jessie', 'Chester']
print cats[2]
cats.append('Catherine') #adding a new element at the end of list
del cats[1]   # removing second cat in original list

#Make the phone book:
phonebook = {'Andrew Parson':8806336, \
'Emily Everett':6784346, 'Peter Power':7658344, \
'Lewis Lame':1122345}
phonebook['Gingerbread Man'] = 1234567
del phonebook['Andrew Parson']

if phonebook.has_key('Peter Power'):
	print "Peter Power is in the dictionary. His/her number is: ", \
	      phonebook['Peter Power']
else :
	print "Peter Power is not in the dictionary"

print "The following people are in the dictionary: "
print phonebook.keys()
print "Their phone numbers are the following: "
print phonebook.values()
print "phonebook dictionary has", len(phonebook), "entries in it" 

# len() code gives length or number of elements!


# for loop
newList=[45, 'eat me', 90210, "The day has come, the walrus said, \
to speak of many things", -67]

for value in newList:
    print value


# cheerleading program
word = raw_input("Who do you go for? ") #get a word from the user

for letter in word:
    call = "Gimme a " + letter + "!"
    print call
    print letter + "!"

print "What does that spell?"
print word + "!"

#TEXT ADVENTURE GAME

#the menu function:
def menu(list, question):
    for entry in list:
        print 1 + list.index(entry),
        print ") " + entry

    return input(question) - 1

#Give the computer some basic information about the room:
items = ["pot plant","painting","vase","lampshade","shoe","door"]

#The key is in the vase (or entry number 2 in the list above):
keylocation = 2

#You haven't found the key:
keyfound = 0

loop = 1

#Give some introductary text:
print "Last night you went to sleep in the comfort of your own home."
print "Now, you find yourself locked in a room. You don't know how"
print "you got there, or what time it is. In the room you can see"
print len(items), "things:"
for x in items:
    print x
print ""
print "The door is locked. Could there be a key somewhere?"

#Get your menu working, and the program running until you find the key:

while loop == 1:
    choice = menu(items,"What do you want to inspect? ")
    if choice == 0:
        if choice == keylocation:
            print "You found a small key in the pot plant."

            print ""
            keyfound = 1
        else:
            print "You found nothing in the pot plant."
            print ""
    elif choice == 1:
        if choice == keylocation:
            print "You found a small key behind the painting."
            print ""

            keyfound = 1
        else:
            print "You found nothing behind the painting."
            print ""
    elif choice == 2:
        if choice == keylocation:
            print "You found a small key in the vase."
            print ""
            keyfound = 1
        else:
            print "You found nothing in the vase."

            print ""
    elif choice == 3:
        if choice == keylocation:
            print "You found a small key in the lampshade."
            print ""
            keyfound = 1
        else:
            print "You found nothing in the lampshade."
            print ""

    elif choice == 4:
        if choice == keylocation:
            print "You found a small key in the shoe."
            print ""
            keyfound = 1
        else:
            print "You found nothing in the shoe."
            print ""
    elif choice == 5:
        if keyfound == 1:
            loop = 0
            print "You put in the key, turn it, and hear a click"

            print ""
        else:
            print "The door is locked, you need to find a key."
            print ""

# Remember that a backslash continues
# the code on the next line

print "Light floods into the room as \
you open the door to your freedom."






