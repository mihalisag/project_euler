# 10/05/19

from sqrt2 import srt
import time

sq_num = [i**2 for i in range(1,10)]
l = []

def p80():
    for i in range(1,100):
        if i not in sq_num:
            a = srt(i,102)
            a = list(a[:101])
            a.remove('.')
            b = [int(i) for i in a]
            l.append(sum(b))

    return l

if __name__ == '__main__':
    start = time.time()
    a = p80()
    end = time.time()-start
    print(sum(a),end)
