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

def dfsid_search(s1,g):
  open=[[]]
  closed=[]
  i=0
  while(1):
      s=copy.deepcopy(s1)
      l = generate_children(s)
      i=i+1
      for each in l:
        if each not in open and each not in closed:
          open.append(each)
          print(open)
      open1=copy.deepcopy(open)
      closed1=[]
      while len(list(open1)) > 0:
        s1 = list(open1)[len(list(open1))-1]
        del(open1[len(list(open1))-1])
        closed1.append(s1)
        print(s1)
        for each in s1:
          if each==g:
            print("found at depth ",i)
            return
      if len(list(open)) > 0:
        s1 = list(open)[len(list(open))-1]
        del(open[len(list(open))-1])
        closed.append(s1)
      else:
        print ("not found")


s=[['A','B'],['C'],[]]
g=['C','B','A']

dfsid_search(s,g)

