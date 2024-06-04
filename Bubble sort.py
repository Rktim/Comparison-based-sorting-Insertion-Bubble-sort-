def bubble(a):
    n=len(a)
    for i in range (n-1):
        for j in range (0,n-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a

ar=[11,2 ,4,1,6]
print("output:",bubble(ar))