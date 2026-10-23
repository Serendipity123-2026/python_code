#  while 循环
def binary_search(arr, target):
    low, high = 0, len(arr) - 1         # 定于数组边界
    while low <= high:                                                       # 1, 3, 5, 7, 9, 11, 13, 15, 17, 19
        mid = (low + high) // 2         # 对数组进行 二分      4 -> 9
        if arr[mid] == target:          # 找到返回下标
            return mid
        elif arr[mid] < target:         # 下标对应的值小于目标值 舍弃左(前)边
            low = mid + 1
        else:                           # 下标对应的值大于目标值 舍弃右(后)边
            high = mid - 1
    return -1

nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

print(binary_search(nums, 15))          # 输出 7


# 递归的写法
def search(arr, target, low, high):
    if low >= high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return search(arr, target, mid + 1, high)       # 下标对应的值小于目标值 舍弃左(前)边
    else:
        return search(arr, target, low, mid - 1)        # 下标对应的值大于目标值 舍弃右(后)边

nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# 初始调用：low=0，high=最后一个下标
print(search(nums, 5, 0, len(nums)-1))         # 输出 2
