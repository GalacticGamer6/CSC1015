#Program to test timeutil
#Neeraav Ranjit
#12/04/2023

"""
>>> import timeutil
>>> timeutil.validate("00:00 a.m.")
False
>>> timeutil.validate("hh:45 a.m.")
False
>>> timeutil.validate("8:45 b.k.")
False
>>> timeutil.validate("4:455 p.m.")
False
>>> timeutil.validate(":7:34 p.m.")
False
>>> timeutil.validate("4:30 a.m.")
True

"""
import doctest
doctest.testmod(verbose=True)