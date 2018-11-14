import sys

if len(sys.argv) < 3:
    print("Use: grep_word.py word <filename>")
    sys.exit()


word = sys.argv[1]
for filename in sys.argv[2:]:
    for line_number, line in enumerate(open(filename), start=1):
        if word in line.lower():
            print("{0}:{1}:{2}".format(filename,line_number, line.strip()))