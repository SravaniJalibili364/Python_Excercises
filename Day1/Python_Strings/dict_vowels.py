'''For a given string, print the count of different vowels in it.'''


# Defining the function to count the different vowels in the string 

def Count_Vowels(string, vowels):

	# Using the casefold function ,string converted to smaller case
	string = string.casefold()
	
	# storing vowels in the count variable using dictionary as a data structure
	count = {}.fromkeys(vowels, 0)


	for character in string:
		# Checking the condition whether the character was vowel or not
		if character in count:
			# If it is a char then the particular vowels count updated in the dictionary
			count[character] += 1
	return count
	

Vowels = 'aeiou'
String = input()
#Now the vowels count will print
print (Count_Vowels(String, Vowels))
