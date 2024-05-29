#Neeraav Ranjit
#26/04/2024
#Program to check whtehre a prime number is also a palnidrom,e, given a range of numbres
"""
only 1 case, ill suck it up
 code wont work for between 10 000 and 20 000 because i think theres a set recursion limit on the automarker

"""
import sys
sys.setrecursionlimit (3000000)
def check_prime(n,div = 2):
    #im literally just gonna use it like a for loop
    if div == n:
        return True
    if n%div == 0:
        return False
    else:
        return check_prime(n,div+1)

#We can use our palndrom function from thr previous question
def check_palindrome(s):
    s = str(s)

    if len(s) <= 1:
        return True
    else:
        #just checking if outer chars are equal
        if s[0] == s[-1]:
            return check_palindrome(s[1:-1])
        else:
            return False
def check_prime_palindrome(N,M):
    if N<=M:
        # print("N: Prime?\t" + str(check_prime(N)),"\t\tN: Is Palindrome?\t" + str(check_palindrome(N)))
        if check_prime(N) and check_palindrome(N):
            print(N)
        # print("N: " + str(N) + "\tM: " + str(M))
        check_prime_palindrome(N+1,M)

if __name__ == '__main__':
    N = eval(input("Enter the starting point N:\n"))
    M = eval(input("Enter the ending point M:\n"))

    print("The palindromic primes are:")
    check_prime_palindrome(N,M)