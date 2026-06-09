import bisect
import os

def get_longest_subsequence(arr, increasing=True):
    """
    Finds a longest increasing or decreasing subsequence in O(n log n) time.
    """
    if not arr:
        return []

    n = len(arr)
    data = arr if increasing else [-x for x in arr]
    
    prev_indices = [None] * n
    tail_indices = [None] * (n + 1)
    
    current_len = 0
    for i, x in enumerate(data):
        low = 1
        high = current_len
        while low <= high:
            mid = (low + high) // 2
            if data[tail_indices[mid]] < x:
                low = mid + 1
            else:
                high = mid - 1
        
        pos = low
        prev_indices[i] = tail_indices[pos - 1]
        tail_indices[pos] = i
        
        if pos > current_len:
            current_len = pos

    result = []
    curr = tail_indices[current_len]
    while curr is not None:
        result.append(arr[curr])
        curr = prev_indices[curr]
    
    return result[::-1]

def load_dataset(filepath):
    """
    Reads n and the permutation from a file.
    Handles files where n is on the first line and the permutation follows.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"The file '{filepath}' was not found.")
        
    with open(filepath, 'r') as f:
        content = f.read().replace(',', ' ').split()
        
    if not content:
        raise ValueError("The file is empty.")
        
    n = int(content[0])
    permutation = [int(x) for x in content[1:]]
    
    if len(permutation) != n:
        print(f"Warning: Expected {n} elements, but found {len(permutation)}.")
        
    return n, permutation

def main():
    filename = "C:/Users/adeolu/Downloads/rosalind_lgis (5).txt"
    # using of forward slash, adding r in front of the file path with back slash or using double back slash will prevent error in loading the file path
    try:
        if os.path.exists(filename):
            print(f"Loading data from {filename}...")
            n, test_pi = load_dataset(filename)
        else:
            print(f"File '{filename}' not found. Using internal example data.")
            n = 5
            test_pi = [5, 1, 4, 2, 3]

        lis_res = get_longest_subsequence(test_pi, increasing=True)
        lds_res = get_longest_subsequence(test_pi, increasing=False)
        
        print("\nLongest Increasing Subsequence:")
        print(*(lis_res))
        
        print("\nLongest Decreasing Subsequence:")
        print(*(lds_res))
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()