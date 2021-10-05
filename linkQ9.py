# 8.Write a Python function that accepts a string and calculate the 
# number of upper case letters and lower case letters. Go to the editor
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Uppercase characters : 3
# No. of Lower case Characters : 12

def letter():
    string ='The quick Brow Fox'
    i=0
    count=0
    count1=0
    while i<len(string):
        if string[i]>="A" and string[i]<="Z":
            count=count+1
        elif string[i]>="a" and string[i]<="z":
            count1=count1+1
        i+=1
    print("uppercase character",count)
    print("lowercase chracter",count1)

string ='The quick Brow Fox'
letter()

