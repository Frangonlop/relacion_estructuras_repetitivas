sentence=input("Dame una frase: ")
letter=input("Dame una letra: ")
cont=0
for i in range(1, len(sentence)):
    if sentence[i]==letter:
        cont=cont+1
print("La letra "+str(letter)+" aparece "+str(cont)+" veces en la frase")