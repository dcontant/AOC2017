from itertools import combinations as comb

with open('AOC2017_2.data','r') as f:
    data = [[int(x) for x in row.split('\t')] for row in f.read().split('\n')]
    
total = 0
total_2 = 0
for row in data:
    total += max(row)-min(row)
    for c in comb(row,2):
        a,b = sorted(c)
        if b%a == 0:
            total_2 += b//a
print('part 1:', total)
print('part 2:', total_2)
