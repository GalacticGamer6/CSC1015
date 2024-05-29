sentence = input("Enter a sentence:\n")
formatted_sentence = sentence + " "

output = ""
#the algorithm extracts each word between spaces
#now that we have the fromatted sentenc(added a space at the end), the find method can pull the last word
#the algorithm will take the first word (ending before a space) and add that to a variable called output, sperated by a ,
#the sentence will then be cut by the word that was just added
#this cycle repeats
for i in range(formatted_sentence.count(" ")):
        output += formatted_sentence[0:formatted_sentence.find(" ")].lower() + ", "
        formatted_sentence = formatted_sentence[formatted_sentence.find(" ") + 1:]

#going to -2 so we can get rid of the last comma, then we just add the full stop
print("The word list:",output[0:-2] + ".")