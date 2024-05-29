"""
Neeraav Ranjit
ITS 4/20 BABYYYYy(I don t partake) 2024
A program that takes a list of marks and reports them as a historgram
"""


user_input = input("Enter a space-separated list of marks:\n")

marks = user_input.split(" ")
num_fails = 0
num_3  = 0
lower_2 = 0
upper_2 = 0
first = 0

#Dealing with the mark counting
for current_mark in marks:
    if(int(current_mark) < 50):
        num_fails+=1
    elif(50<=int(current_mark)<60):
        num_3+=1
    elif(60<=int(current_mark)<70):
        lower_2+=1
    elif(70<=int(current_mark)<75):
        upper_2+=1
    elif(int(current_mark) >= 75):
        first+=1

#coding the Axis
print("1 |" + "X"*first)
print("2+|" + "X"*upper_2)
print("2-|" + "X"*lower_2)
print("3 |" + "X"*num_3)
print("F |" + "X"*num_fails)