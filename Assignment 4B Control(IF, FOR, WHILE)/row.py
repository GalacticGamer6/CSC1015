n = eval(input("Enter a number between -6 and 93:\n"))

if not(-6<n<93):
    print("Invalid input! The value of 'n' should be between -6 and 93.")
else:
    for i in range(0,7):
        if(0<= n+i <= 9):
            print("",n + i, end=" ")
        else:
            print(n + i, end=" ")
