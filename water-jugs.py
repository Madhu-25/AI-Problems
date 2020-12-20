capacity=(8,5,3)
x = capacity[0]
y = capacity[1]
z = capacity[2]

#funtion to check if goal state is attained
def goal(s):
  if(s[0]==4 or s[1]==4):
    return True
  return False
 
#dictionary to maintain parent of each node
parent={}

#list to append next state of each node
L=[]
def next_states2(state):
    a = state[0]
    b = state[1]
    c = state[2]
    if(a>0):
      #empty a into b
        if(a+b>y):
            L.append((a-(y-b),y,c))
            
        else:
            L.append((0,a+b,c))
      #empty a into c
        if(a+c>z):
            L.append((a-(z-c),b,z))
        else:
            L.append((0,b,a+c))
  #empty jug b
    if(b>0):
      #empty b into a
        if(a+b>x):
            L.append((x, b-(x-a), c))
        else:
            L.append((a+b, 0, c))
            
      #empty b into c
        if(b+c>z):
            L.append((a, 0, b+c))
        else:
            L.append((a, b-(z-c), z))
  #empty jug c
    if(c>0):
      #empty c into a
        if(a+c>x):
            L.append((x, b, c-(x-a)))
        else:
            L.append((a+c, b, 0))
            
        if(b+c>y):
            L.append((a, y, c-(y-b)))
        else:
            L.append((a, b+c, 0))
            
    return L

def path(s,p):
    if(s!=initial_state):
        p.append(parent[s])
        path(parent[s],p)
        return p

def bfs(state):
  p=[]
  q=[]
  q.append(state)
  visited=[]
  while(len(q)!=0):
    s=q.pop(0)
    if(goal(s)):
      
      p=path(s,p)
      for e in reversed(p):
        print(e)
      print(s,'\n\n')
      break
    lis=next_states2(s)
    for i in lis:
      if(i not in visited and i not in parent.values()):
        visited.append(i)
        q.append(i)
        parent[i]=s
    
initial_state = (8,0,0)
bfs(initial_state)




""" output:
(8, 0, 0)                                                                                                               
(5, 0, 3)                                                                                                               
(5, 3, 0)                                                                                                               
(2, 3, 3)                                                                                                               
(2, 5, 1)                                                                                                               
(7, 0, 1)                                                                                                               
(7, 1, 0)                                                                                                               
(4, 1, 3)     """ 
