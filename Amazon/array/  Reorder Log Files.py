class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        arr_dig = []
        arr_alp = []
        logs = [i.split() for i in logs]
        for i in logs:
            if i[1].isdigit():
                arr_dig.append(i)
            else:
                arr_alp.append(i)
        # for i in arr_alp:
        #     print(i[1:]+[i[0]])
        return [" ".join(i) for i in sorted(arr_alp, key = lambda x: x[1:]+[x[0]]) + arr_dig]
            
