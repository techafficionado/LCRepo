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
    
class StreamChecker:
    '''
    Example:
    Dictionary : [bab,ab]
    query - a,a,a,b,a,a,b
    ALGORITHM:
    FOR EVERY "QUERY" CALL, KEEP APPENDING THE LETTER TO THE WORD ALREADY BUILT OUT.
    GOAL IS TO FIND OUT IF THE LAST K CHARACTERS OF THE WORD SO FAR ARE ACTUALLY A PROPER WORD IN THE DICTIONARY. FOR EXAMPLE, IF AB IS IN DICTIONARY QUERY FOR WHOLE WORS SUCH AS AAB, AAAAB ETC SHOULD RETURN TRUE SINCE THEY LAST K CHARCTERS AB OCCUR IN THE DICTIONARY.
    SINCE THE GOAL IS TO CHECK THE LAST X CHARS FOR VALID WORD - IT HELPS TO BUILD A REVERSE TRIE OF DICTIONARY WORDS AND REVERSING THE WHOLE WORD SO FAR BUILT FROM ALL QUERIES. 
    WE ITERATE THROUGH THE REVERSED WORD BUILD SO FAR AND IF THERE IS ANY MATCH IN DICTIONARY WITH EOW IS TRUE WE RETURN TRUE. IF AT ANY INDEX OF THE REVERSE WORD, A PROPER MATCH IN TRIE IS NOT FOUND THEN WE RETURN FALSE
    '''

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for word in words:
            self.trie.addWord(reversed(word))
            
        self.curTrieNode = self.trie.root
        
        self.wordSofar = ""
        
        self.count = 1

    def query(self, letter: str) -> bool:
        #print("query num:{} letter:{} self.curTrieNode:{}".format(self.count,letter,self.curTrieNode.val))
        self.count += 1
        '''
        if letter in self.curTrieNode.children:
            self.curTrieNode = self.curTrieNode.children[letter]
            print("self.curTrieNode val:{} eow:{}".format(self.curTrieNode.val,self.curTrieNode.eow))
            
            return self.curTrieNode.eow
        else:
            self.curTrieNode = self.trie.root
            
        return False
        '''
        self.wordSofar += letter
        #print("self.wordSofar:{}".format(self.wordSofar))
        node = self.trie.root
        for char in reversed(self.wordSofar):
            if char in node.children:
                node = node.children[char]
                if node.eow is True:
                    return True
            else:
                #self.wordSofar = char
                return False
        return False
        
        
        
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
