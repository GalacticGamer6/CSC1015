# Neeraav Ranjit
# 05/05/2024
# A program t find anagrams from a some given text in a text file

def check_anagram(target,current_word):
    #crates an entry of all the letter occourences in the target and current word to compare later
    target_occourences = {}
    current_word_occourences ={}

    for char in target:
        if char not in target_occourences:
            target_occourences[char] = 1
        else:
            target_occourences[char] += 1

    # print(target, target_occourences,sep="\t")

    #now we do the same for the current_word
    for char in str(current_word).rstrip():
        if char not in current_word_occourences:
            current_word_occourences[char] = 1
        else:
            current_word_occourences[char] += 1

    # print(current_word, current_word_occourences,sep="\t")

    if target_occourences == current_word_occourences:
        return True
    else:
        return False

if __name__ == '__main__':

    file = open("EnglishWords.txt","r")

    print("***** Anagram Finder *****")
    target = input("Enter a word: ")

    #store the anagrams
    anagrams = []


    for line in file:
    #checking if the line is an actual word and not the junk in the beginning
    #do this by splitting the sentence into words, if the length is 1, then it is a word, and we will anagram check
        current_line = line.split()
        if len(current_line) == 1:
            if check_anagram(target,str(line)):
                anagrams.append(line.rstrip())
            else:
                continue

    #there will be a dupliacte target added to the list, just remove it
    anagrams.remove(target)
    if len(anagrams) == 0:
        print("Sorry, anagrams of " + "\'"+target+"\'"+ " could not be found.")
    else:
        print(anagrams)