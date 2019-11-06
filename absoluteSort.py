def absSort(nums):
  def merge(nums,start,mid,end):
    '''print("merge start:{} mid:{} end:{}".format(start,mid,end))
    len1 = mid - start +1
    len2 = end - mid

    arr1 = [0]*len1
    arr2 = [0]*len2
    for i in range(len1):
      arr1[i] = nums[start+i]

    for j in range(len2):
      arr2[j] = nums[mid+1+j]'''


    arr1 = nums[start:mid+1]
    arr2 = nums[mid+1:end+1]

    len1 = len(arr1)
    len2 = len(arr2)

    print("arr1:{} arr2:{}".format(arr1,arr2))
    
    i=0
    j=0
    k=start
    while i < len1 and j<len2:
      if abs(arr1[i]) < abs(arr2[j]):
        nums[k] = arr1[i]
        i += 1
        k += 1
      elif abs(arr1[i]) > abs(arr2[j]):
        nums[k] = arr2[j]
        j += 1
        k += 1
      else:
        #if abs(arr1[i]) == abs(arr2[i]):
        if arr1[i] < arr2[j]:
          nums[k] = arr1[i]
          i += 1
          k += 1
        else:
          nums[k] = arr2[j]
          j += 1
          k += 1
      #else:
      #  nums[k] = arr2[j]
      #  j += 1
      #  k += 1
    while i<len1:
      nums[k] = arr1[i]
      i += 1
      k += 1
    while j<len2:
      nums[k] = arr2[j]
      j += 1
      k += 1 



  def mergeRec(nums,start,end):
    if start >= end:
      return

    mid = start + (end-start)//2
    print("start:{} mid:{} mid+1:{} end:{}".format(start,mid,mid+1,end))
    mergeRec(nums,start,mid)
    mergeRec(nums,mid+1,end)
    merge(nums,start,mid,end)

  mergeRec(nums,0,len(nums)-1)



nums = [-2,0,1,2,-2,4,5]
print(absSort(nums))
print("nums:{}".format(nums))
