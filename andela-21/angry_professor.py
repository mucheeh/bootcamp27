#!/usr/bin/py
if __name__ == '__main__':
    t = input()
    for _ in xrange(t):
        h, m = map(int, raw_input().split())
        A = map(int, raw_input().split())
        for k in A:
            if k <= 0:
                m -= 1
        if m <= 0:
            print "NO"
        else:
            print "YES"