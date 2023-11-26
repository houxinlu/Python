class Solution:
    def majorityElement(self, nums):
        count, major = 0, 0
        for num in nums:
            print(count, major, num)
            if count == 0:
                major = num
            if num == major:
                count = count + 1
            else:
                count = count - 1
        return major


if __name__ == '__main__':
    arry = [5, 4, 4, 2, 1]
    solu = Solution()
    print(solu.majorityElement(arry))
