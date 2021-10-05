#  Write a function For example, if we give 9119  the function should return  
#  811181, as the  square of 9 is 81 and square of 1  is 1.
# a=[]
# num=int(input("enter the number"))
# a.append(num)
# print(a)

num=input("enter the number")
i=0
new_list=[]
while i<len(num):
    squre=int(num[i])**2
    new_list.append(str(squre))
    i=i+1
# print(new_list)

print(''.join(new_list))




