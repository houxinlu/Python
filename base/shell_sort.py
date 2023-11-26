# 希尔排序
# 带gap跨度的插入排序

def shell_sort(arr):
    n = len(arr)
    gap = int(n / 2)
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = array[j - gap]
                j = j - gap
            arr[j] = temp
        gap = int(gap / 2)
    return arr


if __name__ == '__main__':
    array = [2, 5, 12, 6, 9, 4]
    print(shell_sort(array))
