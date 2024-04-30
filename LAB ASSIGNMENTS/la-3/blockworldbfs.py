import copy
def generate_children(s):
  l=[]
  for i in range(len(s)):
    if(len(s[i])!=0):
      for j in range(len(s)):
        s1=copy.deepcopy(s)
        if(j!=i):
          x=s1[i][0]
          s1[i].remove(x)
          s1[j].insert(0,x)
          l.append(s1)
  return l

def bfs_search(s1,g):
  open=[]
  closed=[]
  while(1):
      s=copy.deepcopy(s1)
      l = generate_children(s)
      for each in l:
        if each not in open and each not in closed:
          open.append(each)
          print(open)
      if len(open) > 0:
        s1 = open[0]
        del(open[0])
        print(s1)
        closed.append(s1)
        for each in s1:
          if each==g:
            print("found")
            return
      else:
        print ("not found")


s=[['A','B'],['C'],[]]
g=['C','B','A']

open=[]
closed=[]

generate_children(s)
bfs_search(s,g)
