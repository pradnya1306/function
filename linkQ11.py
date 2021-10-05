# mplement a function named generateRange(min, max, step), which takes three 
# arguments and generates a range of integers from min to max, with the step. 
# The first integer is the minimum value, the second is the maximum of the range and
#  the third is the step. (min < max)

# Task
# Implem# generate_range(2, 10, 2) # should return list of [2,4,6,8,10]
# generate_range(1, 10, 3) # should return list of [1,4,7,10]
# generate_range(2, 10, 2) # should return array of [2, 4, 6, 8, 10]
# generate_range(1, 10, 3) # should return array of [1, 4, 7, 10]
# Note
# min < max
# step > 0
# the range does not HAVE to include max (depending on the step)
def list():
    list1=[]
    for i in range(min,max,step):
        list1.append(i)
    return(list1)

min=int(input("enter the number :"))
max=int(input("enterv the number :"))
step=int(input("enter the number :"))
list1=list()
print(list1)

         