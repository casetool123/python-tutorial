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






