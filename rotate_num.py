class Solution:
    @staticmethod
    def sort_method(sort_list: list):
        if len(sort_list) != 0:
            low, high = 0, len(sort_list) - 1
            if sort_list[low] < sort_list[high]:
                return sort_list[0]

            def sort_index(sortlist: list, low: int, high: int):
                index = low
                for i in range(low + 1, high + 1):
                    if sortlist[i] < sortlist[index]:
                        index = i
                return index

            def find_index(sort_list: list, low: int, high: int):
                if high - low > 1:
                    mid = int((low + high) / 2)
                    if sort_list[mid] == sort_list[low] == sort_list[high]:
                        return sort_index(sort_list, low, high)
                    if sort_list[mid] >= sort_list[low]:
                        return find_index(sort_list, mid, high)
                    if sort_list[mid] <= sort_list[high]:
                        return find_index(sort_list, low, mid)
                return high

            return sort_list[find_index(sort_list, low, high)]


if __name__ == "__main__":
    l = [3, 4, 5, 6, 1, 2, 3]
    l = [1, 0, 1, 1, 1]
    print(Solution.sort_method(l))
