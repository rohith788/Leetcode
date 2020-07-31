class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        d = {}
        arr = []
        for i in arr1:
            if i in d: 
                d[i] += 1
            else:
                d[i] = 1
        for i in arr2:
            if i in d: 
                d[i] += 1
            else:
                d[i] = 1
        for i in arr3:
            if i in d: 
                d[i] += 1
            else:
                d[i] = 1
                
        for k in d:
            if(d[k] == 3):
                arr.append(k)
        return arr
#########################################################################################################
class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        arr = [i for i in arr1 if i in arr2 and i in arr3]
        return arr
                