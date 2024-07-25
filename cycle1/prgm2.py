def fibonacci_no(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        a,b=0,1
        print(a)
        for i in range(2,n+1):
            print(b)
            temp=a+b
            a=b
            b=temp
        return b


n=int(input("Enter  the value for n:"))
fibonacci_no(n)