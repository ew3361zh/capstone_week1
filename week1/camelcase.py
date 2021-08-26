""" 
Write a program that turns a sentence into camel case. The first word is lowercase, 
the rest of the words have their initial letter capitalized, and all of the words 
are joined together. For example, with the input "fOnt proCESSOR and ParsER", 
your program will output "fontProcessorAndParser". 

Optional extra question: print a warning message if the input will not produce a 
valid variable name. You don't need to be exhaustive in checking, but test for a 
few common issues, such as starting with a number, or containing invalid characters 
such as # or + or ". 

Test your program with different example inputs, and comment your code.  
"""
# import regex library
import re
# introduce program to user
print('This program turns a string sentence of separate words into a single camel case string')
# ask user for sentence
sentence = input('Please enter a sentence to be turned into a camel case string: ')
# check for characters we don't want
sentence_regex = re.compile(r'[0-9#+"]+')
# search using the pattern for matches:
sentence_found = sentence_regex.search(sentence)
# add while loop to catch all sentence entries that match this bad pattern of unwanted characters/numbers
while sentence_found is not None:
    sentence = input('Please try again to enter a sentence - don\'t use any numbers or any non-letter characters like (" + #): ')
    sentence_found = sentence_regex.search(sentence)
# split sentence into individual parts
sentence_list = sentence.split()
# create empty string to build final camelcase string into
final_sentence = ''
# use for loop to go through list of sentence pieces numerically
for sentence_piece in range(len(sentence_list)):
    # start with first piece of sentence and make it all lowercase
    if sentence_piece == 0:
        final_sentence = sentence_list[sentence_piece].lower()
    # for all other pieces, make them lowercase and then title-cased
    else:
        final_sentence = final_sentence + sentence_list[sentence_piece].lower().title()

# print the result to the user
print(final_sentence)
