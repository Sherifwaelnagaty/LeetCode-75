class Solution:
    def compress(self, chars):
        if len(chars) <= 1:
            return len(chars)

        write_index = 0
        read_index = 0

        while read_index < len(chars):
            current_char = chars[read_index]
            count = 0

            while read_index < len(chars) and chars[read_index] == current_char:
                read_index += 1
                count += 1

            chars[write_index] = current_char
            write_index += 1

            if count > 1:
                for digit in str(count):
                    chars[write_index] = digit
                    write_index += 1

        return write_index
