time = input("Enter the date and time (yyyy-mm-dd hh:mm):\n")

year = time[2:4]
month = time[5:7]
day = time[8:10]

hour = int(time[11:13])
minute = (time[14:16])

suff = ""

if(day[1] == "1"):
    if(day == "11"):
        suff = "th"
    else:
        suff = "st"
elif(day[1] == "2"):
    suff = "nd"
elif(day[1] == "3"):
    suff = "rd"
else:
    suff = "th"

pre = ""

if 0<hour<12:
    pre = "am"
elif hour == 12:
    pre = "pm"
elif hour == 12 and (1 <= int(minute) <= 59):
    pre = "pm"
elif hour == 0 and (1 <= int(minute) <= 59):
    hour+=12
    pre = "am"
elif hour == 0:
    pre = "am"
    hour+=12
else:
    hour = int(hour)
    hour-=12
    pre = "pm"

month_in_words = ""

if(month == "01"):
    month_in_words = "January"
elif(month == "02"):
    month_in_words = "February"
elif(month == "03"):
    month_in_words = "March"
elif(month == "04"):
    month_in_words = "April"
elif(month == "05"):
    month_in_words = "May"
elif(month == "06"):
    month_in_words = "June"
elif(month == "07"):
    month_in_words = "July"
elif(month == "08"):
    month_in_words = "August"
elif(month == "09"):
    month_in_words = "September"
elif(month == "10"):
    month_in_words = "October"
elif(month == "11"):
    month_in_words = "November"
elif(month == "12"):
    month_in_words = "December"

print(hour,":",minute," ",pre," on the ",int(day),suff," of ",month_in_words," '",year,sep="")


