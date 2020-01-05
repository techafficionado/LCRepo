class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # ITERATIVE:
        low = 0
        high = len(nums)-1
        
        while low<=high:
            mid = low + (high-low)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid +1
                
                
        return -1
        
        # RECURSIVE
        def binarySearchRec(nums,low,high):
            if low > high:
                return -1
            mid = low + (high-low)//2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return binarySearchRec(nums,low,mid-1)
            else:
                return binarySearchRec(nums,mid+1,high)
                
                
        return binarySearchRec(nums,0,len(nums)-1)   
