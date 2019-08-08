class Solution:
    @staticmethod
    def oneintwo(num: int) -> int:
        count = 0
        while num:
            if num & 1 == 0:
                count +=1
            num = num >> 1
            print(num)
        return count

    @staticmethod
    def oneintwo2(num: int) -> int:
        count = 0
        flag = 1
        while flag < num:
            if num & 1 == 0:
                count +=1
            flag <<= 1
            print(flag)
        return count



if __name__ == '__main__':
    num = -8
    print(Solution.oneintwo2(num))
