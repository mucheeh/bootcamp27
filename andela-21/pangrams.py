# Enter your code here. Read input from STDIN. Print output to STDOUT
def getCharCnt(s):
    return len(set(c.lower() for c in s if c != ' '))
 
if __name__ == '__main__':
    s = raw_input()
    if getCharCnt(s) == 26:
        print "pangram"
    else:
        print "not pangram"
