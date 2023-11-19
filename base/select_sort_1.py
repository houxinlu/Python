# 选择排序
# def select_sort(array):
#     for i in range(len(array)):
#         min_index = i
#         for j in range(i + 1, len(array)):
#             if array[j] < array[min_index]:
#                 min_index = j
#         array[i], array[min_index] = array[min_index], array[i]
#         # tmp = array[min_index]
#         # array[min_index] = array[i]
#         # array[i] = tmp
#     return array
#
#
# if __name__ == '__main__':
#     array1 = [7, 9, 8, 12, 2, 5, 4]
#     print(select_sort(array1))
