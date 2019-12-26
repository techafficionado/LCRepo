class TrieNode():
    def __init__(self,val):
        self.val = val
        self.children = {}
        self.eow = False
        
class Trie():
    def __init__(self):
        self.root = TrieNode('*')
        
    def addWord(self,word):
        node = self.root
        
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                # create Trienode
                tn = TrieNode(char)
                node.children[char] = tn
                node = node.children[char]
        node.eow = True
                
    def checkWord(self,word):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return False
           
        if node.eow is True:
            return True
        return False
            
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        '''
        ALGORITHM
        CONSTRUCT TRIE
        ADD THE WORDS IN DICITIONARY TO THE TRIE
        DO DFS OF THE BOARD AND PARALLELY PROGRESS ON THE TRIENODE
        MAIN CONDITIONS:
        IF CHAR NOT IN THE TRIENODE CHILDREN RETURN
        IF VISITED IS TRUE RETURN TO AVOID WRAPAROUND REPETITIVE LOOPS FOR THE SAME INDEX I,J
        IF EOW IS TRUE, THAT MEANS WE FOUND THE WORD, APPEND IT TO RESULT
        '''
        def dfs(board, i, j, trienode, charList):
            if board[i][j] not in trienode.children:
                return
            if visited[i][j] is True:
                return
            
            trienode = trienode.children[board[i][j]]
            
            if trienode.eow is True:
                result.add("".join(charList[:]+[board[i][j]]))
            
            visited[i][j] = True
            for nr,nc in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
                if nr<0 or nr>rlen-1 or nc<0 or nc>clen-1:
                    continue
                dfs(board,nr,nc,trienode,charList+[board[i][j]])
            visited[i][j] = False
            
            
        rlen = len(board)
        clen = len(board[0])
        visited = [[False for j in range(clen)] for i in range(rlen)]
        trie = Trie()
        result = set()#[]
        for word in words:
            trie.addWord(word)
          
        #print("trie root:{}".format(trie.root))
        #for word in words:
        #    res = trie.checkWord(word)
        #    print("word:{} res:{}".format(word,res))
        
            
        for i in range(rlen):
            for j in range(clen):
                dfs(board,i,j,trie.root, [])
                
        return result
        
        
        
        
        
