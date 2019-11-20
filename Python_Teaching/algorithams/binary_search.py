def binarysearch(arr, x, l, r):

    if r>=1:
        mid = int(l+(r-l)/2)
        if arr[mid] == x:
            return mid
        elif arr[mid] >x:
            return binarysearch(arr, x, l, mid-1)
        elif arr[mid] <x:
            return binarysearch(arr, x, mid+1, r)

def binarysearchiter(arr, x, l, r):
    trip = 0
    while l <= r:
        mid = int((l+r)/2)
        print(f"mid value is {mid}")
        print(f"l value is {l}")
        print(f"r value is {r}")

        if arr[mid] == x:
            print(f"This is {trip}'d trip'")
            return mid
        elif arr[mid] < x:
            l = mid +1
            trip += 1
            print(f"This is {trip}'d trip'")
        else:
            r = mid -1
            trip += 1
            print(f"This is {trip}'d trip'")


arr = [1,2,3,4,8,9,10,12]
x = 8

result = binarysearchiter(arr, x, 0, len(arr)-1 )
print(result)