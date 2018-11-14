import operator

user_input =  [1,21,5,3,5,8,321,1,2,2,32,6,9,1,4,6,3,1,2]

def get_dic_keys(data_list):
    values = set()
    for i in data_list:     
       values.add(i)
    return values

key_values = get_dic_keys(user_input)
items_count = dict()

for i in key_values:
    appearce = user_input.count(i)
    items_count[i] = appearce

print(items_count)
print("Item | Count")

sorted_d = sorted(items_count.items(), key=lambda x: x[1], reverse=True)

for k,v in sorted_d:
    print("{k} | {v}".format(**locals()))
