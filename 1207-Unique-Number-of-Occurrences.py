class Solution(object):
    def uniqueOccurrences(self, arr):
        counter = {}
        for num in arr:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        
        occurrence_count = {}
        
        for count in counter.values():
            if count in occurrence_count:
                return False  
            else:
                occurrence_count[count] = 1
        
        return True  

        