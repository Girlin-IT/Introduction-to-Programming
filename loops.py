num = int(input("Enter a non negative number: "))
factor = 1

for i in range (1, num+1):
    factor = factor*i
    print(i,":", factor)


