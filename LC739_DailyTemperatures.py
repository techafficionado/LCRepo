class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        '''
        ALGORITHM:
        START FROM LEFT TO RIGHT
        APPEND FIRST ELEMENT TO STACK
        KEEP APPENDING ELEMENTS TO STACK AS LONG AS THEY ARE LESSER THAN THE CURRENT STACK TOP BECAUSE OUR GOAL IS TO FIND THE GREATER ELEMENTS FOR ALL ELEMENTS THAT ARE STUCK ON STACK.
        AS SOON AS A GREATER ELEMENT IS FOUND POP THE CURRENT VALUE FROM STACK AND UPDATE ITS INDEX IN THE RESULT ARRAY WHICH MEANS THAT YOU'D ALSO HAVE TO STORE THE INDEX OF THE ELEMENT IN THE STACK ALONG WITH THE VALUE
        FOR ALL THE REMAINING ELEMENTS JUST SET THE INDEX TO 0 IMPLYING THERE IS NO OTHER HIGHER ELEMENT FOUND FOR THEM
        '''
        tlen = len(T)
        #if tlen == 1:
        #    return [0]
        st = collections.deque()
        st.append([T[0],0]) # list with value and index
        result = [0]*tlen
        for i in range(1,tlen):
            while st and T[i]>st[-1][0]:
                result[st[-1][1]] = i-st[-1][1]
                st.pop()
            st.append([T[i],i])
            
        return result        
