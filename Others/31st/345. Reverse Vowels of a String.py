class Solution:
    def reverseVowels(self, s: str) -> str:
        d = {'a': True, 'e': True, 'i': True, 'o': True, 'u': True}
        arr = []
        for i in range(len(s)):
            if(s[i].lower() in d): arr.append(i)
        i, j = 0, len(arr) - 1
        str_arr = list(s)
        while(i < j):
            temp = str_arr[arr[i]]
            str_arr[arr[i]] = str_arr[arr[j]]
            str_arr[arr[j]] = temp
            i += 1
            j -= 1
        return "".join(str_arr)
            
            