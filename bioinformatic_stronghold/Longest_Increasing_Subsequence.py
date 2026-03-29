import bisect
import sys

def get_subsequence(arr, increasing=True):
    n = len(arr)
    if n == 0:
        return []

    tails = []
    tails_indices = []
    predecessors = [-1] * n

    for i, x in enumerate(arr):
        if increasing:
            idx = bisect.bisect_left(tails, x)
        else:
            idx = bisect.bisect_left(tails, -x)
        
        val = x if increasing else -x
        
        if idx < len(tails):
            tails[idx] = val
            tails_indices[idx] = i
        else:
            tails.append(val)
            tails_indices.append(i)
        
        if idx > 0:
            predecessors[i] = tails_indices[idx - 1]

    res = []
    curr = tails_indices[-1]
    while curr != -1:
        res.append(arr[curr])
        curr = predecessors[curr]
    
    return res[::-1]

if __name__ == "__main__":
    input_data = sys.stdin.read().split()
    if not input_data:
        pi = [5, 1, 4, 2, 3]
    else:
        pi = [int(x) for x in input_data[1:]]

    lis = get_subsequence(pi, increasing=True)
    lds = get_subsequence(pi, increasing=False)

    print(" ".join(map(str, lis)))
    print(" ".join(map(str, lds)))