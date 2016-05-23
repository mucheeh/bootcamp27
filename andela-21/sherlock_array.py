# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

if __name__ == "__main__":
    for _ in range(int(sys.stdin.readline())):
        n = int(sys.stdin.readline())
        vector = list(map(int, sys.stdin.readline().split()))
        exists_same_sum = 'NO'
        
        if n > 2:
            h = sum(vector[:1])
            m = sum(vector[2:])
        
            for index in range(1, len(vector)-1):
                if h == m:
                    exists_same_sum = 'YES'
                    break
                    
                h += vector[index]
                m -= vector[index+1]
            print(exists_same_sum)
        elif n == 1:
            print('YES')
        else:
            print('NO')