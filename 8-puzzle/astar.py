import numpy as np
import heapq 
import copy



class stateClass(object):
    __slots__ = ['_state','n','actual_position','depth']
    def __init__(self,state=None,n=None, depth=None):
        self.actual_position = {}
        self._state = state
        self.n = n
        self.depth = depth
        for i in range(0, (n ** 2)):
            self.actual_position[i] = ((i// n) , (i % n))

    
    def h2(self):
        
        count=0
        count += self.depth
        sequence = self._state
        for i in range(self.n):
            for j in range(self.n):
                
                actual_loc = self.actual_position[sequence[i][j]]
                count = count +  (abs(actual_loc[0] - i)  + abs(actual_loc[1] - j))
           
        return count
    def __str__(self):
        return '\nState:\n' + str(self._state) + '\nDepth: ' + str(self.depth)

    def __lt__(self,other):
        return self.h2() < other.h2()
    
    def __gt__(self,other):
        return self.h2() > other.h2()
    
    def __eq__(self,other):
        for i in range(self.n):
            for j in range(self.n):
                if self._state[i][j] != other._state[i][j]:
                    return False
        return True
    def __hash__(self):
        return hash(self._state.tostring())
        
        
        
        
    def find_space(self):
	    for i in range(self.n):
	        for j in range(self.n):
	            if self._state[i][j] == 0:
	                return i,j
        
    def generate_states(self):
        sequence = self._state
        space_i , space_j=self.find_space()
        for row_add,col_add in [(-1,0),(1,0),(0,1),(0,-1)]:
            temp_sequence = copy.deepcopy(sequence)
            if space_i + row_add >= 0 and space_i + row_add < self.n and space_j + col_add >= 0 and space_j + col_add < self.n:
                temp_sequence[space_i][space_j],temp_sequence[space_i + row_add][space_j + col_add]= temp_sequence[space_i + row_add][space_j + col_add],temp_sequence[space_i][space_j]
                yield stateClass(temp_sequence,self.n, self.depth+1)
	    
	    


        
def isGoal(array):
    for i in range(3):
        for j in range(3):
            if(array[i][j] !=( i*3 +j)):
                return False
    return True       
        

def Astar(input_array,n):
    
    parent={}
    input_state = stateClass(input_array, n, 0)
    visited = []
    
    
    
    
    List = []
    heapq.heapify(List)
    heapq.heappush(List,input_state)   
    while(len(List)):
        state=heapq.heappop(List)

        if isGoal(state._state):
            print('\nGoal state reached!\n No of steps: ',  (state.depth))
            l=[]
            
            for i in range(26):
                l.append(state)
                state=parent[state]
            l.append(input_state)
            l.reverse()
            for i in l:
                print(i)
            
        
        
        visited.append(state)
        
        for child in state.generate_states():
            if child not in visited:
                heapq.heappush(List,child)
                parent[child]=state
                
        
        
  


N = int(input())

l = []

for i in range(N):
    l.append(list(map(int,input().split(' '))))



input_array = np.array(l)

Astar(input_array,N)



'''output:
3
7 2 4
5 0 6
8 3 1

Goal state reached!
 No of steps:  26

State:
[[7 2 4]
 [5 0 6]
 [8 3 1]]
Depth: 0

State:
[[7 2 4]
 [0 5 6]
 [8 3 1]]
Depth: 1

State:
[[0 2 4]
 [7 5 6]
 [8 3 1]]
Depth: 2

State:
[[2 0 4]
 [7 5 6]
 [8 3 1]]
Depth: 3

State:
[[2 5 4]
 [7 0 6]
 [8 3 1]]
Depth: 4

State:
[[2 5 4]
 [7 3 6]
 [8 0 1]]
Depth: 5

State:
[[2 5 4]
 [7 3 6]
 [0 8 1]]
Depth: 6

State:
[[2 5 4]
 [0 3 6]
 [7 8 1]]
Depth: 7

State:
[[2 5 4]
 [3 0 6]
 [7 8 1]]
Depth: 8

State:
[[2 5 4]
 [3 6 0]
 [7 8 1]]
Depth: 9

State:
[[2 5 0]
 [3 6 4]
 [7 8 1]]
Depth: 10

State:
[[2 0 5]
 [3 6 4]
 [7 8 1]]
Depth: 11

State:
[[0 2 5]
 [3 6 4]
 [7 8 1]]
Depth: 12

State:
[[3 2 5]
 [0 6 4]
 [7 8 1]]
Depth: 13

State:
[[3 2 5]
 [6 0 4]
 [7 8 1]]
Depth: 14

State:
[[3 2 5]
 [6 4 0]
 [7 8 1]]
Depth: 15

State:
[[3 2 5]
 [6 4 1]
 [7 8 0]]
Depth: 16

State:
[[3 2 5]
 [6 4 1]
 [7 0 8]]
Depth: 17

State:
[[3 2 5]
 [6 4 1]
 [0 7 8]]
Depth: 18

State:
[[3 2 5]
 [0 4 1]
 [6 7 8]]
Depth: 19

State:
[[3 2 5]
 [4 0 1]
 [6 7 8]]
Depth: 20

State:
[[3 2 5]
 [4 1 0]
 [6 7 8]]
Depth: 21

State:
[[3 2 0]
 [4 1 5]
 [6 7 8]]
Depth: 22

State:
[[3 0 2]
 [4 1 5]
 [6 7 8]]
Depth: 23

State:
[[3 1 2]
 [4 0 5]
 [6 7 8]]
Depth: 24

State:
[[3 1 2]
 [0 4 5]
 [6 7 8]]
Depth: 25

State:
[[0 1 2]
 [3 4 5]
 [6 7 8]]
Depth: 26 '''
