class Solution(object):
    def largestAltitude(self, gain):
        result = 0
        highest_element = 0

        for i in range(len(gain)):
            result += gain[i]
            highest_element=max(highest_element,result)
            
        return highest_element
  


        
        