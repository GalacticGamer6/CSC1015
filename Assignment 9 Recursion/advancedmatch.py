#Neeraav Ranjit
#25/04/2024
#A program see if a word matches a word with the ? and * wildcards
#this doesnt work properly, needa brush up on recursion, still cloudy

def match(pattern, word):
    #base cases
    if len(pattern) == 0 and len(word) == 0:
        return True
    elif len(pattern) == 0 and len(word)!= 0:
        return False
    #check if pattern contains a * or not
    elif pattern[0] == '*' and len(word) == 0:
        return True
    elif pattern == '*' and len(word) != 0:
        # If pattern starts with '*', recursively match the rest of the pattern with the word
        return True
    else:
        #sortring out the * cases
        if pattern[0] == '*':
            #matching rest of pattern to word, or pattern to rest of word
            return match(pattern[1:], word) or (len(word) > 0 and match(pattern,word[1:]))
        #sorting out the > cases. pretty much just a copy of simple match but me not being a peabrain and remembering how boolean algebra works
        elif pattern[0] == '?' or pattern[0] == word[0]:
            return match(pattern[1:], word[1:])
        else:
            return False

pattern = input("Enter a pattern:\n")
word = input("Enter a word:\n")
print(match(pattern,word))