import matplotlib.pyplot as plt
import math

def logarithmic_algo_binary_search(arr, target):

    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

result = logarithmic_algo_binary_search([1, 3, 4, 6, 8, 9, 11, 13, 15], 8)
print(result)

steps=[]

def log(n):
    return math.log2(n)

for i in range(1,100):
    steps.append(log(i))

plt.plot(steps)
plt.show()