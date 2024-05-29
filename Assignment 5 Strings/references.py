unformatted = input("Enter the reference:\n")
print("Reformatted reference:")
# the brackets of the year will assist a lot
authors_end_pos = unformatted.find("(")
authors  = unformatted[0:authors_end_pos]
print(authors.title(),end="")

year = unformatted[unformatted.find("("):unformatted.find(")") + 1]
print(year,end=" ")

# now we need the titled
title = unformatted[unformatted.find(")") + 2:unformatted.find(",",unformatted.find(",") + 1)]
print(title.capitalize(),end="")

#now the rest
rest = unformatted[unformatted.find(",",unformatted.find(",")  +3):len(unformatted)]
print(rest,end="")
