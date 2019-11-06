def duplicatesInArray(nums):
  # using hashmap is not constant space
  # this approach here, requires constant space since we know that the numbers in the array can range from 1 to len(arr)
  # derive a index from each of the value in the array - since indexes are 0 based do nums[i]-1 and change the sign
  # requires abs(nums[i]) since a future number could have been modified if a bigger number exists first in the array.
  # for example here 2 occurs before and we modify nums[2-1] which is the index 1 containing value 1 to -1. When we reach this value, we need to do a abs on it, to get a valid index value
  dups = []
  for i in range(len(nums)):
    idx = abs(nums[i]) -1
    if nums[idx] < 0:
      dups.append(abs(nums[idx]))
    else:
      nums[idx] = -nums[idx]
  return dups

nums =[2,1,2,1]
print(duplicatesInArray(nums))

