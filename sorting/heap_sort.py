from sorting import swap


def build_max_heap(seq):
    size = seq[0]
    for i in list(range(int(size/2), 0, -1)):
        max_heapify(seq, i)


def max_heapify(seq, pos):

    l_child = 2 * pos
    r_child = l_child + 1
    largest = pos

    if l_child <= seq[0] and seq[l_child] > seq[pos]:
        largest = l_child

    if r_child <= seq[0] and seq[r_child] > seq[largest]:
        largest = r_child

    if largest != pos:
        swap(seq, pos, largest)
        max_heapify(seq, largest)


if __name__ == "__main__":

    input_array = [9, 2, 15, 10, 18, 7, 3, 4, 0, 1]
    org_input_array = input_array[:]
    build_max_heap(input_array)
    print('For given array :\n{0}\nheap array is:\n{1}'.format(org_input_array, input_array))
