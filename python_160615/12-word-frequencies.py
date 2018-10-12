import sys
import fileinput
import re
from collections import defaultdict

WORD_PATTERN = re.compile(r"[\w']+")

def read_all_words():
    words = []
    for line in fileinput.input():
        new_words = WORD_PATTERN.findall(line)
        words += new_words
    return words

def word_frequencies(words):
    result = defaultdict(int)
    for word in words:
        word = word.lower()
        result[word] += 1
    return result

def assertEqual(first, second, msg=""):
    if first != second:
        msg += "\n{0!r} != {1!r}".format(first, second)
        raise AssertionError(msg)

def run_tests():
    assertEqual(word_frequencies([]), {})
    assertEqual(word_frequencies(["foo", "foo", "foo"]), {"foo": 3})
    assertEqual(word_frequencies(["hi", "HI"]), {"hi": 2})

    print("All tests passed successfully.")

arguments = sys.argv[1:]

if arguments == ["test"]:
    run_tests()
else:
    words = read_all_words()
    frequencies = word_frequencies(words)
    common_words = sorted(frequencies.keys(), key = frequencies.get, reverse = True)
    for word in common_words:
        count = frequencies[word]
        print("{0:5d}   {1}".format(count, word))