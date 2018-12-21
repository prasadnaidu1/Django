#Question:
#Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
#Suppose the following input is supplied to the program:
#hello world and practice makes perfect and hello world again
#Then, the output should be:
#again and hello makes perfect practice world

#Hints:
#In case of input data being supplied to the question, it should be assumed to be a console input.
#We use set container to remove duplicated data automatically and then use sorted() to sort the data.
str=input("enter the data :")
lines=[line for line in str.split()]
#print(" ".join(sorted(list(set((lines))))))
l1=sorted(lines)
print(l1)
l2=list(lines)
print(l2)
l3=sorted(l1)
print(l3)
l4=set(lines)
print(l4)
l5=" ".join(sorted(list(set(lines))))
print(l5)