# 堆排序
# 大根堆，
# 1. 从上到下遍历构建堆 nLogn
# 2. 优化 从下到上便利构建堆 （比从上到下时间复杂度更优 n）


def heapify(arr, i, len):
    left = i * 2 + 1
    best = left + 1
    while left < len:
        if left + 1 <= len and arr[left + 1] < arr[left]:
            best = left
        if arr[best] < arr[i]:
            best = i
        if best == i:
            break
        print(best, i)
        arr[best], arr[i] = arr[i], arr[best]
        i = best
        left = i * 2 + 1
        print(i, left)


if __name__ == '__main__':
    arr1 = [4, 5, 3, 1, 7, 12, 8, 0, 9, 11]
    # arr1 = [4, 5, 6]
    n = len(arr1)

    for i in range(n - 1, -1, -1):
        heapify(arr1, i, n)
    print(arr1)
