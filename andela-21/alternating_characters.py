# Enter your code here. Read input from STDIN. Print output to STDOUT
def count_(token):

    count = 0
    for index, letter in enumerate(list(token)):
        if index > 0 and token[index-1] == letter:
            count += 1
    return count

for _ in xrange(input()):
    print count_(raw_input())