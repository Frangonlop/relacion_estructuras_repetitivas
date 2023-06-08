word=input("Dame una palabra y te la mostrare letra por letra empezando por el final: ")
for i in range(len(word)-1, -1, -1):
    print(word[i])