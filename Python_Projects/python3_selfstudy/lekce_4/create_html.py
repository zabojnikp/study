import datetime
import xml.sax.saxutils

COPYRIGHT_TEMPLATE = "Copyright (c) {0} {1}. All rights reserved."

STYLESHEET_TEMPLATE = '<link rel="stylesheet" type"text/css" media="all" href="{0}" />\n'

HTML_TEMPLATE = """<?xml version="1.0"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" \
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="cs" xml:lang="cs">
<head>
<title>{title}</title>
<!-- {copyright} -->
<meta name="Description" content="{description}" />
<meta name="Keywords" content="{keywords}" />
<meta equiv="content-type" content="text/html; charset=utf-8" />
{stylesheet}\
</head>
<body>

</body>
</html>
"""

class CancelError(Exception): pass

def main():
    user_information = dict(name=None, year=None, filename=None, title=None, description=None, stylesheet=None, keywords=None)

    while True:
        try:
            print('\nVyvoreni ramce souboru HTML\n')
            populate_info(user_information)
            create_html(**user_information)

        except CancelError:
            print("Zruseno")

        if (get_info_value("Vytvorit dalsi html soubor? (a / n)", default='ano').lower()) not in ('a', 'ano'):
            break

def populate_info(information):
    name = get_info_value("Zadejte jmeno", field='jmeno')
    if not name:
        raise CancelError()

    year = get_integer("Zadejte rok pro copyright")
  
    filename = get_info_value("Zadejte nazev souboru", field="nazev souboru")
    if not filename:
        raise CancelError()
    
    if not filename.endswith(('.html', '.htm')):
        filename += ".html"

    title = get_info_value("Zadej titulek", field = "titulek")
    if not title:
        raise CancelError()

    description = get_info_value("Zadej popis (volitelne)", field="titulka", optional=True)

    stylesheet = get_info_value("Zadejte nazev souboru s sablonou stylu (volitelne)", field="sablona stylu", optional=True)
   
    if stylesheet and not stylesheet.endswith(".css"):
        stylesheet += ".css"

    keywords = []
    while True:
        keyword = get_info_value("Zadejte klicove slovo (volitelne)", field="klicove slovo", optional=True)
        if keyword:
            keywords.append(keyword)
        else:
            break

    information.update(name=name, year=year, filename=filename, title=title, description=description, stylesheet=stylesheet, keywords=keywords)

def get_info_value(message, field="string", default=None, mininum_length=0, maximum_length=80, optional=False):
    
    message += ": " if default is None else " [{0}]: ".format(default)

    while True:
        try:
            user_input = input(message)
            if not user_input:
                if default is not None:
                    return default
                if optional is True:
                    return ""
                else:
                    raise ValueError("{0} cannot be empty".format(field))

            if not (mininum_length <= len(user_input) <= maximum_length):
                raise ValueError("{field} musi mit nejmene "
                "{minimum_length} a nejvice "
                "{maximum_length} znaku".format(**locals()))
            
            return user_input

        except ValueError as err:
            print("Chyba!", err)

def get_integer(message, field="rok", default=datetime.date.today().year, minimum_year=1900, maximum_year=datetime.date.today().year + 1):
    
    message += " [{0}]: ".format(default)

    while True:
        try:
            user_input = input(message)
            if not user_input and default is not None:
                    return default
            i = int(user_input)

            if not (minimum_year <= i <= maximum_year):
                raise KeyError("{field} musi mit nejmene "
                "{minimum_year} a nejvice "
                "{maximum_year}".format(**locals()))
            
            return i

        except KeyError as err:
            print("Error!", err)
        
        except ValueError:
            print("Chyba! {0} musi byt integer".format(field))

def create_html(year, name, title, description, keywords, stylesheet, filename):
    copyright = COPYRIGHT_TEMPLATE.format(year, xml.sax.saxutils.escape(name))
    title = xml.sax.saxutils.escape(title)
    description = xml.sax.saxutils.escape(description)
    keywords = ",".join(item for item in keywords) if keywords else ""
    stylesheet = STYLESHEET_TEMPLATE.format(stylesheet) if stylesheet else ""
    html = HTML_TEMPLATE.format(**locals())

    fh = None
    try:
        fh = open(filename, 'w', encoding='utf8')
        fh.write(html)

    except EnvironmentError:
        print("ERROR")

    else: 
        print("Ulozen ramec", filename)

    finally:
        if fh is not None:
            fh.close()

main()