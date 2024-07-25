def is_perfectno(n):
    if n<=0:
        return False
    sum_of_div=0
    for i in range(1,n):
        if n%i==0:
            sum_of_div+=i

    if n==sum_of_div:
        print(f"{n} is a perfect number")
    else:
        print(f"{n} is not a perfect number")

n=int(input("Enter a number:"))
is_perfectno(n)