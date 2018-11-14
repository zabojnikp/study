import collections
tasks = collections.OrderedDict()
tasks[8031] = "Backup"
tasks[4027] = "Scan email"
tasks[5733] = "Build system"
tasks[8031] = "Denni zaloha"
print(list(tasks.keys()))

unsorted = dict()
unsorted[8031] = "Backup"
unsorted[4027] = "Scan email"
unsorted[5733] = "Build system"
unsorted[8031] = "Denni zaloha"

print(list(unsorted.keys()))