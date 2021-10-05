# Q9.Write a Python program to generate and print a list of first and 
# last 5 elements where 
#   the values are square of numbers between 1 and 30 (both included).
# Output :-([1, 4, 9, 16, 25], [676, 729, 784, 841, 900]).
# def square():
list=[1,4,9,16,25,36,49,64,81,100,121,144,169,196,225,256,269,324,361,400,441,484,529,576,625,676,729,784,841,900]
i=0
a=[]
m=[]
while i<5:
    a.append(list[i])
    j=25
    b=[]
    while j<30:
        b.append(list[j])
        j+=1
    i=i+1
m.append(a)
m.append(b)
print(m)

        