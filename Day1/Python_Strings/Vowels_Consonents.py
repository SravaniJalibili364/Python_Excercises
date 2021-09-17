'''For a given string, print the count of vowels and consonants'''

String_input = input()
Vowels_Count = 0
Consonents_count = 0
Vowels_list = ('a','e','i','o','u','A','E','I','O','U')
other_char_count = 0

for i in String_input:
    #cheking whether i is char or not
    if i.isalpha():
        # Checking the membership where i is in vowel list or not
        if(i in Vowels_list):
            #Now the vowel count increament to 1 if i was in vowel list
            Vowels_Count += 1
        else:
            #Consonent count will increament to if it was not there in list
            Consonents_count += 1
    else:
        other_char_count += 1


print("Vowels_Count",Vowels_Count)
print("Consonents_count",Consonents_count)
print("Other_Char_Count",other_char_count)
