# class Solution:
#     def sortedSquares(self, A: List[int]) -> List[int]:
#         for i in range(len(A)):
#           A[i] = A[i] * A[i]
#         print(A)
#         A.sort()
#         return A
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        n = len(A)
        arr = []
        j = 0
        for i in A:
          if i > 0:
            break
          j += 1
          
        i = j - 1
        while j < n and i >= 0:
          if A[i] ** 2 < A[j] ** 2:
            arr.append(A[i] ** 2)
            i -= 1
          else:
            arr.append(A[j] ** 2)
            j += 1
        while i >= 0:
          arr.append(A[i]** 2)
          i -= 1
        while j < n:
          arr.append(A[j]** 2)
          j += 1
        return arr
            