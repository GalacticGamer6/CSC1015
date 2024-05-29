# A program to test numberutil
#Neeraav Ranjit
#12/04/2024
"""
>>> import numberutil

>>> numberutil.aswords(0)
'zero'
>>> numberutil.aswords(100)
'one hundred'
>>> numberutil.aswords(144)
'one hundred and forty four'
>>> numberutil.aswords(140)
'one hundred and forty'
>>> numberutil.aswords(112)
'one hundred and twelve'
>>> numberutil.aswords(9)
'nine'
>>> numberutil.aswords(45)
'forty five'
>>> numberutil.aswords(40)
'forty'

"""
import doctest
doctest.testmod(verbose=True)