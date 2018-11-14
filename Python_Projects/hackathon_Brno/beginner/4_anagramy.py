list = ['chocolate', 'cote']
letter = []

def is_anagram(list):
    i = 0
    is_anagram = False
    while i < len(list): 
        for y in list[i]:
            letter.append(y)  
            letter.sort()
            for x in letter:
                if x in list[i + 1]:
                    is_anagram = True

        i += 1
            
    return (letter)
 
print(is_anagram(list))