# https://adventofcode.com/2021/day/3

from collections import Counter
from copy import deepcopy

for n in ('test-input', 'input'):
    with open(n, 'r') as f:
        globals()[n.replace('-', '_')] = f.read().split('\n')

def part1(seq):
    gamma, epsilion = '', ''

    for i in range(0, len(seq[0])):
        counter = Counter(''.join(item[i] for item in seq))
        gamma += counter.most_common(1)[0][0]
        epsilion += counter.most_common()[-1][0]

    return int(gamma, base=2)*int(epsilion, base=2)

print("[part 1] test input", part1(test_input))
print("[part 1] actual input", part1(input))

def part2(seq):
    ox_rating = 0
    co_rating = 0

    def find(n):
        subl = deepcopy(seq)
        for i in range(0, len(seq[0])):

            common = Counter(''.join(item[i] for item in subl)).most_common()
            if n == -1:
                common = list(reversed(common))
            
            if len(common) == 1:
                common.append([int(not int(common[0][1])), 0])

            if common[n][1] == common[n+1][1]:
                c = '1' if n == 0 else '0'
            else:
                c = common[0][0]

            subl = list(filter(lambda item: item[i] == c, subl))
        return int(subl[0], 2)

    return find(0)*find(-1)
        
        

print("[part 2] test input", part2(test_input))
print("[part 2] actual input", part2(input))