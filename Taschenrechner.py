
rechenart = str (input("Welche Rechenart möchtest du benutzen?"))
zahl1 = int (input ("Welche erste Zahl möchtest du benutzen?"))
zahl2 = int (input ("Welche zweite Zahl möchtest du benutzen?"))

if rechenart == "+":
    print (f"{zahl1} {rechenart} {zahl2} = {zahl1+zahl2} ")
elif rechenart == "-":
    print(f"{zahl1} {rechenart} {zahl2} = {zahl1 - zahl2} ")
elif rechenart == "*":
    print(f"{zahl1} {rechenart} {zahl2} = {zahl1 * zahl2} ")
elif rechenart == "/":
     print(f"{zahl1} {rechenart} {zahl2} = {zahl1 / zahl2} ")
else:
     print ("kein gültiger Operator")