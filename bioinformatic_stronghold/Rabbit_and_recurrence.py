n = int(input("what is the value of n? "))
k = int(input("what is the value of k? "))
def fibonacci (n, k):
    if n == 1 or n == 2:
        return 1
    
    parent = 1
    child = 1
    for _ in range(3, n + 1):
        total = child + (parent * k)
        parent = child
        child = total
    return child


    
print("The total of object is", fibonacci(n, k))