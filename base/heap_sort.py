# 堆排序
# 大根堆，
# 1. 从上到下遍历构建堆 nLogn
# 2. 优化 从下到上便利构建堆 （比从上到下时间复杂度更优 n）

def heapInsert(arr, i):
    while arr[i] > arr[int((i - 1) / 2)]:
        arr[i], arr[int((i - 1) / 2)] = arr[int((i - 1) / 2)], arr[i]
        i = int((i - 1) / 2)


def heapify(arr, i, size):
    left = i * 2 + 1
    # 注意下标区间
    while left < size:
        right = left + 1
        if right < size and arr[right] > arr[left]:
            largest = right
        else:
            largest = left
        if arr[largest] < arr[i]:
            largest = i
        if largest == i:
            break
        arr[largest], arr[i] = arr[i], arr[largest]
        i = largest
        left = i * 2 + 1


if __name__ == '__main__':
    arr1 = [4, 5, 3, 1, 7, 12, 8, 0, 9, 11]
    # arr1 = [3, 2, 1, 5, 6, 4]
    n = len(arr1)

    # 构造大根堆，构造大根堆有两种方式，一种是从上倒下，一种是从下到上
    # 从上到下最会一次比较的值比较多，但从下到上是O(n),因为初始下面的n/2 没有孩子可比
    # #1. 向上调整大根堆的方式
    # for i in range(n):
    #     heapInsert(arr1, i)
    # 2.向下调整大根堆的方式，建堆 O(n)
    for i in range(n - 1, -1, -1):
        heapify(arr1, i, n)

    size = n
    k = size -2
    while size > k:
        size = size - 1
        arr1[0], arr1[size] = arr1[size], arr1[0]
        heapify(arr1, 0, size)
    print(arr1)
    print(size, arr1[k])
    # print(arr1)
