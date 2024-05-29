#Neeraav Ranjit
#A program to test whether a word is a pallindrome
#22/04/2024


def check_palindrome(s):
    if len(s) <= 1:
        return True
    else:
        #just checking if outer chars are equal
        if s[0] == s[-1]:
            return check_palindrome(s[1:-1])
        else:
            return False

def main():
    s = input("Enter a string:\n")

    if(check_palindrome(s)):
        print("Palindrome!")
    else:
        print("Not a palindrome!")

main()