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
    min_length = len(polymer)
    for unit in range(65,91):
        poly_opt = polymer.replace(chr(unit), "").replace(chr(unit).lower(), "")
        encoding = [ord(poly) for poly in poly_opt]
        diff = [abs(chr1 - chr2) for chr1, chr2 in pairwise(encoding)]
        while 32 in diff:
            index = diff.index(32)
            poly_opt = poly_opt[:index] + poly_opt[index+2:]
            encoding = [ord(poly) for poly in poly_opt]
            diff = [abs(chr1 - chr2) for chr1, chr2 in pairwise(encoding)]
        if len(poly_opt) < min_length:
            min_length = len(poly_opt)
    print(min_length)
