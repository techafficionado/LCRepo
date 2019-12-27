class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''
        #https://leetcode.com/problems/partition-equal-subset-sum/discuss/453387/C%2B%2B-or-DP-or-Easy-to-understand
        ALGORITHM:
        COMPUTE WHOLE SUM OF ALL THE NUMBERS AND DIVIDE BY 2 FOR HALF SUM
        DO USUAL RECURSIVE TARGET SUM FOR THE HALF SUM
        TO SPEED UP, USE DP TABLE WITH ROWS OF SUM AND COLUMNS OF INDEX
        '''
        def recTargetSum(nums,idx,tsum,rlist):
            if tsum == 0:
                #print("rlist:{}".format(rlist))
                return True
            
            if idx >= len(nums):
                return False
            
            if tsum < 0:
                return False
            
            #nextIdx = idx+1
            #print("tsum:{} idx:{}".format(tsum,idx))
            if dp[tsum][idx] != -1:
                return dp[tsum][idx]
            
            res = recTargetSum(nums,idx+1,tsum-nums[idx],rlist+[nums[idx]]) or recTargetSum(nums,idx+1,tsum,rlist)
            #print("tsum:{} idx:{}".format(tsum,idx))
            
            dp[tsum][idx] = res
            return res
            #return recTargetSum(nums,idx+1,tsum-nums[idx],rlist+[nums[idx]]) or recTargetSum(nums,idx+1,tsum,rlist)
        
        
        
        # compute sum
        fsum = 0
        for num in nums:
            fsum += num
            
        if fsum%2 != 0:
            return False
        
        tsum = fsum//2
        #print("tsum:{}".format(tsum))
        dp = [[-1 for j in range(len(nums)+1)] for i in range(tsum+1)] # sum is in row, index is in column
        #print("dp:{}".format(dp))
        #return recTargetSum(nums,0,tsum,[])
        ret = recTargetSum(nums,0,tsum,[])
    
        #print("dp:{}".format(dp))
        return ret
        
