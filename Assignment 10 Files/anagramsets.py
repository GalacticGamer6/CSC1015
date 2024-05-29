output = []
#Mise en place
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




#first lets get the word length
word_length = eval(input("Enter word length:"))

words = []

file = open("EnglishWords.txt","r")
#first get all n letter words
for line in file:
    # checking if the line is an actual word and not the junk in the beginning
    # do this by splitting the sentence into words, if the length is 1, then it is a word, and we will anagram check
    current_line = str(line).split()
    if len(current_line) == 1:
        if len(str(line).rstrip()) == word_length:
            words.append(str(line).rstrip())

# print("1st",words)
#take those words and find anagrams
#gonna use that find anagram function we cooked earlier n question 1 to help us
#we can also just use the entiretiy of question 1 for the next bit

#for this next bit we essentially just have to loop through each word in the n letter list and see if is has anagrams. Basically a mini question 1. We then add this and its annagam to another list , and add that to a big list, and then order it
for current_word in words:
    anagrams_of_current_word = []
    for i in range(len(words)):
        if current_word == words[i]:
            continue
        if check_anagram(current_word,words[i]):
            anagrams_of_current_word.append(str(words[i]).rstrip())
            # print(current_word, words[i])
        output.append(anagrams_of_current_word)
output.sort()
print(output)
# print(words)
# print(output)
