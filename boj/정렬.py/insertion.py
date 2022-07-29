array=[8,5,2,1,3,13,18,45]

def insertion_sort(array):
    n=len(array)
    for i in range(1,n):
    # i = 0 , range(1,0,-1) i=7 range(7,0,-1)
        for j in range(i,0,-1):
            if array[j-1]>array[j]:
                array[j-1],array[j]=array[j],array[j-1]
    print(array)

insertion_sort(array)