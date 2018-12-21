#Question:
#Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
#Suppose the following input is supplied to the program:
#without,hello,bag,world
#Then, the output should be:
#bag,hello,without,world
p=[x for x in input("enter data with sepatate the comma:").split(",")]
p.sort()
print(",".join(p))