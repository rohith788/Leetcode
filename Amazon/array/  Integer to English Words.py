class Solution:
    def numberToWords(self, num: int) -> str:
        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split() # Array of numbers from 1-19
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split() # Array of numbers from 20-90 in tens
        
        def word(n):
            if n < 20: return to19[n-1:n] # Getting the words of numbers below 20
            if n < 100: return [tens[n//10 - 2]] + word(n%10) # Getting words of number in their 10 from 20 to 90
            if n < 1000: return [to19[n//100 - 1]] + ['Hundred'] + word(n%100) # words fo number in their hundreds
            for i,v in enumerate(('Thousand', 'Million', 'Billion')): # enumerating the array with sufixs after 100s
                if n < 1000**(i+1): #this is to break the recurssion loop 
                    return word(n//1000**i) + [v] + word(n%1000**i)
        return ' '.join(word(num)) if num > 0 else 'Zero' #for the zero border case