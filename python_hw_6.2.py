x = input("Name: ")
if x[0].islower():
    print("Errore")
for i in range(1, len(x)):
    if x[i].isupper():
        print("Errore")
        break
for a in x:
    if a.isalpha():
        continue
    print("Errore")