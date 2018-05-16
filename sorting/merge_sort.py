from sorting import random_list_generator,INF

def median(var1, var2):
    """
    gives middle value for range var1.......var2
    :param var1: starting array index
    :param var2: end array index
    :return: middle value
    """
    return int((var1+var2)/2)


def merge_sort(l,p,r):
    #print('{0} -- {1}'.format(p, r))
    q = median(p,r)
    if p<r:
        merge_sort(l,p,q)
        merge_sort(l,q+1,r)
        merge(l,p,q,r)

def merge(l,p,q,r):
    #n1 = q-p+1
    #n2 = r-q
    l_copy = l[:]
    l_n1 = l_copy[p:q+1]
    l_n2 = l_copy[q+1:r+1]
    l_n1.append(INF)
    l_n2.append(INF)
    #res=[]
    # i,j = 0,0
    # try:
    #     while 1:
    #         if l_n1[i]<=l_n2[j]:
    #             res.append(l_n1[i])
    #             i+=1
    #         else:
    #             res.append(l_n2[j])
    #             j+=1
    # except IndexError:
    #     while INF in res: res.remove(INF)

    ii,jj = 0,0
    for k in range(p,r+1):
        if l_n1[ii] <= l_n2[jj]:
            l[k] = l_n1[ii]
            ii += 1
        else:
            l[k] = l_n2[jj]
            jj += 1

    #l[p:r+1] = res
    #l = [res[i] if (i in range(p,r+1)) else x for i, x in enumerate(l)]

if __name__=="__main__":
    #print(median(1,6))
    #input_list = random_list_generator()
    input_list = [22,1,3,77,43,56,0,90]
    print(input_list)
    merge_sort(input_list, 0, len(input_list)-1)
    print(input_list)
