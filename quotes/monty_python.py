import numpy as np

quote = {}

quote[1] = '''
    Strange women lying in ponds distributing swords
    is no basis for a system of -------.
    '''

quote[2] = '''
    I am an enchanter. There are some who call me… ----.
    '''

quote[3] = '''
    King Arthur: “Look, you stupid b***ard, you’ve got no arms left!”
    Black Knight: “Yes I have.”
    King Arthur: “Look!”
    Black Knight: “It’s just a ------ ------…”
    '''



def holy_grail(num):
    return quote[num]


if __name__ == '__main__':
    num  = np.random.randint(1, 8)
    holy_grail(num)
