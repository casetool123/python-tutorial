#loop - it helps us to repeat a set of statements.
# 1. while
# 2. for 

# #WHILE LOOP 
# while is used to repeatedly execute instructions as long as the condition is true.
# 
# SYNTAX
# while condition:
#     statement 1
#     statement 2

#1. reapeat a set of statements till a condition remains True

# num = int(input("Enter a number"))
# while num == 3:
#     print("it ran")
#     num = int(input("Enter a number"))

# print('it will not run')


# 2. to repeat a set of ststements finite number of times.

# count = 0
# while count <= 5:
#     print(count)
#     count = count + 1          # increament 


# 3. can also iterate through a string, a list or a tupe

s = 'Bangalore'
lst = ['abc', 'efg', 'hij', 'xyz']
tpl = (10, 20, 30 , 40 , 50)

print(len(s))
print(len(lst))
print(len(tpl))

i = 0
while i < 4:
    print(s[i], lst[i], tpl[i])
    i = i+1



