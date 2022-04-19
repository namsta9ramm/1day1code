array=[8,5,2,3,7,22,57]

def selection_sort(array):
    n=len(array)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if array[j]<array[min_index]:
                min_index=j
        array[i],array[min_index]=array[min_index],array[i]
    print(array)

selection_sort(array)
