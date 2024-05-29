# Given a word, calculate how many syllables it contains.

def is_vowel(letter):
    if letter in "aeiouy":
        return True
    else:
        return False

def next_vowel(word,index):
    for i in range(index,len(word)):
        if is_vowel(word[i]):
            return i

    return len(word)

def count_syllables(word):
    count = 0
    i = 0

    while i< len(word)-2:
        i = next_vowel(word, i)
        print("i: ",i)
        if(i== len(word)-1 and word[i]=="e"):
            if(count==0):
                count = 1
            else:
                break
        elif i!= len(word)-1 and is_vowel(word[i+1]):
            print(word[i])
            count+=1
            i+=2
        else:
            count+=1
            i+=1
    return count

def main():
    word = ""
    while word!= 'q':
        word = input('Enter a word (or \'q\' to quit):\n')
        print("The word",word,"has",count_syllables(word))

# Do not modify.
if __name__ == '__main__':
    main()