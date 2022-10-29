

amountDue = 50
while amountDue>0:
    print ("Amount due: ", amountDue)
    coin = int(input("Insert Coin: "))
    if coin in [5,10,25]:
        amountDue -=coin


changeOwed = abs(amountDue)
print("Change Owed: ", changeOwed)

