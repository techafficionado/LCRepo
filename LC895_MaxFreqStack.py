class FreqStack:

    '''
    ALGORITHM:
    MAINTAIN HASHMAP TO SAVE VALUE TO FREQ MAPPING
    MAINTAIN GROUP WITH FREQ - LIST MAPPING FOR ALL ELEMENTS WITH THE SAME FREQ. NEW ELEMENTS WILL BE AT THE END THUS GIVING US THE TOP OF THE STACK MAX FREQ ELEMENT EFFECT
    MAINTAIN SELF.MAXFREQ TO MAINTAIN THE MAXIMUM FREQUENCY
    '''
    def __init__(self):
        self.freq = collections.Counter() # stack element - freq
        self.group = collections.defaultdict(list) # freq - list of stack elements
        self.maxfreq = 0
        

    def push(self, x: int) -> None:
        self.freq[x] += 1
        if self.freq[x] > self.maxfreq:
            self.maxfreq = self.freq[x]
        self.group[self.freq[x]].append(x)        

    def pop(self) -> int:
        while len(self.group[self.maxfreq]) == 0:
            self.maxfreq -= 1
        x = self.group[self.maxfreq].pop()
        self.freq[x] -= 1
        return x
        
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
