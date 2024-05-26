#------------------------------------------------------------------------------
#  RandomInput.py
#  Creates random input file for CSE 102 Programming Project.
#------------------------------------------------------------------------------
import random
import sys
sys.tracebacklimit=0

# get user input and initialize local variables
filename = input('Enter name of file to create: ')
n = int( input('Enter number of vertices (an int >=2): ') )
assert n>=2, f'{n} is not >=2'
m = int( input(f'Enter number of edges (an int >={n-1} and <={n*(n-1)/2}): ') )
assert n-1<=m<=n*(n-1)/2, f'{m} is not >={n-1}'
a = int( input('Enter weight lower bound (an int): ') )
b = int( input(f'Enter weight upper bound (an int >={a}): ') )
assert b>=a, f'{b} is not >={a}'
f = open(filename, 'w')

# create a random tree on n vertices, n-1 edges
adj = dict()
edge = list()
for y in range(2,n+1):
   x = random.randint(1, y-1)
   edge.append({x,y})
   adj[(x,y)] = adj[(y,x)] = 1
# end

# create additional m-n+1 random edges
for i in range(m-n+1):
   x = random.randint(1,n)
   y = random.randint(1,n)
   while (x,y) in adj or x==y:
      x = random.randint(1,n)
      y = random.randint(1,n)
   # end
   edge.append({x,y})
   adj[(x,y)] = 1
   adj[(y,x)] = 1
   # end
# end

# create  file
f = open(filename, 'w')
f.write(str(n)+'\n')
f.write(str(m)+'\n')
for i in range(m):
   x = tuple(edge[i])[0]
   y = tuple(edge[i])[1]
   w = random.randint(a,b)
   f.write(f'{x} {y} {w}\n')   
# end
f.close()