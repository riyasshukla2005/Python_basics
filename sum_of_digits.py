num = int(input("enter a number: "))
def sumOfDigits(num):
    sum = 0
    while(num!=0):
        digit = num%10
        sum += digit
        num //= 10
    
    return sum

print(sumOfDigits(1234))