'''
3. Matrix product
Question : Given a matrix, find the path from top left to bottom right with the
greatest product by moving only down and right
'''

import sys
from functools import reduce
def pathProduct(grid):
  def dfs(grid,r,c,path):
    nonlocal maxprod

    if r == len(grid)-1 and c== len(grid[0])-1:
      print("path:{}".format(path))
      res = reduce(lambda x,y:x*y,path)
      print("res:{}".format(res))
      maxprod = max(res,maxprod)
      return

    for nr,nc in [[r+1,c],[r,c+1]]:
      if nr<0 or nr>len(grid)-1 or nc<0 or nc>len(grid[0])-1:
        continue
      dfs(grid,nr,nc,path+[grid[nr][nc]])

  path = [grid[0][0]]
  maxprod = -sys.maxsize
  dfs(grid,0,0,path)
  return maxprod



grid = [[-1, 2, 3],[4, 5, -6],[7, 8, 9]]
#grid = [[-1, 2, 3],[4, 5, -6],[7, 8, 9]]

print(pathProduct(grid))
