def permutations(nums):
  def permRec(nums,start):
    
    nonlocal result
    if start == len(nums):
      result.append(nums[:])

    for i in range(start,len(nums)):
      #runList.append(nums[i])
      nums[i],nums[start]=nums[start],nums[i]

      permRec(nums,start+1)

      nums[start],nums[i]=nums[i],nums[start]

  result = []
  permRec(nums,0)    
  return result

def combinations(nums):
  def combRec(nums,start,runList):
    nonlocal result
    #if start == len(nums):
    result.append(runList[:])
    for i in range(start,len(nums)):
      runList.append(nums[i])
      combRec(nums,i+1,runList)
      runList.pop()


  result = []
  combRec(nums,0,[])
  return result




nums=[1,2,3,4]
print(permutations(nums))  
print(combinations(nums))
