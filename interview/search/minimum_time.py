def findItems(machines,temp):
    ans = 0
    for i in range(len(machines)):
        ans += temp // machines[i]
    return ans

def BinarySearch(machines,goal,high):
    low = 1
    while low < high:
        mid = (low + high) >> 1
        item = findItems(machines,mid)
        if item < goal:
            low = mid + 1
        else:
            high = mid
    return high
# Complete the minTime function below.
def minTime(machines, goal):
    maxval = -float('inf') 
    for i in range(len(machines)): 
        maxval = max(maxval, machines[i]) 
    return BinarySearch(machines,goal,maxval * goal)