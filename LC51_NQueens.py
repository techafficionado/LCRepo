class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        # prow, pcol, plrdiag, prldiag
        
        def checkValidPosition(row,j):
            nonlocal prow,pcol,plrdiag,prldiag
            if row in prow or j in pcol or (row-j) in plrdiag or (row+j) in prldiag:
                return False
            return True
        
        def placeQueen(row,j):
            nonlocal prow,pcol,plrdiag,prldiag
            #print("Placing queen row:{} j:{}".format(row,j))
            prow.append(row)
            pcol.append(j)
            plrdiag.append(row-j)
            prldiag.append(row+j)
            
        def unPlaceQueen(row,j):
            nonlocal prow,pcol,plrdiag,prldiag
            #print("UnPlacing queen row:{} j:{}".format(row,j))
            prow.remove(row)
            pcol.remove(j)
            plrdiag.remove(row-j)
            prldiag.remove(row+j)
                
            
        def nQueenRec(row):
            nonlocal result, solutions
            if row > n-1:
                solutions.append(result[:])
                return
            
            for j in range(n):
                #print("row:{} j:{}".format(row,j))
                if checkValidPosition(row,j):
                    placeQueen(row,j)
                    result[row] = j
                    nQueenRec(row+1)
                    #backtrack
                    unPlaceQueen(row,j)
            
            
        prow = []
        pcol = []
        plrdiag = []
        prldiag = []
        result = [-1]*n
        solutions = []
        fsol = []
        nQueenRec(0) # row
            
        for sol in solutions:
            li = []
            for col in sol:
                subli = ["." for i in range(n)]
                subli[col] = "Q"
                li.append("".join(subli))
            fsol.append(li)
            
        return fsol
        
