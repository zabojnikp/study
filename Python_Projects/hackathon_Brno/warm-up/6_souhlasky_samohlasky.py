user_input = 'a speech sound that is produced by comparatively open configuration of the vocal tract'
raw_text = user_input.replace(" ", '')

vowels = []
consonants = []
sentence = {}

for i in raw_text:
    if i.lower() in "aeiouy":
        vowels.append(i)
    else:
        consonants.append(i)

sentence["vowels"] = len(vowels)
sentence['consonants'] = len(consonants)
print(sentence)