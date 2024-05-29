n = eval(input("Enter a number between -6 and 2:\n"))

if not(-6<n<2):
    print("Invalid input! The value of 'n' should be between -6 and 2.")
else:
    for i in range(42):
        if(i % 7==0):
            if(0<=n+i<=9):
                print("",n+i)
            else:
                print(n + i, end="\n")