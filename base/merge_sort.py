# 归并排序
# 需要一个数组记录

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    min_index = len(arr) // 2

    arr_left = merge_sort(arr[:min_index])
    arr_right = merge_sort(arr[min_index:])
    result = sub(arr_left, arr_right)
    return result


def sub(arr_left, arr_right):
    i, j = 0, 0
    new_arr = []
    while i < len(arr_left) and j < len(arr_right):
        if arr_left[i] < arr_right[j]:
            new_arr.append(arr_left[i])
            i = i + 1
        else:
            new_arr.append(arr_right[j])
            j = j + 1

    new_arr = new_arr + arr_left[i:]
    new_arr = new_arr + arr_right[j:]
    return new_arr


if __name__ == '__main__':
    a = [1, 2, 4, 12, 6, 1, 2, 6]
    print(merge_sort(a))
