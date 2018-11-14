import sys
import unicodedata

#print out table
def print_unicode_table(word):
    print('{:^10} {:^10} {:^10} {:^40}'.format('oct', 'hexa', 'char', 'title'))
    print('{0:-^10} {0:-^10} {0:-^10} {0:-^40}'.format(''))
    
    number = ord(" ")
    end = min(0xD800, sys.maxunicode)
    while number < end:
        char = chr(number)
        name = unicodedata.name(char, '**UNKNOWN**' )
        for word in words:
            if word in name.lower() or word == '0':
                print('{0:^10} {0:^10X} {0:^10c} {1}'.format(number, name.title())) #vypis jenom ty, ktere splnuji podminku
        number += 1

words = []
if len(sys.argv) > 1:
    if sys.argv[1] in {'-h', '--help'}:
        print("použití: {0} [řetězec]".format(sys.argv[0]))
        words = None

    else:
        for word in sys.argv[1:]:
            words.append(word.lower())
        print_unicode_table(words)

else:
    words.append('0')
    print_unicode_table(words)