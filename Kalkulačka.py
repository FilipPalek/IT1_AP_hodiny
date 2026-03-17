while(True):
 clen1 = int(input("Zadejte člen."))
 clen2 = int(input("Zadejte druhý člen"))

 print("1. Součet \n2. Součin \n3. Rozdíl \n4.")
 operace = input("Vyberte číslo operace, kterou chcete provést")

 match operace:
   case 1:
    soucet = clen1 + clen2
    print(soucet)
   case 2:
     soucin = clen1 * clen2
     print(soucin)
   case 3:
     rozdíl = clen1 - clen2
     print(rozdíl)
   case 4:
     if clen2 == 0:
      print("Nelze dělit nulou!")
     else:
      podíl = clen1 / clen2
      print(podíl)

 konec = input("Přejete si ukončit program Y/N")
 if konec.lower() == "y":
   break