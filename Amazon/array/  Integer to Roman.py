class Solution:
    def intToRoman(self, num: int) -> str:
        th = ["", "M", "MM" ,"MMM"]
        hu = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC","DCCC", "CM"]
        te = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        on = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return(""+(th[num // 1000])+(hu[(num % 1000) // 100])+(te[(num % 100) // 10])+(on[(num % 10)]))