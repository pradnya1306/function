def showNumbers(limit):
    i=0
    while i<=limit:
        if i%2==0:
            print(i,"is even number")
        else:
            print(i,"is odd number")
        i=i+1
     
limit=int(input("enter the limit"))
showNumbers(limit)