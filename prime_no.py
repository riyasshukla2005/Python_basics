num = 7
def prime(num):
    for i in range(2,num):
        if (num%i==0):
            return "Not Prime"
        else:
            return "Prime"
        
print(prime(num))