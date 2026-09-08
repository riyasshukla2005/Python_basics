num = int(input("enter range: "))
def prime_numbers(num):
    for i in range(1,num+1):
        for j in range(2,int(i**0.5)+1):
            if (i%j==0):
                break
        else:
            print(i,end=" ")
            
print(prime_numbers(num))