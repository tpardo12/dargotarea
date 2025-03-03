def sol(l1, l2, i ,j,t):
    ret = 0
    if i < 0 and j >= 0:
        return j + 1 
    elif j < 0 and i >= 0:
        return i + 1
    if i >= 0 and j >=0 :
        curr = t[i][j]
        if curr != 1000:
            ret = curr
        else : 
            if  l1[i] == l2 [j]:
                curr = sol(l1,l2,i-1,j-1,t)
                t[i][j] = curr
                ret = curr
            else: 
                curr = min( sol(l1,l2,i-1,j,t) + 1, sol(l1,l2,i,j-1,t) + 1 )
                t[i][j] = curr
                ret = curr
        
    return ret

def listas (l1, l2):
    al1 = len(l1) -1
    al2 = len(l2) -1 
    t = [[1000 for i in range(al1 +1)] for j in range((al2) +1 )]
    ret = sol(l1,l2,al1,al2,t)
    return(ret)

l1 = [1,4,2,3,5]
l2 = [5,4,1,2,3]
print(listas(l1,l2))
