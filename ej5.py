amount=int(input("Dime la cantidad que deseas invertir "))
interes=int(input("Dime el interés anual "))
years=int(input("Dime el número de años "))
for i in range(1, years+1):
    ben=amount*(interes/100)*i
    print("El capital obtenido en el "+str(i)+" año es de "+str(amount+ben))