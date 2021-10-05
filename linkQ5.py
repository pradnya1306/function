# Q1.Write a Python program to count the number of strings where the 
# string length is 2     or more and the first and last characters are the 
# same from a given list of strings.
#  ist=['abc', 'xyz', 'aba', '1221']
# result= 2.


ist=['abc', 'xyz', 'aba', '1221']
i=0
list1=[]
while i<len(ist):
    if len( ist[i]) >2:
        # print(len(ist[i]))
        j=0
        count=0
        while j<len(ist[i]):
            if ist[i][j]==ist[i][(len(ist[i])-1)]:
                count=count+1

            j=j+1
        # if ist[i][j]==ist[i][(len(ist[i])-1)]:
                # count=count+1

    i=i=+1
print(count)