class Solution:

    @staticmethod
    def joseph_loop(solder: int, choose_num: int):
        solder_list = []
        for i in range(solder):
            solder_list.append(i)
        index = 0
        while len(solder_list) > 1:
            if index != choose_num:
                index += 1
            else:
                pass



