class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        operations,k=[],[]
        c,s=0,0
        while c!=n and s<len(target):
            c+=1
            k.append(c)
            operations.append('Push')
            if target[s]==k[-1]:
                s+=1
                continue
            else:
                k.pop()
                operations.append('Pop')
        return operations
