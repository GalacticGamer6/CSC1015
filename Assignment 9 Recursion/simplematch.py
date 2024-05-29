#Neeraav Ranjit
#27/04/2024
#A program to test ? wildcards and match words
def match(pattern,word):

    #Base cases
    if len(pattern) == 0 and len(word) == 0:
        return True
    elif len(pattern) == 0 and len(word)!= 0:
        return False
    elif len(pattern) != 0 and len(word) == 0:
        return False
    else:
        if pattern[0] == '?':
        #just going 1 by 1 and seeing if lengths are equal
            return match(pattern[1:],word[1:])
        #if not a ?, then its immediately false
        elif word[0]!=pattern[0]:
            return False
        #otherwise the strings are perfectly equal
        else:
            return match(pattern[1:],word[1:])

#not me wasting 3 days until i realize you dont need a main method