import sys

"""
查找方法： 顺序查找，二分查找，二叉排序树查找、哈希表查找
在一个排序的数组或者部分排序的数组中查找某个数字或者统计某个数字出现的次数，可以尝试用二分查找
哈希表查找和二叉排序树查找的重点在于考察的数据结构而不是算法
哈希表的优势在于可以O(1)地查找，是效率最高的查找方式，但是需要消耗额外的空间
与二叉排序树对应的是二叉搜索树

迭代与递归

额外空间消耗
最差时间复杂度
平均时间复杂度
"""
class SortedMethod:

    @staticmethod
    def quick_sort(sort_list: list):
        pass



    @staticmethod
    def bubble_sort(sort_list: list):
        """
        冒泡的额外空间消耗为：O(n)
        最差和平均时间复杂度为：O(n^2)
        """
        if len(sort_list) != 0:
            for i in range(len(sort_list)):
                for j in range(i+1, len(sort_list)):
                    if sort_list[i] > sort_list[j]:
                        sort_list[i], sort_list[j] = sort_list[j], sort_list[i]
            return sort_list

    @staticmethod
    def selection_sort(sort_list: list) -> list:
        """
        空间复杂度为： O(n)
        最差和平均时间复杂度为：O(n^2)
        :param sort_list: list
        :return: list
        """
        list_length = len(sort_list)
        if list_length != 0:
            index = 0
            while index < list_length:
                tmp_index = index
                for i in range(index+1, list_length):
                    if sort_list[tmp_index] > sort_list[i]:
                        tmp_index = i
                sort_list[index], sort_list[tmp_index] = sort_list[tmp_index], sort_list[index]
                index += 1
            return sort_list

    @staticmethod
    def merge_sort(sort_list: list) -> list:
        """
        归并排序：1. 将每对单个元素（默认情况下， 已排序）归并为2个元素的有序数组
                2. 将2个元素的每对有序数组归并成为4个元素的有序数组，重复这个过程。。
                3. 最后一步： 归并2个N/2元素的排序数组以获得完全排序的N个元素数组
                注意： 排序数组中元素的个数可能为奇数
        :param sort_list: list
        :return: list
        """
        def sort_l(sort_list: list, left: int, right: int, templist: list):
            if left < right:
                mid = int((left+right)/2)
                sort_l(sort_list, left, mid, templist)
                sort_l(sort_list, mid, right, templist)

        def merge(sort_list: list, left: int, mid: int, right: int, tmplist: list):
            i = left
            j = mid + 1




            pass


if __name__ == '__main__':
    sort_list = []
    s = SortedMethod.selection_sort(sort_list)
    print(s)




