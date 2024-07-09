def largestHist(nums):
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
    
    res=0
    for i in range(len(nums)):
        curr = nums[i]
        curr +=(i-ps[i]-1)*nums[i]
        curr +=(ns[i]-i-1)*nums[i]
        res=max(res,curr)
    return res
    
def largestRect(mat):
    res=largestHist(mat[0])
    for i in range(1,len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j]==1:
                mat[i][j]+=mat[i-1][j]
        res=max(res,largestHist(mat[i]))
    return res
    
# mat=[[0,1,1,0],[1,1,1,1],[1,1,1,1],[1,1,0,0]]
mat = [[1,0,0,1,1],[0,0,0,2,2],[1,1,1,3,3],[0,2,2,4,4]]
print(largestRect(mat))
