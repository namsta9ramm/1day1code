a=int(input())
array_ans=[]
for _ in range(a):
    k=int(input())
    array_ans.append(k)
# 분할정복과 재귀를 이용한 알고리즘
# len array= 9 
def merge_sort(array):
	if len(array) < 2:
		return array
	mid = len(array) // 2
	low_arr = merge_sort(array[:mid])
	high_arr = merge_sort(array[mid:])
    #[8][4][6][2][9][1][3][5]
	merged_arr = []
	l = h = 0
	while l < len(low_arr) and h < len(high_arr):
		if low_arr[l] < high_arr[h]:
			merged_arr.append(low_arr[l])
			l += 1
		else:
			merged_arr.append(high_arr[h])
			h += 1
	merged_arr += low_arr[l:]
	merged_arr += high_arr[h:]
	
	return merged_arr
array = print(merge_sort(array_ans))