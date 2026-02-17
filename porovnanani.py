x = int(input ("Zadejte první číslo"))
y =int(input("Zadejte druhé číslo"))
if x > y:
    #print (x + "Je větší než " + y) Nefukční kvůli typům
    #print(x,"Je větší než " ,y)
    #print (str(x) + "Je větší než " + str(y)) možnost přetypenout
    print (f"{x} je větší než {y}")
elif x == y:
    print("Zadaná čísla jsou stejná")
else:
    print (f"{y} je větší než {x}") 