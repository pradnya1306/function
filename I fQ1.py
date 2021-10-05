def eligible_for_vote(age):
    if age>=18:
        print("you are eligible")
    else:
        print("not eligible")

age=int(input("enter the age:"))
eligible_for_vote(age)