# This program will determine the type of an animal based on a simple classification scheme
#
# RNJNEE001
#

number = int(input("Enter a number:\n"))
proper_divisiors = "The proper divisors of "+ str(number)+ " are:\n"
number_check = 0
for i in range(1,number):
    if number%i == 0 & i != number:
        number_check += i
        proper_divisiors = proper_divisiors + str(i) + " "

print(proper_divisiors)
print("")

if number_check == number:
    print(str(number),"is a perfect number.")
else:
    print(str(number),"is not a perfect number.")

