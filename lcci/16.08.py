# -*- coding: utf-8 -*-
# @Time    : 2020/4/20 上午10:44
# @Author  : RegiusQuant <315135833@qq.com>
# @Project : leetcode
# @File    : 16.08.py
# @Desc    : 说明

UNITS = ['', 'One', 'Two', 'Three', 'Four', 'Five',
         'Six', 'Seven', 'Eight', 'Nine', 'Ten',
         'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen',
         'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']

TENS = [None, None, 'Twenty', 'Thirty', 'Forty', 'Fifty',
        'Sixty', 'Seventy', 'Eighty', 'Ninety']


class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'

        billion, num = divmod(num, int(1e9))
        million, num = divmod(num, int(1e6))
        thousand, num = divmod(num, int(1e3))

        result = []
        if billion:
            result.append(self.numberToWords(billion))
            result.append('Billion')
        if million:
            result.append(self.helperThree(million))
            result.append('Million')
        if thousand:
            result.append(self.helperThree(thousand))
            result.append('Thousand')
        if num:
            result.append(self.helperThree(num))
        return ' '.join(result)

    def helperThree(self, num):
        if num < 20:
            return UNITS[num]
        elif num < 100:
            result = TENS[num // 10]
            remains = num % 10
            if remains:
                result += ' ' + UNITS[remains]
            return result
        else:
            result = UNITS[num // 100] + ' ' + 'Hundred'
            remains = num % 100
            if remains:
                result += ' ' + self.helperThree(remains)
            return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.numberToWords(1234567891))
