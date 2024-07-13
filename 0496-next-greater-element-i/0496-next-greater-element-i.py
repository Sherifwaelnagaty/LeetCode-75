class Solution:
    def nextGreaterElement(self, array: List[int], array2: List[int]) -> List[int]:
        stack = []
        new_array = []
        
        for i in range(len(array2) - 1, -1, -1):
            if len(stack) == 0:
                new_array.append(-1)
            elif len(stack) > 0 and stack[-1] > array2[i]:
                new_array.append(stack[-1])
            elif len(stack) > 0 and stack[-1] <= array2[i]:
                while len(stack) > 0 and stack[-1] <= array2[i]:
                    stack.pop()
                
                if len(stack) == 0:
                    new_array.append(-1)
                else:
                    new_array.append(stack[-1])
            stack.append(array2[i])
        new_array = new_array[::-1]

        result = [0]*len(array)
        k = 0
        for i in range(len(array)):
            for j in range(len(array2)):
                if array[i] == array2[j]:
                    result[k] = new_array[j]
                    k += 1
        return result