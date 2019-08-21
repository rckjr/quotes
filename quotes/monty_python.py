import numpy as np

def holy_grail(num):
    quote = {}

    quote[1] = '''
    Strange women lying in ponds distributing swords 
    is no basis for a system of -------.
    '''

    print(quote[num])

    
if __name__ == '__main__':
    num  = np.random.randint(1, 8)
    holy_grail(num)
