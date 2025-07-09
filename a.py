import wifilists as wifi

def getnum(num)->str:
    num=int(num)
    if num>80 and num<=100:
        return '5'
    elif num>60 and num<=80:
        return '4'
    elif num>40 and num<=60:
        return '3'
    elif num>20 and num<=40:
        return '2'
    else:
        return '1'
    

listt=wifi.listwifi()
SavedAndAvailable=listt[0]
Available=listt[1]
print("Available and saved : ")
for i in SavedAndAvailable:
    print(getnum(SavedAndAvailable[i]),i)

print("Available : ")
for i in Available:
    print(getnum(Available[i]),i)
