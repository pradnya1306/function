# part-1
def calculator(num1,num2,opration):
    if opration=="+":
        sum=(num1)+(num2)
        print(sum)
    elif opration=="-":
        substract=num1-num2
        print(substract)
    elif opration=="*":
        multiply=num1*num2
        print(multiply)
    elif opration=="/":
        division=num1/num2
        print(division)
    else:
        print("none")


# calculator (20,25,"+")
# calculator(40,3,"-")
# calculator(10,4,"*")
# calculator(40,4,"/")
# calculator(50,60,"*")
# calculator(80,120,"/")
# calculator(90,23,"-")

# part-2

def calculator(opration):
    if opration=="+":
        add_result=(num1)+(num2)
        return(add_result)
    elif opration=="-":
        subtract_result=num1-num2
        return(subtract_result)
    elif opration=="*":
        multiply_result=num1*num2
        return(multiply_result)
    elif opration=="/":
        divide_result=num1/num2
        return(divide_result)
    else:
        print("none")

num1=int(input("enter the 1st number"))
num2=int(input ("enter the 2nd number"))
opration=input("enter the opration")
add_result=calculator("+")
print(add_result)
subtract_result=calculator("-")
print(subtract_result)
multiply_result=calculator("*")
print(multiply_result)
divide_result=calculator("/")
print(divide_result)

# # part-3

# def list_change(list1=[5,10,50,20],list2=[2,20,3,5]):
#     multiple_list=[]
#     for i in range( len(list1)):
#         # for j in range (len(list2)):
#         num1=list1[i]
#         num2=list2[i]
#         multiply_result=calculator()
#         multiple_list.append(multiply_result)
         
# list_change()


