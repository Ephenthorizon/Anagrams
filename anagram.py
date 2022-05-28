# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True

def find_anagrams(word,anagram):
    # Removing the spacing in the word and anagram
    word = word.replace(' ', '')
    anagram = anagram.replace(' ', '')
    #Checking if the letters in word and anagram are the same.
    if sorted(word.lower()) == sorted(anagram.lower()):
        return True
    else:
        return False
print(find_anagrams('blame', 'a blem'))
print(find_anagrams('hello', 'check '))
print(find_anagrams('racecar', 'cecar ra'))