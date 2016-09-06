import re
import os
from myClass import *



# implementation notes at worst this program runs at O(n^2)
# TODO: create a gui for class inputs and for displays
#		have a excel to txt converter function

#creates a "myClass" from class textfile and returns it
def makeFiles(filename):

	thisClass = DartmouthClass()
	#opens the given file and gets its contents and the first line
	with open('./data/'+filename, 'r') as myfile:
		data=myfile.read()
		myfile.seek(0)
		firstLine = myfile.readline()

	#finds the Dartmouth Class Name going CLST ###
	regClassName = re.compile('CLST\s\d\d\d\s')
	regClassNum = re.compile('\d\d\d')
	className = re.search(regClassName, data)
	classNum = re.search(regClassNum, className.group())

	#finds the year of the class from the first line
	regYear = re.compile('\d\d\d\d')
	classYear = re.search(regYear, firstLine)

	#finds the time of year the class was from first line
	regTerm = re.compile('Winter|Fall|Spring|Summer')
	classTerm = re.search(regTerm, firstLine)

	#finds all of the dartmouth IDs in the file
	regDid = re.compile('F0\w\w\w\w\w')
	dids = re.findall(regDid, data)

	#writes to a file that is made from the found class info
	#f = open(classNum.group() + classTerm.group() + classYear.group() + '.txt', 'w')
	#f.write(classNum.group()+"\n")
	#f.write(classTerm.group() +"\n")
	#f.write(classYear.group() + "\n")

	#sets the values for the class
	thisClass.setNumber(classNum.group())
	thisClass.setTerm(classTerm.group())
	thisClass.setYear(classYear.group())

	for i in dids:
		thisClass.appendDid(i)
		#f.write(i + "\n")

	#f.close()
	thisClass.setDate()
	#print (thisClass.getDid())
	return thisClass

def sortClasses(classList):
	sortClassesHelper(classList, 0 , len(classList)-1)
def sortClassesHelper(thisList, first, last):
	if first < last:
		spiltpoint = partition(thisList, first, last)
		sortClassesHelper(thisList, first, spiltpoint - 1)
		sortClassesHelper(thisList, spiltpoint + 1, last)
# basic quicksort algoirthm
def partition(alist, first, last):
	pivotvalue = alist[first].getDate()
	leftmark = first+1
	rightmark = last
	done = False
	while not done:
		while leftmark <= rightmark and alist[leftmark].getDate() <= pivotvalue :
			leftmark = leftmark + 1
		while alist[rightmark].getDate() >= pivotvalue and rightmark >= leftmark:
			rightmark = rightmark - 1
		if rightmark < leftmark:
			done = True
		else:
			temp = alist[leftmark]
			alist[leftmark] = alist[rightmark]
			alist[rightmark] = temp
	temp = alist[first]
	alist[first] = alist[rightmark]
	alist[rightmark] = temp

	return rightmark


classList = []
for filename in os.listdir('./data'):
	classList.append(makeFiles(filename))

 # this dictionary takes a student id as a key has a value of 
 # a list of classes the student has taken
classDictionary = {}

#this fills the dictionary with students based on class
for thisClass in classList:
	for studentId in thisClass.getDid():
		if (classDictionary.get(studentId) == None):
			tempList = []
			tempList.append(thisClass)
			classDictionary[studentId] = tempList
		else:
			classDictionary.get(studentId).append(thisClass)

totalstudents = 0 
firstStudents = 0
for y in classDictionary:
	print (y)
	totalstudents += 1
	sortClasses(classDictionary[y])
	if (classDictionary[y][0].getNumber() == "001"):
		firstStudents += 1
	for w in classDictionary[y]:
		print w.getDate()



print totalstudents
print firstStudents











