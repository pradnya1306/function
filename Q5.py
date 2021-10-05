# def chek_numbers():
#     num1=int(input("enter the 1st number"))
#     num2=int(input("enter the 2nd number"))
#     if num1 and num2%2==0:
#         print("both are even numers")
#     else:
#         print("both are not even numbers")

# chek_numbers()

def chek_numbers(num1,num2):

    if num1%2==0 and num2%2==0:
        print("both are even numers")
    else:
        print("both are not even numbers")

# chek_numbers(5,8)
def check_number_list():

    # i=0
    for i in range(len(list1)):
        num1=list1[i]
        num2=list2[i]
        chek_numbers(num1,num2)
      
        i=i+1

list1=[2,6,18,10,3,75]
list2=[6,19,24,12,3,87]
check_number_list()

