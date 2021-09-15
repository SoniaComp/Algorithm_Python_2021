def solution(A):
    # write your code in Python 3.6
    
    l_max_slice_sum = [0]*len(A)
    r_max_slice_sum = [0]*len(A)
    
    for i in range(1,len(A)-2):
        l_max_slice_sum[i] = max(l_max_slice_sum[i-1]+A[i],0)
    
    for i in range(len(A)-2,1,-1):
        r_max_slice_sum[i] = max(r_max_slice_sum[i+1]+A[i],0)
            
    max_slice_sum = l_max_slice_sum[0] + r_max_slice_sum[2]
    
    for i in range(1,len(A)-1):
        max_slice_sum = max(max_slice_sum,l_max_slice_sum[i-1]+r_max_slice_sum[i+1])
    
    return max_slice_sum