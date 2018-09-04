import operator;

inversions = 0

def mergeSort(alist):
    #print("Splitting ",alist)
    global inversions #I feel bad about this
    if len(alist)>1:
        mid = len(alist)//2
        right = alist[:mid]
        left = alist[mid:]

        mergeSort(left)
        mergeSort(right)

        i=0
        j=0
        k=0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                alist[k]=left[i]
                i=i+1
            else:
                inversions = inversions + (len(left) - i)
                #print (inversions)
                alist[k]=right[j]
                j=j+1
            k=k+1

        while i < len(left):
            alist[k]=left[i]
            i=i+1
            k=k+1

        while j < len(right):
            alist[k]=right[j]
            j=j+1
            k=k+1
    #print("Merging ",alist)

    

with open("IntArray.txt") as f:
    x = [int(digit.strip()) for digit in f]
#x = [1,3,5,2,4,6]
mergeSort(x)
print ("There are",inversions,"in",len(x),"samples")
with open("sorted-IntArray.txt",'w') as of:
    for digit in x:
        of.write(str(digit) + ",")
    
of.close()

#print (x)
