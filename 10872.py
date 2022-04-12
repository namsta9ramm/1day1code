#재귀를 사용하여 팩토리얼 해결하기
k=int(input())
def factorial(k):
    if k==0:
        return (1)
    else: 
        return k*factorial(k-1)
print(factorial(k))