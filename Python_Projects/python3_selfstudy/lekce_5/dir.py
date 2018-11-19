import optparse
import os
import datetime

def main():
    opts, path = process_option()
    dir_names = []
    file_names = []

    if not opts.recursive:
        for file in os.listdir(path[0]):
            if file.startswith('.') and not opts.hidden:
                continue
            fullname = os.path.join(path[0], file)
            if os.path.isfile(fullname):
                file_names.append(fullname)
            else:
                dir_names.append(fullname)
    else:
        for root, dirs, files in os.walk(path[0]):
            for name in files:
                if name.startswith('.') and not opts.hidden:
                    continue
                file_names.append(os.path.join(root, name))
            for name in dirs:
                dir_names.append(os.path.join(root, name))
   
    summary_line = get_summary_line(file_names, dir_names)
    file_names.extend(dir_names)
    file_dir_data, order_key = get_items_info(opts, file_names)
    file_dir_data.sort(key=lambda x: str(x[order_key]))
    
    for i in range(0, len(file_dir_data)):
        print("{0[0]} {0[1]:^10} {0[2]:>5} {0[3]}".format(file_dir_data[i]))
    print(summary_line)

def get_items_info(opts, items):
    items_info = []
    for item in items:
        modified = datetime.datetime.fromtimestamp(os.path.getmtime(item)).strftime("%m/%d/%Y %I:%M %p")
        folder = '<DIR>' if os.path.isdir(item) else ''
        size = ''
        if os.path.isfile(item):
            size = os.path.getsize(item) if opts.sizes else ''
        items_info.append((modified, folder, size, item))
    
    order_key = 0 if opts.order in {"m", "modified"} else (2 if opts.order in {"s", "size"} else 3)
    return items_info, order_key

def get_summary_line(filenames_list, dirnames_list):
    list_count = (len(filenames_list), len(dirnames_list))
    summary_line = "\n"
    filetype = "soubor"
    for i in range(0, len(list_count)):
        number = list_count[i] if list_count[i] else "zadny"
        string_ending = "y" if list_count[i] in range(2,5) else ("" if list_count[i] in range(0,2) else "u")
        if string_ending == "y" and filetype == "adresar":
            string_ending = 'e'
        summary_line += " {number} {filetype}{string_ending}".format(**locals())
        filetype = "adresar"
    return summary_line
        

def process_option():
    usage = "usage: %prog [options] arg1 arg2"
    parse = optparse.OptionParser(usage=usage)
    parse.add_option("-H", "--hidden", dest='hidden', action="store_true", help="show hidden all_files [default = off]")
    orderList = ["name", "n", "modified", "m", "size", "s"]
    parse.add_option('-o', "--order", dest='order', help="order result based on {0} [default = %default]".format(orderList))
    parse.add_option("-r", "--recursive", dest='recursive', action="store_true", help="sestupuje rekurzivne do podadresaru [default = off]")
    parse.add_option("-s", "--sizes", dest='sizes', action="store_true", help="shows file size [defalut = off]")
    parse.set_defaults(order=orderList[0])
    options, args = parse.parse_args()
    
    if not args:
        args = ["."]
    return options, args

main()