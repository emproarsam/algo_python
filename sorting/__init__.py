
INF = float("inf")

def random_list_generator():
    import random
    list_size = int(str(input('Enter size of a list!!!')).strip())
    list_slice = int(str(input('Enter slice for the list!!!')).strip())
    input_list = [random.randint(1, i) for i in range(1, list_size+1, list_slice)]
    return input_list

def swap(seq,i,j):
    temp = seq[i]
    seq[i] = seq[j]
    seq[j] = temp