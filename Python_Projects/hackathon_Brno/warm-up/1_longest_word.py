
word_list = ['Python', 'is', 'a', 'widely', 'used', 'high-level', 'programming',
        'language', 'for', 'general-purpose', 'programming,', 'created',
        'by', 'Guido', 'van', 'Rossum', 'and', 'first', 'released', 'in', '1991.']

words = {}

def get_longest_word(list):
    for index in word_list:     
        words[index] = len(index)
     
    max_value = max(words.values())
    for k,v in words.items():
        if v == max_value:
            return k, v


print("Output: ", get_longest_word(word_list))
