def bin_search(array, target, start, end):
  if start > end:
    return None
  mid = (start+end)//2

  if array[mid] == target:
    return mid
  
  elif array[mid] > target:
    return bin_search(array, target, start, mid-1)
  
  else:
    return bin_search(array, target, mid+1, end)

n, target = map(int, input().split())

a = list(map(int, input().split()))

result = bin_search(a, target, 0, n-1)

if result == None:
  print('nothing')
else:
  print(result+1)