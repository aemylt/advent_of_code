import itertools

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)

with open("input/day_5.txt") as input:
    polymer = input.read()[:-1]
    encoding = [ord(poly) for poly in polymer]
    diff = [abs(chr1 - chr2) for chr1, chr2 in pairwise(encoding)]
    while 32 in diff:
        index = diff.index(32)
        polymer = polymer[:index] + polymer[index+2:]
        encoding = [ord(poly) for poly in polymer]
        diff = [abs(chr1 - chr2) for chr1, chr2 in pairwise(encoding)]
    print(len(polymer))
