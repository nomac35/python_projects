
#Pig Latin Games
#Rules:
#For word that begin with constant sound is transposed to the end of the word and "ay" is affixed
#if it starts with vowel add "yay" to the end
#needs to start with an alpabetical character
word = str(raw_input("Please enter a word : "))

while not word.isalpha():
	print("Please enter a alphab characters only")
	word = str(raw_input("Please enter a word : "))
else:
	if word[0] not in 'aeiouAeiou':
 		print word[1:]+word[0]+"ay"
 	else:
 		print word+"yay"

