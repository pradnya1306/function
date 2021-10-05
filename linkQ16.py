# Write a function that prints all the prime numbers between 0 and limit where 
# limit is a parameter.

def prime_number():
    i=1
    while i<=num:
        j=1
        count=0
        while j<=num:
            if i%j==0:
                count=count+1
            j=j+1
        
        if count==2:
            print(i,"is prime number")
        else:
            print(i,"not prime number")
        i=i+1


num=int(input("enter the number"))
prime_number()


