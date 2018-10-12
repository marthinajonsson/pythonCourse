def necklaces(N):
    for n in range(2 ** N):
        yield "{0:0{digits}b}".format(n, digits=N)

def has_N_white_beads(necklace, N):
    return necklace.count("1") == N

def flip(necklace):
    return necklace[::-1]

def rotate(string, steps):
    return string[steps:] + string[:steps]

def better_than_all_rotations_and_reflections(necklace):
    for i in range(1, len(necklace)):
        if necklace > rotate(necklace, i):
            return False
        if necklace > flip(rotate(necklace, i)):
            return False
    return True

WHITE_BEADS = 3
BLACK_BEADS = 13
TOTAL = WHITE_BEADS + BLACK_BEADS

for s in necklaces(TOTAL):
    if not has_N_white_beads(s, WHITE_BEADS):
        continue

    if not better_than_all_rotations_and_reflections(s):
        continue

    print(s)