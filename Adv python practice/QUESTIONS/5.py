#Question:
#Define a class which has at least two methods:
#getString: to get a string from console input
#printString: to print the string in upper case.
#Also please include simple test function to test the class methods.

#Hints:
#Use __init__ method to construct some parameters
class sample:
    def __init__(self):
        self.string=""
    def getstring(self):
        self.string=input("enter your string :")
    def printstring(self):
        print(self.string.upper())
#calling block
s=sample()
s.getstring()
s.printstring()