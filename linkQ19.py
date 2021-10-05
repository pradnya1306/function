#  Consider an array/list of sheep where some sheep may be missing from 
#  their place. We need a function that counts the number of sheep present in 
#  the array (true means present).

# The correct answer would be 17.Hint: Don't forget to check for 
# bad values like null/undefined


def sheep():
    i=0
    count=0
    while i<len(example):
        if example[i]=="True":
            count=count+1
        i=i+1
    print(count)

example=['True', ' True', ' True',  'False',
'True',  'True',  'True',  'True' ,
'True',  'False', 'True',  'False',
'True',  'False', 'False', 'True' ,
'True',  'True',  'True',  'True' ,
'False', 'False', 'True',  'True']
sheep()
