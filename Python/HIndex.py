import sys

def binary_search_h_index(arr, low, high, best):
 
    if high >= low:
 
        mid = (high + low) // 2
 
        if (mid+1) >= arr[mid]:
            return binary_search_h_index(arr, low, mid - 1, max(best, min(arr[mid], mid+1)))
 
        else:
            return binary_search_h_index(arr, mid + 1, high, max(best, min(arr[mid], mid+1)))
 
    else:
        return best


noPapers = int(sys.stdin.readline())
citationsOnPapers = []
for paper in range(0, noPapers):
    citationsOnPapers.append(int(sys.stdin.readline()))
citationsOnPapers.sort(reverse=True)

result = binary_search_h_index(citationsOnPapers, 0, len(citationsOnPapers)-1, 0)

print(result)
