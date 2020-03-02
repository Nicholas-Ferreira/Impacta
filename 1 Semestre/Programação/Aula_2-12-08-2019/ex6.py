import random

nums = []
dado = [0, 0, 0, 0, 0, 0]

for i in range(10):
    n = random.randint(1, 6)
    nums.append(n)
    dado[n-1] += 1

print(nums)
print(dado)