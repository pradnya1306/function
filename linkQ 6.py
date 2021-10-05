# Q5.Write a Python function that takes a list and returns a new 
# list with unique elements of the first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5].

def unique_list(samplelist):
    
    i=0
    list=[]
    while i<len (SampleList):
        j=0
        while j<len(SampleList):
            if SampleList[i]==SampleList[j]:
                if SampleList[i]not in list:
                    list.append(SampleList[i])
            j=j+1

        i=i+1
    return(list)


SampleList=[1,2,3,3,3,3,4,5]
new_list=unique_list(SampleList)
print(new_list)