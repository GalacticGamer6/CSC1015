first_name = input("Enter first name:\n")
last_name = input("Enter last name:\n")
inheritance = eval(input("Enter sum of money in USD:\n"))
country = input("Enter country name:\n\n")

print("Dearest ", first_name, "\nIt is with a heavy heart that I inform you of the death of my father,"
                             "\nGeneral Fayk ", last_name, ", your long lost relative from Mapsfostol."
                             "\nMy father left the sum of ",inheritance,"USD for us, your distant cousins."
                             "\nUnfortunately, we cannot access the money as it is in a bank in ",country,"."
                             "\nI desperately need your assistance to access this money."
                             "\nI will even pay you generously, 30% of the amount - ", 0.3*inheritance,"USD,"
                             "\nfor your help.  Please get in touch with me at this email address asap."
                             "\nYours sincerely\nFrank ",last_name, sep="")