num=int(input("Dame un  número "))
output="Los impares son: "
for i in range (1, num+1):
    if i%2!=0:
        output = output + str(i)+ ","
print(output[:len(output)-1])