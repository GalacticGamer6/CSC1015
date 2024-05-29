#Program to check the correctness of numberutil.py
#Neeraav Ranjit
# 11/04/2024

"""
>>> import numberutil

>>> numberutil.aswords(4)
'four'
>>> numberutil.aswords(100)
'one hundred'
>>> numberutil.aswords(101)
'one hundred and one'
>>> numberutil.aswords(18)
'eighteen'
>>> numberutil.aswords(141)
'one hundred and forty one'
>>> numberutil.aswords(0)
'zero'
>>> numberutil.aswords(45)
'forty five'
>>> numberutil.aswords(345)
'three hundred and forty five'



"""
import doctest
doctest.testmod(verbose=True)
