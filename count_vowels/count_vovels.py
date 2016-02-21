#Write a program to count the vowels in a given string

word = raw_input("Please enter a string: ")
vowels = 'aeiuo'

count = {}.fromkeys(vowels,0)

for i in word.lower():
	if i in count:
		count[i]+=1
print count