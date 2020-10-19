'''
1.两数之和
题目描述：
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''



'''
"""
方法一：暴力破解法
"""
#本地编译时反复报错”NameError: name 'List' is not defined“，经查询需要加上typing头即可
#python是一门弱类型的语言，使用过程不用过多关注变量的类型，但是同时也带来了问题，就是代码的易读性变差了，
#有时候自己都不知道传入的是什么参数。因此在python3.5之后，引入了一个typing模块，这个模块可以很好解决这个问题。
from typing import List
import time
#python3.8起不支持clock()
#start = time.clock()
start =time.perf_counter()
class Solution:
    def twoSum(self, nums: List[int], target:int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[j] + nums[i] == target:
                    return [i,j]

        return []
#如果Solution后面没有（）会报错  TypeError: twoSum() missing 1 required positional argument: 'self'
#print(Solution.twoSum(nums = [2, 7, 11, 15], target = 26))
print(Solution().twoSum(nums = [2, 7, 11, 15], target = 26))
#PYTHON3.8不支持clock
#end = time.clock()
end = time.perf_counter()
print('Running time: %.8s ms'%((end-start)*1000))
'''

"""
方法一：暴力破解法（By:KionCheng）
"""

# class Solution():
#   def __init__(self,nums,target):
#       self.nums = nums
#       self.target = target
#
#   def twoSum(self):
#       n = len(self.nums)
#       for i in range(n):
#           for j in range(i+1,n):
#               if self.nums[j] + self.nums[i] == self.target:
#                   print([i,j])
# X = Solution([2,7,11,16],13).twoSum()







#
# # 作者：匿名用户
# # 链接：https://www.zhihu.com/question/46973549/answer/103805810
# # 来源：知乎
# # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# #
# # 强行装个吧：定义类的时候，若是添加__init__方法，那么在创建类的实例的时候，实例会自动调用这个方法，一般用来对实例的属性进行初使化。比如：
# class  TestClass:
#     def  __init__(self, name, gender):
#     #定义 __init__方法，这里有三个参数，这个self指的是一会创建类的实例的时候这个被创建的实例本身（例中的testman），你也可以写成其他的东西，比如写成me也是可以的，这样的话下面的self.Name就要写成me.Name。
#          self.Name=name
#     #通常会写成self.name=name，这里为了区分前后两个是不同的东东，把前面那个大写了，等号左边的那个Name（或name）是实例的属性，后面那个是方法__init__的参数，两个是不同的）
#          self.Gender=gender
#     print('hello')
#     #这个print('hello')是为了说明在创建类的实例的时候，__init__方法就立马被调用了。
#
# testman = TestClass('Neo','Male')

# 这里创建了类testClass的一个实例 testman, 类中有__init__这个方法，
# 在创建类的实例的时候，就必须要有和方法__init__匹配的参数了，
# 由于self指的就是创建的实例本身，self是不用传入的，所以这里传入两个参数。
# 这条语句一出来，实例testman的两个属性Name，Gender就被赋值初使化了，其中Name是 neo，Gender 是male。


# """
# 方法二：哈希表
# """
# # class Solution:
# #     def __init__(self,nums,target):
# #         self.nums = nums
# #         self.target = target
# #
# #     def twoSum(nums, target):
# #         lens = len(nums)
# #         for i in range(lens):
# #             for j in range(i+1,lens):
# #                 if nums[j] + nums[i] == target:
# #                     print([i,j])
# #         return []
# #
# # if __name__ == '__main__':
# #     Solution.twoSum(nums = [2, 7, 11, 15], target = 26)






def inspect(x):
    if x == 0:
        print(x, "is zero")
    elif x > 0:
        print(x, "is positive")
    elif x < 0:
        print(x, "is negative")
    else:
        print(x, "is unlike anything I've ever seen...")

if __name__ == '__main__':
    result = int(input())
    print (inspect(result))