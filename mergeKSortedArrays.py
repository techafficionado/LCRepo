import heapq
def mergeKSortedArrays(arrList):
  k = len(arrList)
  n = len(arrList[0])
  print("k:{} n:{}",k,n)
  totEl = 1
  # compute total number of elements to handle case where the length of arrays are uneven
  for i in range(k):
    totEl += len(arrList[i])
  print("totEl:{}".format(totEl))
  li = []
  count = k
  
  results = []
  for i in range(k):
    arri = arrList[i]
    # append the element, number of array, index, lenght of array
    heapq.heappush(li,[arri[0], i, 0, len(arri)]) #element, number of array, index in array
  while count < n*k:
    print("count:{}".format(count))
    heapEle = heapq.heappop(li)
    ele, arrnum, idx, arrlen = heapEle
    idx = idx+1
    if idx <= arrlen:
      newarrEle = arrList[arrnum][idx]
      heapq.heappush(li,[newarrEle,arrnum,idx,arrlen])
    results.append(ele)
    count += 1
  while len(li)>0:
    heapEle = heapq.heappop(li)
    results.append(heapEle[0])

  print("results:{}".format(results))





arrList = [[1,4,7],[2,5,8],[3,6,9]]  
print(mergeKSortedArrays(arrList))
