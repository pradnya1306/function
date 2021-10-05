# Sample String : "1234abcd"
# Output : "dcba4321".
# SampleString="1234abcd"

def samplestring():
    list=[]
    for i in range(len(string)):
        list.append(string[i])
   
    i=len(list)-1
    list2=[]
    while i >=0:
        list2.append(list[i])
        i-=1
    # print(list2)
    k=str("".join(list2))
    return(k)

string="1234abcd"
m=samplestring()
print(m)