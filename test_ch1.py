   # Write a function that takes a string argument
   # and returns the number of vowels in it

def vowel_count(string):
       vowels = ['a', 'e', 'i', 'o', 'u']
       count = 0
       for ch in string.lower():
           if ch in vowels:
               count += 1
       return count


def test_with_any_name():
    assert vowel_count('chromedriver') == 4

def test_with_my_uppercase_name():
    assert vowel_count('CHROMEDRIVER') == 4

