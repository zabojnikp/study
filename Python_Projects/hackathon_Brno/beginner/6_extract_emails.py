import string
import re

my_string = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris vulputate lacus id eros consequat \
tempus. Nam viverra velit sit amet lorem lobortis, at tincidunt nunc ultricies. Duis facilisis ultrices lacus, id \
tiger123@email.cz auctor massa molestie at. Nunc tristique fringilla congue. Donec ante diam cnn@info.com, dapibus \
lacinia vulputate vitae, ullamcorper in justo. Maecenas massa purus, ultricies a dictum ut, dapibus vitae massa. \
Cras abc@gmail.com vel libero felis. In augue elit, porttitor nec molestie quis, auctor a quam. Quisque b2b@money.fr \
pretium dolor et tempor feugiat. Morbi libero lectus, porttitor eu mi sed, luctus lacinia risus. Maecenas posuere leo 
sit amet spam@info.cz. elit tincidunt maximus. Aliquam erat volutpat. Donec eleifend felis at leo ullamcorper cursus. 
Pellentesque id dui viverra, auctor enim ut, fringilla est. Maecenas gravida turpis nec ultrices aliquet.'''

emails = dict()
email_domains = []
all_emails = []
emails_with_num = []

def hasNumbers(inputString):
    return bool(re.search(r'\d', inputString))

words_list = my_string.split()
for word in words_list:
    if "@" in word:
        all_emails.append(word)
        email_domains.append((word.rpartition('@'))[2])
        if hasNumbers(word):
           emails_with_num.append(word)

emails['all_emails'] = all_emails    
emails['domain'] = email_domains
emails['emails_with_num'] = emails_with_num

print(emails)