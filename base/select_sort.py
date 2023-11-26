# 选择排序，找出未完成排序的最小的值与当前遍历值做交换


def select_sort(array):
    for i in range(len(array)):
        minIndex = i
        for j in range(i + 1, len(array)):
            if array[j] < array[minIndex]:
                minIndex = j
        array[i], array[minIndex] = array[minIndex], array[i]

    return array


if __name__ == '__main__':
    array = [2, 5, 12, 6, 9, 4]
    print(select_sort(array))
