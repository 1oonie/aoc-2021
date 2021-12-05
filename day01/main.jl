# https://adventofcode.com/2021/day/1

function get_numbers(filename)
    f = open(filename)
    data = String(read(f))
    
    numbers = Vector{Int}()

    for line in split(data, "\n")
        append!(numbers, parse(Int, line))
    end
    return numbers
end

function part1(filename)
    numbers = get_numbers(filename)

    pos = 2 # 1 is never applicable because it has no previous element
    count = 0

    while pos <= length(numbers)
        if numbers[pos] > numbers[pos-1]
            count += 1
        end
        pos += 1
    end

    return count
end

println("[part 1] test input ", part1("test-input"))
println("[part 1] actual input ", part1("input"))

println("\n")

function part2(filename)
    numbers = get_numbers(filename)

    pos = 2
    count = 0

    while pos <= length(numbers)-2 # last 2 cannot have enough to make a window
        if sum(numbers[pos:pos+2]) > sum(numbers[pos-1:pos+1])
            count += 1
        end
        pos += 1
    end

    return count
end

println("[part 1] test input ", part2("test-input"))
println("[part 2] actual input ", part2("input"))