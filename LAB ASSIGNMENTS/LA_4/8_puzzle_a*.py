#In this code "s_no" represents the number of states it visited from initial state
import copy

q=[]
visited=[]
counter=0

g=[[1,2,3],
    [8,0,4],
    [7,6,5]]

s0=[[2,0,3],
    [1,8,4], # 0 represents blank space
    [7,6,5]]

def compare(s,g):
    if s==g:
        return 1
    else:
        return 0

def find_pos(s1):
    for i in range(len(s1)):
        for j in range(len(s1[i])):
            if s1[i][j]==0:
                return [i,j]
            
def up(s):
    pos=find_pos(s)
    row=pos[0]
    col=pos[1]
    s1=copy.deepcopy(s)
    if row>0: 
        s1[row][col],s1[row-1][col]=s1[row-1][col],s1[row][col]
    return s1

def down(s):
    pos=find_pos(s)
    row=pos[0]
    col=pos[1]
    s1=copy.deepcopy(s)
    if row<len(s1)-1: 
        s1[row][col],s1[row+1][col]=s1[row+1][col],s1[row][col]
    return s1

def left(s):
    pos=find_pos(s)
    row=pos[0]
    col=pos[1]
    s1=copy.deepcopy(s)
    if col>0: 
        s1[row][col],s1[row][col-1]=s1[row][col-1],s1[row][col]
    return s1

def right(s):
    pos=find_pos(s)
    row=pos[0]
    col=pos[1]
    s1=copy.deepcopy(s)
    if col<len(s[0])-1: 
        s1[row][col],s1[row][col+1]=s1[row][col+1],s1[row][col]
    return s1

def dist(s,g,s_no):
    global s0
    counter=0
    for i in range(len(s)):
        for j in range(len(s[i])):
            if s[i][j]!=g[i][j]:
                counter=counter+1
    
    counter=counter+s_no

    return counter


def enqueue(s,s_no):
    global q
    global g

    s_no=s_no+1
    d= dist(s,g,s_no)
    q.append([d,s,s_no])

def generate_child(s,s_no):
    global q
    global visited
    global g

    new_state_up=up(s)
    d=dist(new_state_up,g,s_no+1)
    if new_state_up not in visited and [d,new_state_up] not in q:
        enqueue(new_state_up,s_no)

    new_state_down=down(s)
    d=dist(new_state_down,g,s_no+1)
    if new_state_down not in visited and [d,new_state_down] not in q:
        enqueue(new_state_down,s_no)

    new_state_left=left(s)
    d=dist(new_state_left,g,s_no+1)
    if new_state_left not in visited and [d,new_state_left] not in q:
        enqueue(new_state_left,s_no)

    new_state_right=right(s)
    d=dist(new_state_right,g,s_no+1)
    if new_state_right not in visited and [d,new_state_right] not in q:
        enqueue(new_state_right,s_no)


def search(g):
    global q
    global visited

    while 1:
        q.sort()
        current_state=q[0][1]
        state_number=q[0][2]
        del q[0]

        if compare(current_state,g):
            print("Found\n")
            return
        else:
            visited.append(current_state)
            generate_child(current_state,state_number)
            


def main():
    global q
    global visited
    global g
    global s0

    
    
    d=dist(s0,g,0)
    q.append([d,s0,0])

    search(g)

    l=len(visited)
    print("The number of states it visited is: ",l)
    
if __name__=="__main__":
    main()