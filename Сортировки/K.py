home=list(map(int,input().split()))
taxi=list(map(int,input().split()))
home.sort(reverse=True)
taxi.sort()
summ=0
for i in range(0,len(home)):
    summ+=home[i]*taxi[i]
print(summ)