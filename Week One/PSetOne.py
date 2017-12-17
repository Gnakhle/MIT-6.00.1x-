# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 22:03:13 2017

@author: Gerald
"""

#Problem 1


s = 'azcbobobegghakl'

vowels = 0

for letter in s:
    if (letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u'):
        vowels += 1
print("Number of vowels: " + str(vowels))

#Problem 2

s = 'azcbobobegghakl'


#count = 0
#for i in range(len(s)):
 #   if s[i:i+3] == 'bob':
  #      count += 1
#print("Number of times bob occurs is: " + str(count)

#Problem 3

# initialise tracker variables
maxLen=0
current=s[0]
longest=s[0]

# step through s indices
for i in range(len(s) - 1):
    if s[i + 1] >= s[i]:
        current += s[i + 1]
        if len(current) > maxLen:
            maxLen = len(current)
            longest = current
    else:
        current=s[i + 1]
        
   

print ('Longest substring in alphabetical order is: ' + longest)
