from sorting import swap


def bubble_sort(seq):
    """

    :param seq: input sequence
    :return: sorted list
    """
    global switch
    switch = True

    _seq = seq[:]
    for i in range(len(_seq)):
        if not switch:
            continue
        switch = False
        for j in range(1, len(_seq)-i):
            if _seq[j-1] > _seq[j]:
                swap(_seq, j-1, j)
                switch = True
            j += 1
    return _seq


if __name__ == "__main__":
    input_list = [1312, 54, 33, 355, 67, -252, -8, 60, -78, 5, 4, 736, 2, 5325]
    print('For a given list:\n{}\nThe sorted list is:\n{}'.format(input_list, bubble_sort(input_list)))
