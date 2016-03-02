''' This module is a collection of small procedures
used as solutions to multiple tasks from the CheckiO.org site.
I believe these short pieces of code can show my style 
of coding in Python.
All the solutions are authentic, not copied
'''
def brackets(expr):
    '''Find if all the brackets were closed in expr
    '''
    bracks_queue = ['']
    for sym in expr:
        if sym in ['(', ')','[', ']','{', '}']:
            b = bracks_queue[-1]
            if (b == '(' and sym == ')') or \
               (b == '[' and sym == ']') or \
               (b == '{' and sym == '}'):
                del bracks_queue[-1]
            else:
                bracks_queue.append(sym)
    if len(bracks_queue) == 1:
        return True
    return False

def restricted_sum(data):
    '''Get sum without using "sum", "for", "reduced" and some other 
       trivial methods
    '''
    if len(data) == 1:
        return data[0]
    n = data[0]
    return n + restricted_sum(data[1:])

def convertToRoman(data):
    '''Converts given number up to 4000 into roman
    '''
    lst = [[1, 'I'], [5, 'V'], [10, 'X'], [50, 'L'], [100, 'C'], [500, 'D'], 
           [1000, 'M']]
    lst.sort(reverse = True)
    pls = '' #for cases MMCM.., when the last M is a pls, that is a "plus"-string
    roman = ''
    for x in range(len(lst)):
        n, r = lst[x]
        if n in [1000, 100, 10, 1]:
            if (data % n) >= 0.9 * n:
                pls = r #cases when plus is occured
            roman += r * int(data / n)
            data = data % n 
        elif n in [500, 50, 5]:
            if pls:
                roman += lst[x+1][1] + pls
                pls = ''
                data = data % lst[x + 1][0]
            elif data >= n:
                roman += r + lst[x + 1][1] * int((data - n) / lst[x + 1][0])
                data = data % lst[x + 1][0]
            if n > data % (2 * n) >= 0.8 * n:
                roman += lst[x+1][1] + r
                data = data % lst[x + 1][0]
    return roman

def check_connection(network, first, second):
    '''Find out if two vertices in a graph are connected
    '''
    import collections
    adj_list = collections.defaultdict(set)
    #adj_list shows all the direct friends for each node
    for elmt in network:
        v1, v2 = [parts for parts in elmt.strip().split('-')]
        adj_list.setdefault(v1,[]).append(v2)
        adj_list.setdefault(v2,[]).append(v1)

    visited = []
    #root goes first
    if first in adj_list:
        if second in adj_list[first]:
            return True
        else:
            visited.append(first)
    #non-root elements in queue    
    friends_queue = [friends for friends in adj_list[first] if not friends in visited]
    while friends_queue:
        for fr in friends_queue:
            if second in adj_list[fr]:
                return True
            else:
                visited.append(fr)
                friends_queue += [fr1 for fr1 in adj_list[fr] if not fr1 in visited]
            friends_queue.remove(fr)
    print(visited)
    '''assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    '''
    return False



if __name__ == '__main__':
    print(u"(((1+(1+1))))] has correct brackets -- ",brackets(u"(((1+(1+1))))]"))
    print("2016 in Roman is ", convertToRoman(2016))