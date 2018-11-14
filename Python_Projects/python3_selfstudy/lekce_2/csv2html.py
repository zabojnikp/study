import sys
import xml.sax.saxutils


def main():
    maxwidth = 100
    print_start()
    count = 0
    while True:
        try:
            line = input()
            if count == 0:
                color = "lightgreen"
            elif count % 2:
                color = "white"
            else:
                color = "lightyellow"
            print_line(line, color, maxwidth)
            count += 1
        except EOFError:
            break
    print_end()


def print_start():
    print("<table border='1'>")


def print_line(line, color, maxwidth):
    print("<tr bgcolor='{0}'>".format(color))
    fields = extract_fields(line)
    for field in fields:
        if not field:
            print("<td></td>")
        else:
            number = field.replace(",", "")
            try:
                x = float(number)
                print("<td align='right'>{0:d}</td>".format(round(x)))
            except ValueError:
                field = field.title()
                field = field.replace(" A ", " a ")
                if len(field) <= maxwidth:
                    field = xml.sax.saxutils.escape(field)
                else:
                    field = "{0} ...".format(
                            xml.sax.saxutils.escape(field)(field[:maxwidth]))
                print("<td>{0}</td>".format(field))
    print("</tr>")


def extract_fields(line):
    fields = []
    field = ""
    quote = None
    for c in line:
        if c in "\"'":
            if quote is None: # začátek řetězce uzavřeného do uvozovek
                quote = c
            elif quote == c:  # konec řetězce uzavřeného do uvozovek
                quote = None
            else:
                field += c    # další uvozovku uvnitř řetězce v uvozovkách
            continue
        if quote is None and c == ",": # konec pole
            fields.append(field)
            field = ""
        else:
            field += c        # akumulace pole
    if field:
        fields.append(field)  # přidání posledního pole
    return fields

def process_options():
    

def print_end():
    print("</table>")


main()
