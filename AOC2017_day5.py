with open('AOC2017_5.data', 'r') as f:
    data = [int(x) for x in f.read().split('\n')]

'''
follow the jumps until one leads outside the list.
after each jump, the offset of that instruction increases by 1'''
steps = 0
i = 0
while True:
    try:
        offset =  data[i]
        data[i] += 1
        i += offset
        steps += 1
    except IndexError:
        print('part 1:', steps)
        break
        
with open('AOC2017_5.data', 'r') as f:
    data = [int(x) for x in f.read().split('\n')]

    
'''after each jump, if the offset was three or more, instead decrease it by 1. 
Otherwise, increase it by 1 as before'''
steps = 0
i = 0
while True:
    try:
        offset =  data[i]
        if offset >= 3:
            data[i] -= 1
        else:
            data[i] += 1
        i += offset
        steps += 1
    except IndexError:
        print('part 2:', steps)
        break

