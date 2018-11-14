import os 

def main():
    saved = False
    files = []
    filename, files = choose_file()
    
    while True:
        print("Strazce seznamu")
        print_files(files)
        choice = get_choice(files, saved)
        
        if choice in "Pp":
            item = add_item(files)
            print("Prvek {0} byl pridan do souboru".format(item))
        elif choice in 'Vv':
            item = delete_item(files)
            print("Prvek {0} byl smazan ze souboru".format(item))
        elif choice in "Uu":
            item = save_items(filename, files)
            if item:
                saved = True
            else:
                break
        #elif choice in "Kk":
            


def choose_file():
    ''' Returns filename of selected file or newly created file''' 
    
    enter_filename = False
    files = [file for file in os.listdir('.') if file.endswith('.lst')]
    if files:
        index = get_integer("Zvolte cislo souboru nebo 0 pro vytvoreni noveho", 'cislo souboru', default=0)
        if index == 0:
            enter_filename = True
        else:
            filename = files[index - 1]
    else:
        enter_filename = True
    
    if enter_filename:
        filename = get_string("Zadejte jmeno noveho souboru", 'filename')     
        if not filename.endswith('.lst'):
            filename += '.lst'
    return filename, files


def print_files(files):
    if not files:
        print("-- zatim neexistuji zadne soubory s priponou .lst --")
    else:
        for i, item in enumerate(files):
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
            print('Chyba!', err)


def get_integer(message, field='integer', default=None):
    message += ": " if default is None else " [{0}]: ".format(default)
    while True:
        try:
            user_input = input(message)
            number = int(user_input)
            if not number:
                if default is not None:
                    return default
                else:
                    raise ValueError("{field} nesmi byt prazdny/a".format(**locals()))
            return number
        except ValueError as err:
            print("Error!", err)


def get_choice(files, saved):
    while True:
        if files:
            if not saved:
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
    index = get_integer("Zadej index na vymazani daneho prvku (nebo 0 pro zruseni mazani)", field='delete')
    if index != 0:
        item = items.pop(index - 1)
        return item

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
        pokracovat = get_string("Chcete pokracovat? (a / n)", field='continue', default='a')
        if pokracovat.lower() in ("a", "ano"):
            return True
        else:
            return False
    
    finally:
        if fh is not None:
            fh.close()



main()