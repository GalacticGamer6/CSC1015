#Program to check the correctness of numberutil.py
#Neeraav Ranjit
# 11/04/2024

"""
>>> import palindrome

>>> palindrome.is_palindrome(None)
True
>>> palindrome.is_palindrome("a")
True
>>> palindrome.is_palindrome("23")
False
>>> palindrome.is_palindrome("323")
True
>>> palindrome.is_palindrome("civic")
True

"""
import doctest
doctest.testmod(verbose=True)
