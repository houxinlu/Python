# 选择排序，找出未完成排序的最小的值与当前遍历值做交换


def select_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):  # *1
            if array[min_index] > array[j]:
                min_index = j  # *2

        array[i], array[min_index] = array[min_index], array[i]
        # min_num = array[min_index]
        # array[min_index] = array[i]
        # array[i] = min_num

    return array


if __name__ == '__main__':
    array = [2, 5, 12, 6, 9, 4]
    print(select_sort(array))
