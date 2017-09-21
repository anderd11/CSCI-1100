import math
# input
first = input('Please enter your first name: ')
last = input('Please enter your last name: ')
last = last+'!'

#max length of all strings
a = max(len(first),len(last),len('Hello,'))

#number of asterisks needed for top and bottom of frame
b = a+6

#number of spaces needed between names
c = a - len(first)
d = a - len(last)

e = math.floor((a - len(first))//2)
f = math.floor((a - len(last))//2)
h = e + len(first)%2
i = f + len(last)%2

# output
print('*'*b)
print('*'*2,'Hello,','*'*2)
print('*'*2,' '*e + str(first)+' '*h,'*'*2)
print('*'*2,' '*f + str(last)+' '*i,'*'*2)
print('*'*b)

'''
doesn't work when we have a name with an odd length
'''