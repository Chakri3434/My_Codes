nums=[6,2,5,4,1,5,6]
ps=[]
trash=[]
ps.append(-1)
trash.append(0)
for i in range(1,len(nums)):
    while trash and nums[trash[-1]]>=nums[i]:
        trash.pop()
    if not trash:
        ps.append(-1)
    else:
        ps.append(trash[-1])
    trash.append(i)
print(ps)
