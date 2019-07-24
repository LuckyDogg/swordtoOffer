class Solution:
    """
    根据移动光标的方式，从左上角开始查找是关键
    如果等于就返回为真，如果数组的值小于查找的值那么就向下搜索
    如果数组的值大于查找的值，那么就向左搜索
    """
    @staticmethod
    def two_dimensional(array, number: int) -> bool:
        if array is not None:
            columns = len(array)
            if columns == 0:
                return False
            rows = len(array[0])
            if rows > 0:
                columns = 0
                rows -= 1
                while columns < len(array) and rows >= 0:
                    if array[columns][rows] == number:
                        return True
                    elif array[columns][rows] < number:
                        columns += 1
                    else:
                        rows -= 1
                return False
            return False
        else:
            return False


if __name__ == '__main__':
    array = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
    test = Solution.two_dimensional(array, 14)
    print(test)
    print(Solution())