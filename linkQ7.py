# Q6.Write a Python program to print the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8].


def even_num(list):
    list2=[]
    for i in range(len(list)):
        if list[i]%2==0:
            list2.append(list[i])
    return(list2)

list=[1, 2, 3, 4, 5, 6, 7, 8, 9]
even=even_num(list)
print(even)

