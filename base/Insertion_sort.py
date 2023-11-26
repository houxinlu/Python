# 插入排序
# 插牌形式的插入排序

def insert_sort(arr):
    for i in range(len(arr)):
        insert = arr[i]
        for j in range(0, i):
            if arr[j] > insert:
                arr[i], arr[j] = arr[j], arr[i]
                print(i, j, arr)
    return arr


if __name__ == '__main__':
    array = [2, 3, 1, 5, 6, 4]
    print(insert_sort(array))