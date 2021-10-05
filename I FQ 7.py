def function_name(string1,string2):
    if len(string1)==len(string2):
        print(string1)
        print(string2)
    elif len(string1)>len(string2):
        print(string1)
    else:
        print(string2)


string1=input("enter the string : ")
string2=input("enter the string : ")
function_name(string1,string2)
# function_name("sonu","monu")

