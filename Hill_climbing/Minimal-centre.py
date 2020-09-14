import numpy as np

import copy

class point(object):
    __slots__=['_x','_y', 'n']
    def __init__(self, x = None, y = None, n=None):
        self._x=x
        self._y=y 
        self.n=n
    def manhattan(self,other):
        return (abs(self._x - other._x) + abs(self._y - other._y))
    
    def __str__(self):
        return'\n(x,y) = ('+str(self._x)+','+str(self._y)+')\n' 

    def generate_centre(self):
        for row_add,col_add in [(-1,0),(1,0),(0,1),(0,-1)]:
            x=copy.deepcopy(self._x)
            y=copy.deepcopy(self._y)
            
            if x+row_add>=0 and x+row_add<=self.n and y+col_add>=0 and y+col_add<=self.n:
                yield point(x+row_add, y+col_add, self.n)
                
visited=[]
def find_centre(points_List,n,centre):
    visited.append(centre)
    print('\n--------------------------------------------------------------\nCurrent centre: ',centre,'\nSum of manhattan distances (centre) :',Sum(points_List,centre) )
    List=[]
    for pt in centre.generate_centre():
        if pt not in visited:
            List.append(pt)
    
    print('\nNew centres: \n')        
    for a in List:
        print(a)
    
    
    S=[]
   
    for pt in List:
        S.append(Sum(points_List, pt))
    print('Sum of manhattan distances from new centres: ',S)
    if min(S) < Sum(points_List,centre):
        ind=S.index(min(S))
        centre=List[ind]
        find_centre(points_List,n,centre)
    else:
        print('Finalized Minimal centre: ')
        print(centre)
        print('\n Cost: ',Sum(points_List,centre))
    
   
    
        
        
def Sum(points_List, centre):
    S=0
    for pt in points_List:
        S+=centre.manhattan(pt)
    return S

print('Enter graph dimension(n x n)  n: ')
n=int(input())
l=[]
print('\nEnter the co-ordinates: \n')
for i in range(5):
    l.append(list(map(int,input().split(' '))))
array=np.array(l)

A=point(array[0][0],array[0][1],n)
B=point(array[1][0],array[1][1],n)
C=point(array[2][0],array[2][1],n)
D=point(array[3][0],array[3][1],n)
E=point(array[4][0],array[4][1],n)


Cen=point(0,0,n)


find_centre([A,B,C,D,E],n,Cen)


'''
output: 
Enter graph dimension(n x n)  n: 
9

Enter the co-ordinates: 

1 1
9 4
4 6
2 5
7 7

--------------------------------------------------------------
Current centre:  
(x,y) = (0,0)
 
Sum of manhattan distances (centre) : 46

New centres: 


(x,y) = (1,0)


(x,y) = (0,1)

Sum of manhattan distances from new centres:  [41, 41]

--------------------------------------------------------------
Current centre:  
(x,y) = (1,0)
 
Sum of manhattan distances (centre) : 41

New centres: 


(x,y) = (0,0)


(x,y) = (2,0)


(x,y) = (1,1)

Sum of manhattan distances from new centres:  [46, 38, 36]

--------------------------------------------------------------
Current centre:  
(x,y) = (1,1)
 
Sum of manhattan distances (centre) : 36

New centres: 


(x,y) = (0,1)


(x,y) = (2,1)


(x,y) = (1,2)


(x,y) = (1,0)

Sum of manhattan distances from new centres:  [41, 33, 33, 41]

--------------------------------------------------------------
Current centre:  
(x,y) = (2,1)
 
Sum of manhattan distances (centre) : 33

New centres: 


(x,y) = (1,1)


(x,y) = (3,1)


(x,y) = (2,2)


(x,y) = (2,0)

Sum of manhattan distances from new centres:  [36, 32, 30, 38]

--------------------------------------------------------------
Current centre:  
(x,y) = (2,2)
 
Sum of manhattan distances (centre) : 30

New centres: 


(x,y) = (1,2)


(x,y) = (3,2)


(x,y) = (2,3)


(x,y) = (2,1)

Sum of manhattan distances from new centres:  [33, 29, 27, 33]

--------------------------------------------------------------
Current centre:  
(x,y) = (2,3)
 
Sum of manhattan distances (centre) : 27

New centres: 


(x,y) = (1,3)


(x,y) = (3,3)


(x,y) = (2,4)


(x,y) = (2,2)

Sum of manhattan distances from new centres:  [30, 26, 24, 30]

--------------------------------------------------------------
Current centre:  
(x,y) = (2,4)
 
Sum of manhattan distances (centre) : 24

New centres: 


(x,y) = (1,4)


(x,y) = (3,4)


(x,y) = (2,5)


(x,y) = (2,3)

Sum of manhattan distances from new centres:  [27, 23, 23, 27]

--------------------------------------------------------------
Current centre:  
(x,y) = (3,4)
 
Sum of manhattan distances (centre) : 23

New centres: 


(x,y) = (2,4)


(x,y) = (4,4)


(x,y) = (3,5)


(x,y) = (3,3)

Sum of manhattan distances from new centres:  [24, 22, 22, 26]

--------------------------------------------------------------
Current centre:  
(x,y) = (4,4)
 
Sum of manhattan distances (centre) : 22

New centres: 


(x,y) = (3,4)


(x,y) = (5,4)


(x,y) = (4,5)


(x,y) = (4,3)

Sum of manhattan distances from new centres:  [23, 23, 21, 25]

--------------------------------------------------------------
Current centre:  
(x,y) = (4,5)
 
Sum of manhattan distances (centre) : 21

New centres: 


(x,y) = (3,5)


(x,y) = (5,5)


(x,y) = (4,6)


(x,y) = (4,4)

Sum of manhattan distances from new centres:  [22, 22, 22, 22]
Finalized Minimal centre: 

(x,y) = (4,5)


 Cost:  21

'''
