sentence = input("Enter a sentence:\n")
#format the sentence so that we have another space to target words using the find method
formatted_sentence = sentence + " "

current_word = ""
output =""

for i in range(formatted_sentence.count(" ")):
    #get the current word
    current_word = formatted_sentence[0:formatted_sentence.find(" ")]
    #for the vowel case
    if current_word[0] in "aeiou":
        #seems simple enough right?
        output+= current_word + "way "
    else:
        #Here, i basically want to extract the consonants
        cons_sequence = ""
        i = 0
        #use a while loop to scan each chaarcter until we hit a vowel, adding the non vowel to a varialb ewhich we can just add to the word later(for pig latin)
        while current_word[i] not in "aeiou":
            cons_sequence += current_word[i]
            i+=1
        #Here im must putting the rest of the word(starting from where the vowel starts, which is tracked by i) with the prefix "a" , followed by the consonants , followed by "ay"
        output += current_word[i::] + "a" + cons_sequence + "ay" + " "
        #here i remove the word we just used from our formatted sentence, so that we can track from the 0th position to the first space (1 word) again
    formatted_sentence = formatted_sentence[formatted_sentence.find(" ") + 1:]
print(output.lower())
