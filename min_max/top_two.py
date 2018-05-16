
from sorting import swap
from sorting.merge_sort import median


def top_elements(seq, top=2):
    """
    :param seq: input sequence
    :param top: number of toppers
    :return: gives top two largest elements
    """
    _seq = seq[:]
    toppers = []
    for pos in range(top):
        _max = _seq[0]
        for i in _seq:
            if i > _max:
                _max = i
        toppers.append(_max)
        _seq.remove(_max)
    return toppers


def rec_top_elements(seq, i=2):
    """
    :complexity: T(n) = 2T(n-1) - 3
    :param seq: input sequence
    :param i: current index
    :return: gives top two largest elements
    """
    if len(seq) < 2:
        raise IndexError('Please pass a sequence of length greater than 2.!!!!')
    if i == len(seq):
        return seq[0], seq[1]
    if seq[0] < seq[i]:
        swap(seq, 0, i)
    elif seq[1] < seq[i]:
        swap(seq, 1, 0)
    return rec_top_elements(seq, i+1)


def play_off(p1, p2):
    if p1 > p2:
        return p1, p2
    else:
        return p2, p1


def tournament_winner(seq, l, r):
    """
    :source: https://www.youtube.com/watch?v=gwlevtaC-u0&index=1&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&t=3086s
                1:20:00
    :complexity: T(n) = T(n-1) + log n - 1
    :param seq: input sequence
    :param l: left index
    :param r: right index
    :return: gives top two largest elements
    """
    if l == r:
        return seq[l], seq[l]

    q = median(l, r)
    if l < r:
        player1, loser1 = tournament_winner(seq, l, q)
        player2, loser2 = tournament_winner(seq, q+1, r)
        winner, runner_up = play_off(player1, player2)
        return winner, runner_up


if __name__ == "__main__":

    input_l = [34, 40353, -46, 456, 40086, -7, -657, 856232]
    # winners = top_elements(input_l)
    # winners = rec_top_elements(input_l)
    # print('In the list :\n{}\ntop two elements are:{}\t{}'.format(input_l, *winners))
    print(tournament_winner(input_l, 0, len(input_l) - 1))
    # print('the winner and runner up are:\nIst --> {}\nIInd --> {}'.\
    # format(*tournament_winner(input_l, 0, len(input_l)-1)))
