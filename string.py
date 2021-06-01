s1 = 'Hello'
#indexing
#Python indexing starts with zero

# H  e  l  l  o
# 0  1  2  3  4 ----- positive indexing
#-5 -4 -3 -2 -1 ------- negative indexing

# positive indexing starts from front and negative indexing starts from end.
# positive indexing starts with 0 and negative indexing starts with -1.

#syntax of indexing
#print(variable_name[index_number])

print(s1[0])    #-->H
print(s1[4])    #-->o
print(s1[1])    #-->1

print(s1[-5])
print(s1[-1])
print(s1[-3])

s2= "Good afternoon"

print(s2[5])
print(s2[10])
print(s2[3])
  
#property of strings:

#1.strings are immutable (it can't be changed)
s4= "amrita"

#2.concatenation -- joining using +
print('hello' + 'world')
s5 = s1 + s4
print(s5)

#3. replication --- duplicate or repeating
print("aaaaa")
print(s1*5)

#slicing
s5 = "programming python"
s6 = "COMPUTER"
#print(variable_name[starting_index : ending_index+1])

print(s5[0:4]) #--- > prog 
print(s5[8:11]) #-- >ing 
print(s5[4:6]) #--->ra 
print(s5[8:14]) #--> ing py

#to find out the length of a string -- len()
print(len(s5))

#method
#print(variable_name.method_name())
#to make a string in uppercase -- upper()
print(s5.upper())
print(s6.lower())

#to make the first character to uppercase -- capitalize()
print(s5.capitalize())

#to count the number of characters -- count()
s7 = "I am writing a code aa hgvnk kljfc aaa kkutvg am "
print(s7.count('a'))

# to replace a character in a string -- replace()
print(s7.replace('w','10'))


s = 'The Terrible Tiger Tore The Towel'
#write a code to count the number of 'T' and replace all the 'T' with 't'

sample = 'I am writing python code. I am a beginner.'
# write a code to replace a the frst 'am' with 'are'.
#indexing # slicing #replace() ...
#output: 'I are writing python code. I am a beginner.'

#replacing 1st am
print(sample.replace('am', 'are', 1))

#replacing 2nd am
s1 = sample[0:25]
s2 = sample[26:]
print(s1)
print(s2)
s3 = s2.replace('am', 'are')
print(s3)
sample = s1 + s3
print(sample)












