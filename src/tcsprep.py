def sec_largest(arr):
    sec_largest,largest=float(),float()
    for num in arr:
        if num>largest:
          largest=num
        elif num>sec_largest and num<largest :
           sec_largest=num
    return sec_largest
arr=[1]
res=sec_largest(arr)
print("anser is ",res )