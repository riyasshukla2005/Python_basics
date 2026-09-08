num = int(input("enter a number: "))
def count_digits(num):
    count = 0
    while(num!=0):
        digit = num%10
        count += 1
        num //= 10
        
    return count

print(count_digits(num))