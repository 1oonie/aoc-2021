import copy
from collections import defaultdict

for n in ("input", "test-input"):
    globals()[n.replace("-", "_")] = list(map(int, open(n).read().split(",")))

def part1(fish):
    fish = copy.deepcopy(fish)
    for _ in range(80):
        for n, f in list(enumerate(fish)):
            if f == 0:
                fish.append(8)
                fish[n] = 6
            else:
                fish[n] -= 1
    
    return len(fish)


print("[part 1] test input", part1(test_input))
print("[part 1] test input", part1(input))

def part2(input):
    fish = defaultdict(int)
    for i in input:
        fish[i] += 1

    for _ in range(256):
        count = fish[0]
        del fish[0]
        
        newfish = defaultdict(int)
        for i in fish:
            newfish[i-1] = fish[i]
        fish = newfish

        fish[8] = count
        fish[6] += count        
    
    return sum(fish.values())

print("[part 2] test input", part2(test_input))
print("[part 2] test input", part2(input))