def perfect(num):
    
    i=1
    sum=0
    while i<num:
        if num%i==0:
            sum=sum+i
        i=i+1
    print(sum)
    if sum==num:
        print("perfect number")
    else:
        print("not perfect number")

num=int(input("enter the number"))
perfect(num)

def perfect():
    start=int(input("enter the number"))
    end=int(input("enter the number"))
    j=start
    while j<=end:
        i=1
        sum=0
        while i<j:
            if j%i==0:
                sum=sum+i
            i=i+1
        if sum==j:
            print("perfect number",j)
        j=j+1


perfect()


