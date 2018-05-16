

def min_max(seq):
    """
    :param seq: input sequence
    :return: gives min and max
    """

    _min = float("inf")
    _max = 0
    for i in seq:
        if i < _min:
            _min = i
        if i > _max:
            _max = i
    return _min, _max


def rec_min_max(seq, _max=0, _min=float("inf")):
    """
    :complexity : T(n) = T(n-1) + 2  =>  O(n-1)
    :param seq: input sequence
    :param _max: maximum
    :param _min: minimum
    :return: gives min and max
    """
    if not seq:
        return _max, _min
    _max = (_max >= seq[0]) and _max or seq[0]
    _min = (_min <= seq[0]) and _min or seq[0]
    return rec_min_max(seq[1:], _max, _min)


def rec_min_max2(seq, _max=0, _min=float("inf")):
    """
    :complexity : T(n) = T(n-2) + 3  => O(3n/2)
    :param seq: input sequence
    :param _max: maximum
    :param _min: minimum
    :return: gives min and max
    """
    if not seq:
        return _max, _min
    if seq[0] > seq[1]:
        _max = (_max >= seq[0]) and _max or seq[0]
        _min = (_min <= seq[1]) and _min or seq[1]
    else:
        _max = (_max >= seq[1]) and _max or seq[1]
        _min = (_min <= seq[0]) and _min or seq[0]
    return rec_min_max(seq[2:], _max, _min)


if __name__ == "__main__":

    l = [34, 40353, -46, 456, 40086, -7, -657, 56, 856232, 85, 685]
    # lowest, highest = min_max(l)
    # print('In the list :\n{}\nmin  =  {}\nmax  =  {}'.format(l, lowest, highest))
    lowest, highest = rec_min_max(l)
    print(lowest, highest)
