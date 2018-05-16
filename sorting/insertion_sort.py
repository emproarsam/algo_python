
from sorting import random_list_generator

def insertion_sort(_input):
    """
    Insertion Sort
    :real life example: sorting through playing cards
    :algo type: Sorting
    :time complexity: O(n^2)
    :space complexity : O(1)
    :param _input: list to be sorted
    :return: sorted list
    """

    for i in range(1, len(_input)):
        x = _input[i]
        j = i-1
        while j >= 0 and _input[j] > x:
            _input[j+1] = _input[j]
            j -= 1
        _input[j+1] = x
    return _input

if __name__ == "__main__":
    input_list = random_list_generator()
    print(input_list)
    print(insertion_sort(input_list))
    #print(insertion_sort([123, 2,5,6,8,33,66,88,11]))
