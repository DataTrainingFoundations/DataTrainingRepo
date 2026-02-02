#https://www.codewars.com/kata/577bcb5dd48e5180030004de

def min_unfairness(arr, k):
    n = len(arr)
    if k <= 1 or n < 2:  # edge cases
        return 0
    if k > n:  # can't take more elements than exist
        return 0
    
    arr_sorted = sorted(arr)
    min_diff = float('inf')

    # Slide a window of size k over the sorted array
    for i in range(n - k + 1):
        diff = arr_sorted[i + k - 1] - arr_sorted[i]
        if diff < min_diff:
            min_diff = diff

    return min_diff

print(min_unfairness([30,100,1000,150,60,250,10,120,20],3))