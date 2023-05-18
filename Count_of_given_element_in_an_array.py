''' SRINIVAS EDO ANUKUNNA KAANI AMMA BABOI'''
def count_occurrences(arr, target):
    count = 0
    for element in arr:
        if element == target:
            count += 1
    return count

# Read the input
N = int(input())
arr = list(map(int, input().split()))
target = int(input())

# Call the function and display the result
result = count_occurrences(arr, target)
print(result)

'''applications  [linked list]
polynomial
sparx matrix'''
