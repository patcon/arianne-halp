import sys

usage = """Usage: {} <list file 1> <list file 2>

where each file has one item per line."""

try:
    files = [arg for arg in sys.argv[1:]]
    if len(files) is not 2: raise SyntaxError
    lists = [[line.strip() for line in open(file).readlines()] for file in files]
    sets = [set(l) for l in lists]
    common = list(sets[0].intersection(sets[1]))
    for match in common:
        print(match)
except SyntaxError:
    print(usage.format(sys.argv[0]))
