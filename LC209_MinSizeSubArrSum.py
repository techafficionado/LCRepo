class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0
        slen = len(nums)
        lptr = 0
        rptr = 0
        
        
        tsum = 0
        minlen = float('inf')
        
        while lptr <= rptr and rptr < slen:
            tsum += nums[rptr]
            #print("tsum:{} rptr:{} minlen:{}".format(tsum,rptr,minlen))
            rptr += 1
            
            
            
            while tsum>= s:
                tsum -= nums[lptr]
                lptr += 1
                minlen = min(minlen,rptr-lptr+1)
                
        if not minlen < float('inf'):
            return 0
        return minlen
            
