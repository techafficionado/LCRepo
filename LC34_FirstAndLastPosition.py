class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        '''
        Better solution at
        https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/solution/
        ALGORITHM
        FIND TARGET FIRST
        SEARCH LEFT FOR LEFT MOST
        SEARCH RIGHT FOR RIGHT MOST
        Runtime: 84 ms, faster than 94.42% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
Memory Usage: 14.1 MB, less than 5.36% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
        '''
        def findLeftMost(low,high,target):
            while low <= high:
                mid = low + (high-low)//2
                #print("low:{} mid:{} high:{}".format(low,mid,high))

                if nums[mid] == target:
                    if nums[mid-1] != target:
                        return mid
                    else:
                        high = mid-1
                elif nums[mid] < target:
                    low = mid+1 
                
        
        def findRightMost(low,high,target):
            while low <= high:
                mid = low + (high-low)//2

                if nums[mid] == target:
                    if nums[mid+1] != target:
                        return mid
                    else:
                        low = mid+1
                elif nums[mid] > target:
                    high = mid-1 
            
            pass
            
        result = [-1,-1]
        
        if not nums or len(nums) == 0:
            return result
        
        low = 0
        high = len(nums)-1
        
        
        if nums[low] == target and nums[high] == target:
            return [low,high]
        
        targetIdx = None
        while  low <= high:
            mid = low + (high-low)//2
            print("low:{} mid:{} high:{}".format(low,mid,high))
            
            if nums[mid] < target:
                low = mid+1
            elif nums[mid] > target:
                high = mid-1 
            else:
                targetIdx = mid
                break 
               
        # if element is not found 
        if targetIdx is None:
            return result
        
        if targetIdx == 0:
            l = 0
        elif nums[0] == target:
            l = 0
        elif nums[targetIdx-1] != nums[targetIdx]:
            l = targetIdx
        else:
            # find leftmost
            l = findLeftMost(low,targetIdx,target)
            
        if targetIdx == len(nums)-1:
            r = len(nums)-1
        elif nums[-1] == target:
            r = len(nums)-1
        elif nums[targetIdx+1] != nums[targetIdx]:
            r = targetIdx
        else:
            # find rightmost
            r = findRightMost(targetIdx,high,target)
            
        return [l,r]
        
