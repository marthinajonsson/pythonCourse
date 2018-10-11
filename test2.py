# THIS IS THE SECOND FILE CONTAINING INFO FROM THE SECOND PART OF BEGINNERS COURSE INF PYTHON
# CLASSES AND FILE HANDLING

# think palindrome like deified
"defied"[::-1]

with open('files/words') as f:
	for line in f:
		line = line.rstrip()  #rstrip() removes final line break and whitespaces at the end of string
	#	print("test: ", line)
		if len(line) == 1:	
			continue
		if line[::-1] == line:
			print(line)


# STRINGS

WHITE_BEADS = 3
BLACK_BEADS = 13
TOTAL = WHITE_BEADS + BLACK_BEADS

def necklaces(N):
	return ["{:0{digits}b}".format(n, digits=N) for n in range(2 ** N)]

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


for s in necklaces(TOTAL):
	if not has_N_white_beads(s, WHITE_BEADS):
		continue

	if not better_than_all_rotations_and_reflections(s):
		continue
	print(s)


# DICTIONARIES
phone_numbers = [
	["Philip", "555-1234"],
	["Trazan", "555-4345"],
	["Hugo", "555-8067"],
]

phone_book = {}
for e in phone_numbers:
	phone_book[e[0]] = e[1]


print(dict(phone_numbers))
print(phone_book)

for name in phone_book.keys():
	print(name)


for number in phone_book.values():
	print(number)


for name in sorted(phone_book):
	print(name)


# {:s} string
# {:d} base 10 integer
# {:b} base 2 integer
# {:x} base 16 integer
# {:f} float number

# CLASSES AND OBJECTS
