num=int(input("Dame un número entero positivo "))
output="La cuenta atrás es: "
while num>=0:
    output+=str(num)+","
    num=num-1
print(output)