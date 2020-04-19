"""
Program for merge sort
Intuition: Classic Divide and Conquer approach
Divide - array of size n in two halves n/2 each
Conquer - Sort using merge sort
Combine - combine two sorted sub-arrays into completely sorted one.
@> k.saurabh.smk@gmail.com
"""
from typing import List

class MergeSort():

    def _merge(self, left: List[int], right: List[int]) -> List[int]:
        """
        :param left: left half of array
        :param right: right half of array
        return sorted_array
        """
        left_index, right_index = 0, 0
        sorted_array = []

        while(left_index < len(left) and right_index < len(right)):
            if left[left_index] <= right[right_index]:
                sorted_array.append(left[left_index])
                left_index += 1
            else:
                sorted_array.append(right[right_index])
                right_index += 1

        sorted_array += left[left_index:]
        sorted_array += right[right_index:]
        return sorted_array

    def merge_sort(self, array: List[int]) -> List[int]:
        """
        :param array: array to be sorted
        :return: sorted array
        """
        if len(array) <= 1:
            return array
        half = len(array) // 2
        left_half = self.merge_sort(array[:half])
        right_half = self.merge_sort(array[half:])
        merge = self._merge(left_half, right_half)
        return merge

if __name__ == '__main__':
    input_string = input("Enter elements to sort with spaces:   ")
    split_string = input_string.split()
    input_array = [int(x) for x in split_string]
    sorted_array = MergeSort()
    sorted_array = sorted_array.merge_sort(input_array)
    print('Sorted: ', sorted_array)
