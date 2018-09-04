comparisons = 0

def Partition(A,l,r,q):

    global comparisons
    comparisons = comparisons + (r-l) -1

    #Base.  How low can you go.
    if (l >= r):
        return -1

    # Question 0
    if q == 0:
        p = l
    # Question 1
    elif q == 1:
        p = r-1
    # Question 2
    else:
        a = A[l]
        c = A[r-1]
        b = A[r//2]
        if a > b:
            if a < c:
                p = l
            elif b > c:
                p = r//2
            else:
                p = r-1
        else:
            if a > c:
                p = l
            elif b < c:
                p = r//2
            else:
                p = r-1

            
            
       
    #Swap pivot with first slot
    A[l],A[p] = A[p],A[l]
    p = l
    
    i = l + 1 # i is for placement
    j = i # j is for comparison
    #p is the pivot for comparison
    
    while j < r:     
        if A[j] < A[p]:
            A[j],A[i] = A[i],A[j]
            i=i+1
        j=j+1
    #Swap i and p to divide the partitioned space
    A[i-1],A[p] = A[p],A[i-1]
    return  i-1

## QuickSort
## if n = 1 return
## p = ChoosePivot(A,n)
## parition A around p
## RecursivelySort(First Part < p)
## RecursivelySort(Second Part > p)
def QuickSort(A,l,r,q):

    #TODO: ncluding exchanging the pivot element with the first element just before the main Partition subroutine)
    p = Partition(A,l,r,q)

    if(p >= 0):
        QuickSort(A,l,p,q)
        QuickSort(A,p+1,r,q)

    return A

orgA = [3,8,2,5,1,4,7,6]
orgA = [54,26,93,17,77,31,44,55,20]
orgA = [54044,14108,79294,29649,25260,60660,2995,53777,49689,9083,16122,90436,4615,40660,25675,58943,92904,9900]


with open("IntArray.txt") as f:
    orgA = [int(digit.strip()) for digit in f]

#Three Questions for this assignment
questions = [0,1,2]

for q in questions:
    A = orgA.copy()
    r = len(A)
    QuickSort(A,0,r,q)

    print("Question",q,"Total number of comparions:",comparisons)
    
    file_name = "sorted_" + str(q) + ".txt"
    with open(file_name,mode='w') as of:
        for item in A:
            of.write("%s\n" % item)
    comparisons = 0    

#print(A)
#print(A[:100])
#print(A[-100:])

