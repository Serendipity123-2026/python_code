nums = [10, 20, 30, 40, 50]
try:
    print(nums[10])
except IndexError:
    print("下标越界了，请检查索引值")
print("程序继续运行")
