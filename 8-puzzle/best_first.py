import numpy as np
import heapq 
import copy



class stateClass(object):
    __slots__ = ['_state','n','actual_position','depth']
    def __init__(self,state=None,n=None,depth=None):
        self.actual_position = {}
        self._state = state
        self.n = n
        self.depth = depth
        for i in range(0, (n ** 2)):
            self.actual_position[i] = ((i// n) , (i % n))
    
    def h1(self):
        count=0
        for i in range(1,(self.n**2)):
            if(np.where(self._state==i)!=self.actual_position[i]):
                count+=1
        return count
    
    def h2(self):
        count = 0
        sequence = self._state
        for i in range(self.n):
            for j in range(self.n):
                if sequence[i][j] != 0:
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
                yield stateClass(temp_sequence,self.n,self.depth + 1)
	    
	    

        
        
        
        
def isGoal(state):
    for i in range(3):
        for j in range(3):
            x = state.actual_position[state._state[i][j]]
            if(x[0]!=i or x[1]!=j):
                return False
    return True       
        

def Best_first(input_state,n):
    
    
    

    visited = []
    solution_seq = []
   
    def solve_recursion(state):
        List = []
        heapq.heapify(List)
    
        if isGoal(state):
            print('\nGoal state reached!\n No of steps: ',  (state.depth))
            return True
        
        if state in visited:
            return False
        visited.append(state)
        
        for child in state.generate_states():
            if child not in visited:
                heapq.heappush(List,child)
                
        while len(List):
            next_state = heapq.heappop(List)
            print(next_state, next_state.h2())
            if solve_recursion(next_state):
                solution_seq.insert(0,next_state)
                return True
        return False
    
    solve_recursion(input_state)
    solution_seq.insert(0,input_state)
    for steps in solution_seq:
        print(steps)
N = int(input())

l = []

for i in range(N):
    l.append(list(map(int,input().split(' '))))



input_array = np.array(l)
input_state = stateClass(state = input_array, n = N, depth = 0)


Best_first(input_state, N)


''' Goal state reached!
 No of steps:  56

State:
[[7 2 4]
 [5 0 6]
 [8 3 1]]
Depth: 0

State:
[[7 2 4]
 [5 3 6]
 [8 0 1]]
Depth: 1

State:
[[7 2 4]
 [5 3 6]
 [8 1 0]]
Depth: 2

State:
[[7 2 4]
 [5 3 0]
 [8 1 6]]
Depth: 3

State:
[[7 2 0]
 [5 3 4]
 [8 1 6]]
Depth: 4

State:
[[7 0 2]
 [5 3 4]
 [8 1 6]]
Depth: 5

State:
[[0 7 2]
 [5 3 4]
 [8 1 6]]
Depth: 6

State:
[[5 7 2]
 [0 3 4]
 [8 1 6]]
Depth: 7

State:
[[5 7 2]
 [3 0 4]
 [8 1 6]]
Depth: 8

State:
[[5 0 2]
 [3 7 4]
 [8 1 6]]
Depth: 9

State:
[[0 5 2]
 [3 7 4]
 [8 1 6]]
Depth: 10

State:
[[3 5 2]
 [0 7 4]
 [8 1 6]]
Depth: 11

State:
[[3 5 2]
 [8 7 4]
 [0 1 6]]
Depth: 12

State:
[[3 5 2]
 [8 7 4]
 [1 0 6]]
Depth: 13

State:
[[3 5 2]
 [8 0 4]
 [1 7 6]]
Depth: 14

State:
[[3 0 2]
 [8 5 4]
 [1 7 6]]
Depth: 15

State:
[[3 2 0]
 [8 5 4]
 [1 7 6]]
Depth: 16

State:
[[3 2 4]
 [8 5 0]
 [1 7 6]]
Depth: 17

State:
[[3 2 4]
 [8 0 5]
 [1 7 6]]
Depth: 18

State:
[[3 2 4]
 [0 8 5]
 [1 7 6]]
Depth: 19

State:
[[0 2 4]
 [3 8 5]
 [1 7 6]]
Depth: 20

State:
[[2 0 4]
 [3 8 5]
 [1 7 6]]
Depth: 21

State:
[[2 4 0]
 [3 8 5]
 [1 7 6]]
Depth: 22

State:
[[2 4 5]
 [3 8 0]
 [1 7 6]]
Depth: 23

State:
[[2 4 5]
 [3 0 8]
 [1 7 6]]
Depth: 24

State:
[[2 0 5]
 [3 4 8]
 [1 7 6]]
Depth: 25

State:
[[0 2 5]
 [3 4 8]
 [1 7 6]]
Depth: 26

State:
[[3 2 5]
 [0 4 8]
 [1 7 6]]
Depth: 27

State:
[[3 2 5]
 [1 4 8]
 [0 7 6]]
Depth: 28

State:
[[3 2 5]
 [1 4 8]
 [7 0 6]]
Depth: 29

State:
[[3 2 5]
 [1 4 8]
 [7 6 0]]
Depth: 30

State:
[[3 2 5]
 [1 4 0]
 [7 6 8]]
Depth: 31

State:
[[3 2 0]
 [1 4 5]
 [7 6 8]]
Depth: 32

State:
[[3 0 2]
 [1 4 5]
 [7 6 8]]
Depth: 33

State:
[[3 4 2]
 [1 0 5]
 [7 6 8]]
Depth: 34

State:
[[3 4 2]
 [0 1 5]
 [7 6 8]]
Depth: 35

State:
[[0 4 2]
 [3 1 5]
 [7 6 8]]
Depth: 36

State:
[[4 0 2]
 [3 1 5]
 [7 6 8]]
Depth: 37

State:
[[4 1 2]
 [3 0 5]
 [7 6 8]]
Depth: 38

State:
[[4 1 2]
 [3 6 5]
 [7 0 8]]
Depth: 39

State:
[[4 1 2]
 [3 6 5]
 [0 7 8]]
Depth: 40

State:
[[4 1 2]
 [0 6 5]
 [3 7 8]]
Depth: 41

State:
[[0 1 2]
 [4 6 5]
 [3 7 8]]
Depth: 42

State:
[[1 0 2]
 [4 6 5]
 [3 7 8]]
Depth: 43

State:
[[1 6 2]
 [4 0 5]
 [3 7 8]]
Depth: 44

State:
[[1 6 2]
 [0 4 5]
 [3 7 8]]
Depth: 45

State:
[[1 6 2]
 [3 4 5]
 [0 7 8]]
Depth: 46

State:
[[1 6 2]
 [3 4 5]
 [7 0 8]]
Depth: 47

State:
[[1 6 2]
 [3 0 5]
 [7 4 8]]
Depth: 48

State:
[[1 0 2]
 [3 6 5]
 [7 4 8]]
Depth: 49

State:
[[0 1 2]
 [3 6 5]
 [7 4 8]]
Depth: 50

State:
[[3 1 2]
 [0 6 5]
 [7 4 8]]
Depth: 51

State:
[[3 1 2]
 [6 0 5]
 [7 4 8]]
Depth: 52

State:
[[3 1 2]
 [6 4 5]
 [7 0 8]]
Depth: 53

State:
[[3 1 2]
 [6 4 5]
 [0 7 8]]
Depth: 54

State:
[[3 1 2]
 [0 4 5]
 [6 7 8]]
Depth: 55

State:
[[0 1 2]
 [3 4 5]
 [6 7 8]]
Depth: 56 '''