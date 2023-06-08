num=int(input("Dame un número, y te diré si es primo o no: "))
for i in range(2, num):
    if num%i==0:
        print("El número no es primo")
        break
    if num%i!=0:
        print("El número es primo")
        break