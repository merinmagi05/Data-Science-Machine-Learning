
def is_prime(num):
    if num<=1:
        return False
    if num==2:
        return True
    if num%2==0:
        return False
    # checking divisibility using factors
    sqrt_num=int(num**0.5)+1
    for i in range(3, sqrt_num, 2):
        if num %i==0:
            return False
    return True




start=int(input("Enter the starting number:"))
end=int(input("Enter the ending number:"))

non_prime=[]
for num in range(start, end+1):
    if not is_prime(num):
        non_prime.append(num)
if non_prime:
    print("Non prime numbers are in interval of [{} ,{} ]:{}".format(start,end,non_prime))