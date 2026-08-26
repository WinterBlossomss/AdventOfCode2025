file = open("adventofcode_secretentrance.txt", "r")
lines = [line.rstrip("\n") for line in file]
file.close()

# graph - device -> list of output devices
graph = {}
for line in lines:
    if not line.strip():
        continue
    name, outs = line.split(": ")
    graph[name] = outs.split(" ")

start = "svr"
end = "out"
req1 = "dac"
req2 = "fft"

memo = {}

def paths_needing(node, need1, need2):
    key = (node, need1, need2)
    if key in memo:
        return memo[key]

    if node == end:
        result = 1 if (not need1 and not need2) else 0
        memo[key] = result
        return result

    # If this node satisfies a requirement, it no longer needs to be found down the line since it is already counted
    new_need1 = need1 and (node != req1)
    new_need2 = need2 and (node != req2)

    total = 0
    for neighbor in graph.get(node, []):
        total += paths_needing(neighbor, new_need1, new_need2)

    memo[key] = total
    return total

result = paths_needing(start, True, True)
print(result)