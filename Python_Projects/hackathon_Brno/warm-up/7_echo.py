user_sentense = 'I do not want to work today'
count = 4
new_sentense = ''

words = user_sentense.split()

for i in words:
    new_sentense += (" " + i + " ") * count

print(new_sentense.strip())