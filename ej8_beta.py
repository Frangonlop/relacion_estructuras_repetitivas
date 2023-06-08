num=int(input("Dame un número: "))
num_found=[]
n=0
while len(num_found)<num:
    if n%2==1:
        num_found.append(n)
    n+=1
print(num_found)