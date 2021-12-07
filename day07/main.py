from copy import deepcopy

for n in ("input", "test-input"):
    globals()[n.replace("-", "_")] = list(map(int, open(n).read().split(",")))

def part1(input):
    crabs = deepcopy(input)

    best_align = float("inf")

    for i in range(min(crabs), max(crabs)+1):
        fuel = 0
        for crab in crabs:
            fuel += abs(crab-i)
        
        if fuel < best_align:
            best_align = fuel
    
    return best_align

print("[part 1] test input", part1(test_input))
print("[part 1] test input", part1(input))

def part2(input):
    crabs = deepcopy(input)

    best_align = float("inf")

    for i in range(min(crabs), max(crabs)+1):
        fuel = 0
        for crab in crabs:
            fuel += sum(j for j in range(1, abs(crab-i)+1))
        
        if fuel < best_align:
            best_align = fuel
    
    return best_align

# this is super-slow but i was tired

print("[part 2] test input", part2(test_input))
print("[part 2] test input", part2(input))