from collections import defaultdict
#import sys
#sys.setrecursionlimit(3*10**5)

n = int(raw_input())
A = [0]+map(int, raw_input().split())
AdjOf = [ [] for x in xrange(n+5)]

for i in xrange(n-1):
    u,v = map(int, raw_input().split())
    AdjOf[u].append(v)    
    AdjOf[v].append(u)

ChildrenOf = [ [] for x in xrange(n+5)]#defaultdict(list)
Seen = [0] * (n+5)
que = [1]*n
dq,cq = 0,0
while dq<=cq:
    u = que[dq]
    dq+=1
    Seen[u]=1
    for v in AdjOf[u]:
        if Seen[v]<1:
            ChildrenOf[u].append(v)
            cq+=1
            que[cq]=v

NINF = -10**16
TakeSum = [NINF] * (n+5)
BestSum = [NINF]* (n+5)
ans = NINF

for x in que[::-1]:
    if len(ChildrenOf[x])<1: 
        TakeSum[x] = A[x]
        BestSum[x] = A[x]
        continue
    TakeSum[x]=A[x]
    #for c in ChildrenOf[x]:
    #    TakeSum[x] += TakeSum[c]
    BestSum[x] = NINF
    fi,se = NINF, NINF
    for c in ChildrenOf[x]:
        TakeSum[x] += TakeSum[c]
        BestSum[x] = max(BestSum[x], BestSum[c])
        if BestSum[c]>fi:
            se,fi = fi, BestSum[c]
        elif BestSum[c]>se:
            se = BestSum[c]
    BestSum[x] = max(BestSum[x], TakeSum[x])
    if fi>NINF and se>NINF:
        ans = max(ans, fi+se)

"""
def takeSum(x):
    global TakeSum
    if len(ChildrenOf[x])<1: 
        TakeSum[x] = A[x]
        return A[x]
    if TakeSum[x]>NINF: return TakeSum[x]
    TakeSum[x]=A[x]
    for c in ChildrenOf[x]:
        TakeSum[x] += takeSum(c)
    return TakeSum[x]

def bestSum(x):
    global BestSum
    if len(ChildrenOf[x])<1: 
        BestSum[x] = A[x]
        return A[x]
    if BestSum[x]>NINF: return BestSum[x]
    BestSum[x] = takeSum(x)
    for c in ChildrenOf[x]:
        if A[x]>0:
            BestSum[x] = max(BestSum[x], bestSum(c))
        else:
            BestSum[x] = max(BestSum[x], bestSum(c))
    return BestSum[x]

for u in que[::-1]:
    takeSum(u)
    bestSum(u)

#print TakeSum
#print BestSum
#print ChildrenOf

def getAns(bestList):
    if len(bestList)<2: return NINF
    fi,se = NINF, NINF
    for x in bestList:
        if x>fi:
            se=fi
            fi=x
        elif x>se:
            se=x
    return fi+se        

ans = NINF
for x in que:#[::-1]:
    fi,se = NINF, NINF
    bestList = [BestSum[c] for c in ChildrenOf[x] if BestSum[c]>NINF]
    if len(bestList)<2: continue
    fi,se = NINF, NINF
    for x in bestList:
        if x>fi:
            se=fi
            fi=x
        elif x>se:
            se=x
    ans = max(ans, se+fi)
    #if ans>NINF: break


ans = NINF
Seen = set([1])
que = [1]
dq,cq = 0,0
while dq<=cq:
    u = que[dq]
    dq+=1
    Seen.add(u)
    best=[]
    for v in ChildrenOf[u]:
        if v not in Seen:            
            que.append(v)
            cq+=1
        if BestSum[v]>NINF: best.append(BestSum[v])    
    ans = max(ans, getAns(best))
"""
print ans if ans>NINF else "Impossible"
