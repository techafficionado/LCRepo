class DSU: # Disjoint Set Union
    def __init__(self):
        self.par = range(1001)
        self.rank = [1]*1001 # no of nodes under it including itself
        
    def find(self,x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    
    def union(self,x,y):
        px = self.find(x)
        py = self.find(y)
        if px == py: # same parent
            return False # conveying there is a loop
        # if no loop, then do an union to merge the subsets
        if rank[px] > rank[py]:
            self.par[py] = px
        elif rank[px] < rank[py]:
            self.par[px] = py
        else: # equal rank
            self.par[py] = px
            self.rank[px] += self.rank[py]
        return True
