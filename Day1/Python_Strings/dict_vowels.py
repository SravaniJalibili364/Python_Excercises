'''For a given string, print the count of different vowels in it.'''
def Check_Vow(string, vowels):
	
	string = string.casefold()
	

	count = {}.fromkeys(vowels, 0)
	print(count)
	
	for character in string:
		if character in count:
			count[character] += 1
	return count
	

Vowels = 'aeiou'
String = input()
print (Check_Vow(String, Vowels))
