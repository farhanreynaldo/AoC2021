from collections import defaultdict

SAMPLES = """
fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW
"""


def valid_path(node, seen, dest_list):
    if node == "end":
        return 1
    if node in seen and node.islower():
        return 0
    seen = seen | {node}
    val = 0
    for dest in dest_list[node]:
        val += valid_path(dest, seen, dest_list)
    return val


def total_path(input):
    paths = input.strip().split("\n")
    dest_list = defaultdict(list)
    for path in paths:
        begin, end = path.split("-")
        dest_list[begin].append(end)
        dest_list[end].append(begin)

    return valid_path("start", set(), dest_list)


assert total_path(SAMPLES) == 226
input = open("input/day12.txt").read()
print(total_path(input))


def valid_path_twice(node, seen, dest_list, visited):
    if node == "end":
        return 1
    if node == "start" and seen:
        return 0
    if node in seen and node.islower():
        if visited is None:
            visited = node
        else:
            return 0
    seen = seen | {node}
    val = 0
    for dest in dest_list[node]:
        val += valid_path_twice(dest, seen, dest_list, visited)
    return val


def total_path_twice(input):
    paths = input.strip().split("\n")
    dest_list = defaultdict(list)
    for path in paths:
        begin, end = path.split("-")
        dest_list[begin].append(end)
        dest_list[end].append(begin)

    return valid_path_twice("start", set(), dest_list, visited=None)


assert total_path_twice(SAMPLES) == 3509
print(total_path_twice(input))
