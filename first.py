import heapq
from collections import deque

nums = [-1, -8, -2, -23, -7, - 4, 18, 23, 42, 37, 2]
nums.sort()
print(nums)
print(heapq.nlargest(3, nums))  # Prints [42, 37, 23]
print(heapq.nsmallest(3, nums))  # Prints [-4, 1, 2]


print(min(nums))

print("-" * 20)
CodeAndName = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

max = max(zip(CodeAndName.values(), CodeAndName.keys()))
print("Max: Code = %s , Value = %s" % (max[1], max[0]))
print(min(zip(CodeAndName.values(), CodeAndName.keys())))
print(CodeAndName["IBM"])
# 开发版本1.1
# 开发版本1.2
# 开发版本1.3 fixbug
# 开发版本1.4 fixbug
# 开发版本1.5 fixbug
# 开发版本1.6 fixbug
# 开发版本1.7 fixbug
# 开发版本1.7.1 fixbug
# 开发版本1.7.2 fixbug
# 开发版本1.7.3
# 开发版本1.8
# 开发版本1.8.1
# 开发版本1.8.2
# 开发版本1.8.3
# 开发版本1.8.4
# 开发版本1.8.5
# 开发版本1.8.6
# 开发版本1.8.7
# 开发版本1.8.8
# 开发版本1.8.9
# 开发版本1.8.10 by other
# 开发版本1.8.11
# 开发版本1.8.12