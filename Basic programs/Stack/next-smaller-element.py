ns=[0]*len(nums)
trash=[]
ns[-1]=len(nums)
trash.append(len(nums)-1)
i = len(nums)-2
while i>=0:
    while trash and nums[trash[-1]]>=nums[i]:
        trash.pop()
    if not trash:
        ns[i] = len(nums)
    else:
        ns[i] = trash[-1]
    trash.append(i)
    i-=1 
print(ns)
