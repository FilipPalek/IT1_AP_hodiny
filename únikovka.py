import random
unik = False
pokusy = 3

tajný_kod = str(random.randint(100,999))

while pokusy > 0 and not unik:
    print("Máš", pokusy, "pokusy.")
    print("1 - Prohledat stůl")
    print("2 - Zkusit otevřít dveře")
    print("3 - Podívat se pod koberec\n")

    volba = input("Co uděláš?")

    if volba == "1":
        print("Našel jsi kod", tajný_kod)
    elif volba == "2":
        kod = input("Zadejte kod")
        if kod == tajný_kod:
            unik = True
        else: 
            print("Špatný kod")
            pokusy = pokusy -1
    elif volba == "3":
        print("Nic tu není.")
    else:
        print("Neplatná možnost")

if unik == True:
    print("Unikl jsi")
else:
    print("Prohrál jsi")
    