from collections import Counter, OrderedDict
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        '''
        ALGORITHM
        FIRST GET COUNT OF THE KEY WITH MAX COUNT
        IF IT IS LESS THAN THE LENGHT OF THE LISTS, THEN THAT MEANS WE DO NOT HAVE ENOUGH OF THE TARGET VALUE WITH MAX COUNT IN EITHER LIST , WHICH MEANS ANY AMOUNT OF SWAPPING WOULD NOT GIVE US AN ARRAY WITH SAME VALUE
        
        IF IT IS GREATER THAN EQUAL TO LEN OF LIST THEN WE CAN PROCEED FURTHER
        BUT HOW DO WE VERIFY THAT IF A DOESN'T HAVE THE TARGET VALUE AT THAT INDEX THEN ATLEAST B HAS IT? THE CONDITION TO CHECK IS TO SEE IF ATLEAST EITHER A OR B AT THAT INDEX HAS THE TARGET VALUE, IF NOT RETURN -1
        
        ONCE PAST THE FOR LOOP RETURN TOTAL LEN - MAXCOUNT(A,B) TO RETURN THE LEAST NUMBER OF SWAPS 
        '''
        counter_c = Counter(A+B)
        d = max(counter_c.keys(), key=(lambda key: counter_c[key])) #list(sorted(counter_c.values()))[-1]#.items() # key with max count
        
        #print("counter_c:{} d:{}".format(counter_c,d))
        if counter_c[d] < len(A):
            return -1
        
        #print("d:{}".format(d))
        for i in range(len(A)):
            if A[i]!=d and B[i]!=d:
                return -1

        
        counterA = Counter(A)
        counterB = Counter(B)
        maxval = max(counterA[d],counterB[d])
        return len(A)-maxval
        
