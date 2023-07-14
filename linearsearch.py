def LinearSearch(arr,k):
    count=0
    for i in arr:
        if i==k:
            count+=1
    return count

arr=list(map(int,input().split()))
k=int(input())
print(LinearSearch(arr,k))