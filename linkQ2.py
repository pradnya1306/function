# Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Output : 20.


def sum(num):
    i=0
    sum=0
    while i<len(list):
        sum=sum+list[i]
        i=i+1
    return(sum)

list=[8, 2, 3, 0, 7]
mainsum=sum(list)
print (mainsum)