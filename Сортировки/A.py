def SelectionSort(a):
    for i in range(len(a)-1):
        max_index=i
        for j in range(i+1, len(a)):
            if a[j]>a[max_index]:
                max_index=j
        a[i],a[max_index]=a[max_index],a[i]

a=list(map(int,input().split()))
SelectionSort(a)
print(*a)
