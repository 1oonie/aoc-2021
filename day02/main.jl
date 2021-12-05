# https://adventofcode.com/2021/day/2

function get_data(filename)
    f = open(filename)
    data = String(read(f))
    
    ret = Any[]

    for (index, line) in enumerate(split(data, "\n"))
        parts = split(line, " ")
        push!(ret, [parts[1], parse(Int, parts[2])])
    end
    return ret
end

function part1(filename)
    data = get_data(filename)

    horizontal = 0
    depth = 0

    for item in data
        command = item[1]
        amount = item[2]

        if command == "forward"
            horizontal += amount
        elseif command == "down"
            depth += amount
        else
            depth -= amount
        end
    end

    return horizontal*depth
end

println("[part 1] test input ", part1("test-input"))
println("[part 1] actual input ", part1("input"))

println("\n")

function part2(filename)
    data = get_data(filename)

    horizontal = 0
    depth = 0
    aim = 0

    for item in data
        command = item[1]
        amount = item[2]

        if command == "forward"
            horizontal += amount
            depth += aim * amount
        elseif command == "down"
            aim += amount
        else
            aim -= amount
        end
    end

    return horizontal*depth
end

println("[part 2] test input ", part2("test-input"))
println("[part 2] actual input ", part2("input"))