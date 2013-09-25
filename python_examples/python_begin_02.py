#!/usr/bin/python2.7 
#python exmaples 02

#lists
sampleList = [6,7,4,2,3,4]
print(sampleList[1])  # list starts with 0th element
print(' ')

for a in sampleList:
	print(a)	# a=sampleList[0], a=sampleList[1],...
	print(sampleList[1])

sampleList.append(1928)
sampleList.count('4')
sampleList.index(2)
sampleList.insert(6,1934)
sampleList.remove(7)
sampleList.reverse()

print(sampleList)
		
#tuples : non-changable lists!
sampleTuple = (4,5,6)

# convert tuple into list:
list_new = list(sampleTuple)
list_new.append(7)
print(list_new)

# dictionary: the location of element are not numbers anymore
# dictionary = {'key' : value}
sample_dict = {'Rudi Meier' : 37, 'Seyma Bayrak' : 23}
sample_dict['Ayse Bayrak Meier'] = 2
for a in sample_dict :
	print(a)
	print(a,sample_dict[a])

# formatting , note % means a floating number definition
print('my number is %f' % 1453.0554)
print('my number is %.2f' % 1453.0554)
word = "abcdefghijklmnoprstuxywz"
print('%.10s' % word)

#exceptions vs error handling
var1 = '1'
try: 
	var1 = var1 + 1 #would not work since var1 is a string
except:
	print(var1, "is not a number")
print(" ")

try:
	var2 = var1 +1
except:
	var2 = int(var1)+1
print(var2)

# reading .txt file
f = open("test.txt", "r")
print(f.read(1))
print(f.readline())
print(f.read())

myList = []
for line in f:
	myList.append(line)
	print(myList)

f.close()

f = open("test.txt", "w")
f.write("I am the second part of the text file")
f.write("and this is much cooler")
f.write("Maybe someday, he will promote me to a real file.\n")

f = open("test.txt", "r")
print(f.read())

f = open("test.txt", "a")
f.write("and can I get some pickles on that")

from ClassOne import * #get classes from ClassOne file
myBuddy = Calculator() # make myBuddy into a Calculator object
myBuddy.add(2) #use myBuddy's new add method derived from the Calculator class
print(myBuddy.getCurrent()) #print myBuddy's current instance variable










