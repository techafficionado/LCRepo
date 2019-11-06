def maximalsquare(grid):
  rlen = len(grid)
  clen = len(grid[0])
  maxval = 0
  for i in range(1,rlen):
    for j in range(1,clen):
      if grid[i][j]==1:
        grid[i][j] = min(grid[i-1][j],grid[i-1][j-1],grid[i][j-1])+1
        maxval = max(maxval, grid[i][j])
  return maxval

print(maximalsquare([[1, 1, 1, 0],
         [1, 1, 1, 1],
         [1, 1, 1, 0]])) # answer = 2
