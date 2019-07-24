class Solution:
    @staticmethod
    def replace_space(r: str):
        r = r.replace(" ", '%20')
        print(r)
    """
    正则表达式掌握
    """


if __name__ == '__main__':
    s = 'We are happy'
    Solution.replace_space(s)


