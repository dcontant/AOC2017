from itertools import combinations as comb
from collections import Counter

with open('AOC2017_4.data', 'r') as f:
    data = [passphrase.split(' ') for passphrase in f.read().split('\n')]
    
print('part 1:', sum(len(set(passphrase)) == len(passphrase) for passphrase in data))

print('part 2:', sum(all(Counter(a) != Counter(b) for a,b in comb(passphrase, 2)) for passphrase in data))
    
            
        
