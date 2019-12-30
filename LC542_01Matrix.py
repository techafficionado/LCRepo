import copy
from collections import deque
class Solution:
    '''
    ALGORITHM:
    SINCE DISTANCE OF NON-ZERO CELLS DEPENDS ON THEIR NEIGBORS JUST DOING A STRAIGHFORWARD 2 FOR LOOP TRAVERSAL ON THE MATRIX IS NOT GOING TO HELP SINCE ALL THE VALUES NEEDED TO COMPUTE THE MIN DISTANCE TO 0 NODES ARE NOT POPULATED.
    THE SOLUTION TO THIS IS TO USE BFS AND UPDATE THE DISTANCE ONLY IF CURRENT DISTANCE IS GREATER THAN SOURCE DIST + 1
    THE MAIN POINT IS TO START BFS FROM ALL 0 CELLS 
    '''
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return matrix
        rlen = len(matrix)
        clen = len(matrix[0])
        output = [[float('inf') for j in range(clen)] for i in range(rlen)]
        
        q = deque()
        for i in range(rlen):
            for j in range(clen):
                if matrix[i][j] == 0:
                    q.append([matrix[i][j],i,j])
                    output[i][j] = 0
        #print("q:{}".format(q))
        
        while q:
            val,i,j = q.popleft()
            #print("val:{} i:{} j:{}".format(val,i,j))
            for nr,nc in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
                if nr>=0 and nr<rlen and nc>=0 and nc<clen:
                    # without this condition it would be a forever loop since we are not keeping track of visited cells here. Hence, should atleast rely on the following condition to update and or append to the only the current distance is not as good as neighbor distance +1
                    if output[nr][nc] > output[i][j]+1:
                        output[nr][nc] = min(output[nr][nc],output[i][j]+1)
                        q.append([output[nr][nc],nr,nc])
        return output
        
