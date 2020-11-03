def partition(a,L,R):
    p = R
    i = L-1
    for j in range(L,R):
        if a[j] < a[p]:
            i +=1
            a[i],a[j] = a[j],a[i]
    a[i+1],a[p] = a[p], a[i+1]
    return i+1

def quickSort(a,L,R):
    if L < R:
        p = partition(a,L,R)
        quickSort(a,L,p-1)
        quickSort(a,p+1,R)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    a = list(map(int,input().split()))
    quickSort(a,0,N-1)
    print('#{} {}'.format(tc,a[N//2]))
