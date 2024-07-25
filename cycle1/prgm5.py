def armstrong(num):
    n=num
    no_of_digits=len(str(n))
    sum=0;
    while n>0:
        digit=n%10
        sum+=digit**no_of_digits
        n//=10
    return sum==num

upper_limit=int(input("Enter the number:"))

for num in range(1,upper_limit+1):
    if armstrong(num):
        print(num)