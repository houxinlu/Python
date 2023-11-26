# 冒泡算法


def bubble(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


if __name__ == '__main__':
    array1 = [2, 3, 1, 4, 6, 7]
    result = bubble(array1)
    print(result)
