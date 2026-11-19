class Solution:
    def frequencySort(self, s: str) -> str:
        counts={}
        x=list(s)
        for letter in s:
            counts[letter]=counts.get(letter,0)+1
        
        x.sort(key=lambda ch:counts[ch],reverse=True)
        return ''.join(x)
        

        

        