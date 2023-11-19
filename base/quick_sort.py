# 快速排序，找出一个值，将它放在合适的位置

def quick_sort(arr, left, right):
    if len(arr) <= 1:
        return arr
    if left >= right:
        return

    privot = sub(arr, left, right)
    quick_sort(arr, left, privot - 1)
    quick_sort(arr, privot + 1, right)


def sub(arr, left, right):
    privot = arr[left]
    i, j = left, right
    while i < j:
        while i < j and arr[j] >= privot:
            j = j - 1
        if i < j:
            arr[i] = arr[j]
            i = i + 1
        while i < j and arr[i] <= privot:
            i = i + 1
        if i < j:
            arr[j] = arr[i]
            j = j - 1

    arr[i] = privot
    return i


if __name__ == '__main__':
    a = [1, 2, 4, 12, 6, 1, 2, 6]
    quick_sort(a, 0, len(a) - 1)
    print(a)

# def partition(arr, low, high):
#     i = (low - 1)  # 最小元素索引
#     pivot = arr[high]
#
#     for j in range(low, high):
#
#         # 当前元素小于或等于 pivot
#         if arr[j] <= pivot:
#             i = i + 1
#             arr[i], arr[j] = arr[j], arr[i]
#
#     arr[i + 1], arr[high] = arr[high], arr[i + 1]
#     return (i + 1)
#
#
# # arr[] --> 排序数组
# # low  --> 起始索引
# # high  --> 结束索引
#
# # 快速排序函数
# def quickSort(arr, low, high):
#     if low < high:
#         pi = partition(arr, low, high)
#
#         quickSort(arr, low, pi - 1)
#         quickSort(arr, pi + 1, high)
#
#
# arr = [10, 7, 8, 9, 1, 5]
# n = len(arr)
# quickSort(arr, 0, n - 1)
# print("排序后的数组:")
# print(arr)
