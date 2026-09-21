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

memo = {}

def count_paths(node):
    if node == end:
        return 1
    if node in memo:
        return memo[node]
    total = 0
    for neighbor in graph.get(node, []):
        total += count_paths(neighbor)
    memo[node] = total
    return total

result = count_paths(start)
print(result)