def binsearch(a,l,h,k):
    if l<=h:
        mid=(l+h)//2
        if a[mid]==k:
            return True
        elif a[mid]<k:
            return binsearch(a,mid+1,h,k)
        elif a[mid]>k:
            return binsearch(a,l,mid-1,k)
    return False
a=[1,2,3,4,5,6,7,8]
k=6
l=0
h=len(a)-1
c=binsearch(a,l,h,k)
print(c)