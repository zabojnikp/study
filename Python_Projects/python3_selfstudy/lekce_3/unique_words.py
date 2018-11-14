import sys
import collections

words = collections.defaultdict(int)
if len(sys.argv) > 1: 
    for filename in sys.argv[1:]:
        for line in open(filename, encoding="utf8"):
            for word in line.lower().split():
                word = word.strip()
                if len(word) > 2:
                    words[word] += 1

    for word in sorted(words):
        print("'{0}' se vyskytuje {1}.krat".format(word, words[word]))

else:
    print("Pouziti: 'python unique_words.py <filename>'")
