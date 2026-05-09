#bubble sort:
arr = list(map(int, input("Enter numbers separated by space: ").split()))
n = len(arr)
# original code without optimisation
for i in range(0,n-1):
    for j in range(0, n - 1-i):
        if arr[j] > arr[j + 1]:
            # Swapping
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Sorted array:", arr)


#bubble search with optimisation:
arr = list(map(int,input("Enter numbers separated by space: ").split()))
n = len(arr)
# best efficiency 
for i in range (0,n-1):
  sorted = True
  for j in range ( 0,n-1-i):
    if arr[j] > arr[j+1]:
      arr[j], arr[j+1] = arr[j+1], arr[j] #swapping
      sorted = False
  if sorted== True:
    break
print("Sorted array:", arr)
