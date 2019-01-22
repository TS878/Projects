import os
from time import sleep
'''
Fizz Buzz - Write a program that prints the numbers from 1 to 100. But for 
multiples of three print “Fizz” instead of the number and for the multiples of 
five print “Buzz”. For numbers which are multiples of both three and five print
 “FizzBuzz”.
 '''
###FizzBuzz###
for x in range(1,101):
	if x % 15 == 0:
		print("fizzbuzz")
	elif x % 3 == 0:
		print('fizz')
	elif x % 5 == 0:
		print('buzz')
	else:
		print(x) 
sleep(1)
os.system('clear')
###complete###
'''
Reverse a String - Enter a string and the program will reverse it and print it 
out.
'''
### Reverse a String###
def r_string(string):
	#Reverses a string
	string = list(string)
	string.reverse()
	string = ''.join(string)
	print(string)
r_string('test')
r_string('fun')
r_string('class')
sleep(1)
os.system('clear')
###Complete###
'''
 Pig Latin is a game of alterations played on the English language game. To 
 create the Pig Latin form of an English word the initial consonant sound is
  transposed to the end of the word and an ay is affixed (Ex.: "banana" would 
  yield anana-bay). Read Wikipedia for more information on rules.
  '''
###Pig Latin trasnlator###
def translator(word_):
	word = list(word_)
	first_letter = word[0]
	del word[0]
	word.insert(-1,first_letter)
	word = ''.join(word)
	print("%say" % word)
translator('test')
translator('fun')
translator('class')
sleep(1)
os.system('clear')
###Complete###
'''
Count Vowels - Enter a string and the program counts the number of vowels in 
the text. For added complexity have it report a sum of each vowel found.
'''
###Count Vowels###
def c_vowel(string):
	#Counts the number of times vowels appear in a string
	print(string)
	string = string.lower()
	vowels = ['a','e','i','o','u']
	for letter in vowels:
		if letter in string:
			x = string.count(letter)
			print("-%s:%d" % (letter.title(),x))
		else:
			print("-%s:%s" % (letter.title(), None))
	
c_vowel('test')
c_vowel('FUN')
c_vowel('class')
sleep(1)
os.system('clear')
###Complete###
'''
Check if Palindrome - Checks if the string entered by the user is a palindrome.
 That is that it reads the same forwards as backwards like “racecar”
'''
###Check if Palindrome###
def palindrome(string):
	#Checks the string to see if it is a palindrome
	rstring = list(string)
	rstring = rstring.reverse()
	rstring = string
	if rstring == string:
		print('%s:\nyes' % string.title())

palindrome('racecar')
palindrome('test')
palindrome('fun')
palindrome('class')
sleep(1)
os.system('clear')
###Complete###
'''All project ideas come from Karan at https://github.com/karan'''
