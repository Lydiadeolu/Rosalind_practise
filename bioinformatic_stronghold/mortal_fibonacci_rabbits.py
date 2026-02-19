def solve_mortal_rabbits(n, m):
    
    ages = [0] * m
    ages[0] = 1
    
    for month in range(1, n):
        new_babies = sum(ages[1:])
        
        for i in range(m - 1, 0, -1):
            ages[i] = ages[i - 1]
            
        ages[0] = new_babies
        
    return sum(ages)

n_sample =int(input("Input n. "))
m_sample = int(input("Input m. "))
result = solve_mortal_rabbits(n_sample, m_sample)

if __name__ == "__main__":
    print(f"Sample Input: n={n_sample}, m={m_sample}")
    print(f"Sample Output: {result}")