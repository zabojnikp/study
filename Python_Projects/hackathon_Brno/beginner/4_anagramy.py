words = ['ships', 'hips']
matching_words = []

def is_anagram(list):
    if not words:
        return False
   
    i = 0
    matching_words.append(list[i])
    while i < (len(words) - 1):
        if sorted(list[i].lower()) == sorted(list[i+1].lower()):
            matching_words.append(list[i + 1])
        i += 1
    return len(matching_words) == len(words)

print(is_anagram(words))