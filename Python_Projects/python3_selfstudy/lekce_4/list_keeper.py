import os 

def main():
    fileSaved = False
    items = []
    filename, items = choose_file()
    print("Strazce seznamu")
   
    while True:
        print_items(items)
        user_choice = get_user_choice(items, fileSaved)
        
        if user_choice in "Pp":
            item = add_item(items)
            print("Prvek {0} byl pridan do souboru".format(item))
        elif user_choice in 'Vv':
            item = delete_item(items)
            if item is not None:
                print("Prvek {0} byl smazan ze souboru".format(item))
        elif user_choice in "Uu":
            save_items(filename, items)
            next_actions = get_string("Chcete pokracovat? (a / n)", field='continue', default='a') 
            if next_actions.lower() in ('a', 'ano'):
                continue
            else:
                break
        else:
            close_file(filename, items)
            break
    print('Goodbye!')


def choose_file():
    ''' Returns filename of selected file or newly created file''' 
    
    enter_filename = False
    files = [file for file in os.listdir('.') if file.endswith('.lst')]
    if files:
        try:
            index = int(get_string("Zvolte cislo souboru nebo 0 pro vytvoreni noveho", 'cislo souboru', default=0))
            if index == 0:
                enter_filename = True
            else:
                filename = files[index - 1]
                items = load_file_items(filename)
        except ValueError:
            print("Integer error")
    else:
        enter_filename = True
    
    if enter_filename:
        filename = get_string("Zadejte jmeno noveho souboru", 'filename')     
        if not filename.endswith('.lst'):
            filename += '.lst'
        items = []
    return filename, items

def load_file_items(filename):
    fh = None
    items = []
    try:
        for line in open(filename, encoding="utf8"):
            items.append(line.rstrip())
    except EnvironmentError:
        print("Not able to load {} file".format(filename))
    finally:
        if fh is not None:
            fh.close()
    return items

def print_items(items):
    if not items:
        print("-- v seznamu nejsou zadne prvky --")
    else:
        for i, item in enumerate(items):
            print('{0}: {item}'.format(i + 1, **locals()))
    print()

def get_string(message, field='string', default=None):
    message += ": " if default is None else " [{0}]: ".format(default)
    while True:
        try:
            user_input = input(message)
            if not user_input:
                if default is not None:
                    return default
                else:
                    raise ValueError("{field} nesmi byt prazdny/a".format(**locals()))
            return user_input
        except ValueError as err:
            print('String Error!', err)

def get_user_choice(items, fileSaved):
    while True:
        if items:
            if not fileSaved:
                menu ="[P]řidat   [V]ymazat   [U]lozit   [K]onec" 
                valid_choice = 'PpVvUuKk'
            else:
                menu ="[P]řidat   [V]ymazat   [K]onec" 
                valid_choice = 'PpVvKk'

        else:
            menu ="[P]řidat   [K]onec"
            valid_choice = 'PpKk'
        
        user_choice = get_string(menu, field="menu", default='P')
        
        if user_choice not in valid_choice:
            print("CHYBA: neplatná volba--zadejte některou z těchto možností: '{0}'".format(valid_choice))
            input("Pro pokracovani stisknete klavesu Enter ...")
            

        else:
            return user_choice

def add_item(items):
    item = get_string("Pridat prvek", "item")
    items.append(item)
    items.sort(key=str.lower)
    return item

def delete_item(items):
    try:
        index = int(get_string("Zadej index na vymazani daneho prvku (nebo 0 pro zruseni mazani)", field='delete', default=0))
        if index != 0:
            item = items.pop(index - 1)
            return item
    except ValueError:
        print("Integer error")

def save_items(filename, items):
    fh = None
    try:
        fh = open(filename, "w", encoding="utf8")
        fh.write('\n'.join(items))
        fh.write('\n')
    
    except EnvironmentError as err:
        print("Nemohu ulozit {0}: {1} ".format(filename, err))

    else:
        print("Seznam byl ulozed do {0}, celkem ulozeno prvku: {1}".format(filename, len(items)))
    
    finally:
        if fh is not None:
            fh.close()
    
    return len(items)

def close_file(filename, items):
    save_changes = get_string("Ulozit provedene zmeny (a/n)", 'save_changes', default='a')
    if save_changes.lower() in ('a', 'ano'):
        save_items(filename, items)

main()