'''
Part 1
The reallocation routine operates in cycles. In each cycle, it finds the memory bank with the most blocks 
(ties won by the lowest-numbered memory bank) and redistributes those blocks among the banks. To do this, 
it removes all of the blocks from the selected bank, then moves to the next (by index) memory bank and 
inserts one of the blocks. It continues doing this until it runs out of blocks; if it reaches the last 
memory bank, it wraps around to the first one.
how many redistributions can be done before a blocks-in-banks configuration is produced 
that has been seen before

Part 2
starting from a state that has already been seen, how many block redistribution cycles must be 
performed before that same state is seen again?
'''

with open('AOC2017_6.data', 'r') as f:
    banks = [int(x) for x in f.read().split('\t')]

past = []
steps = 0
while True:
    steps += 1
    i = banks.index(max(banks))
    blocks = banks[i]
    banks[i] = 0
    while blocks:
        i = (i+1)%(len(banks))
        banks[i] += 1
        blocks -= 1
    banks_string = ''.join(str(i) for i in banks) 
    if banks_string not in past:
        past.append(banks_string)
    else:
        print('part 1:',steps)
        print('part 2:', steps - past.index(banks_string)-1)
        break
        
        

        

