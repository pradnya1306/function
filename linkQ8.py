# Write function bmi that calculates body mass index (bmi = weight / height2).

# if bmi <= 18.5 return "Underweight"

# if bmi <= 25.0 return "Normal"

# if bmi <= 30.0 return "Overweight"

# if bmi > 30 return "Obese"

def function_bim(weight,height):
    bmi=weight/height
    if bmi<=18.5:
        return("underweight")
    if bmi<=25.0:
        return("normal")
    if bmi<=30.0:
        return("overweight")
    if bmi>30 :
        return("obese")

weight=int(input("enter the weight : "))
height=int(input("enter the height : "))
calculate =function_bim(weight,height)
print(calculate)
