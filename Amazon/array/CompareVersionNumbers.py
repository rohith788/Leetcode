class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        arr1 = version1.split(".")
        arr2 = version2.split(".")
        i, j = 0, 0
        l_1, l_2 = len(arr1), len(arr2)
        if l_1 > l_2:
            while l_1 != l_2:
                arr2.append('0')
                l_2 += 1
        if l_2 > l_1:
            while l_2 != l_1:
                arr1.append('0')
                l_1 += 1
        while i < len(arr1) and j < len(arr2):
            if int(arr1[i]) > int(arr2[j]): return 1
            if int(arr1[i]) < int(arr2[j]): return -1
            i += 1
            j += 1
        
        return 0