class TDDExample():
    def __init__(self):
        pass

    def reverse_string(self, input_str: str) -> str:
        """
        Reverses order of characters in string input_str.
        """
        output_str = input_str[::-1]
        return output_str

    def find_longest_word(self, sentence: str) -> str:
        """
        Returns the longest word in string sentence.
        In case there are several, return the first.
        """
        words = sentence.split()
        long_w = ''
        for word in words:
            if len(word) > len(long_w):
                long_w = word

        return long_w

    def reverse_list(self, input_list: list) -> list:
        """
        Reverses order of elements in list input_list.
        """
        output_list = input_list[::-1]
        return output_list

    def count_digits(self, input_list: list, number_to_be_counted: int) -> int:
        """
        Return count of digits
        """
        count = 0

        for i in input_list:
            if i == number_to_be_counted:
                count = count + 1
        return count
    
obj = TDDExample()
obj.reverse_list([1,2,3,3])
obj.reverse_string('fksjdlf')

