练习：
	给定一个字符串：‘abcdefghijklmnopqrstuvwxyz’
  1.将其转换成一个列表
  2.将这个列表反转过来
  3.求其长度
  4.获取索引是偶数的值并且生成一个新列表
  5.给定一个列表：[1,3,4,2,5,6,2,7,3,2,7],适用列表解析去除重复项
  6.寻找两个列表：[1,2,5,2,7,2,4,7] 和 [2,5,8,2,4,3]中相同和不相同的新列表，用列表解析实现

H = 'abcdefghijklmnopqrstuvwxyz'
a = list(H)
print a
a.reverse()
print a

print len(H)

print [_ for _ in H if (H.index(_) + 1) % 2 == 0]

X = [1, 3, 4, 2, 5, 6, 2, 7, 3, 2, 7]
L = []
[L.append(_) for _ in X if _ not in L]
print L

M = [1, 2, 5, 2, 7, 2, 4, 7]
N = [2, 5, 8, 2, 4, 3]

NM = []
[NM.append(_) for _ in M if _ in N and _ not in NM]
print NM

MN = []
[MN.append(_) for _ in M if _ not in N and _ not in MN]
[MN.append(_) for _ in N if _ not in M and _ not in MN]

print MN
