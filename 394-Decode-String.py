class Solution:
    def decodeString(self,s: str) -> str:
        arr = []
        current_number = 0
        current_string = ''
        
        for char in s:
            if char.isdigit():
                current_number = current_number * 10 + int(char)
            elif char == '[':
                arr.append((current_string, current_number))
                current_string = ''
                current_number = 0
            elif char == ']':
                prev_string, repeat_times = arr.pop()
                current_string = prev_string + current_string * repeat_times
            else:
                current_string += char
        
        return current_string

        