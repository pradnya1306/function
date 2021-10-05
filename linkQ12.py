# .Write a function to check if a number is prime or not.
def prime_number():
    i=1
    count=0
    while i<=num:
        if num%i==0:
            count=count+1
        i+=1
    if count==2:
        print(" prime number")
    else:
        print("not prime number")

num=int(input("enter the number :"))
prime_number()