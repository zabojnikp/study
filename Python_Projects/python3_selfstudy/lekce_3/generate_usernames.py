import collections
import sys

ID, FORENAME, MIDDLENAME, SURNAME, DEPARTMENT = range(5)

User = collections.namedtuple('User', "username id forename middlename surname department")

def main():
    if len(sys.argv) == 1 or sys.argv[1] in ('-- help', '-h'):
        print("Usage: {} <filename>".format(sys.argv[0]))
        sys.exit()
    
    users = {}
    usernames = set()

    for filename in sys.argv[1:]:
        for line in open(filename, encoding='utf8'):
            line = line.rstrip()
            if line:
                fields = line.split(":")
                username = generate_username(fields, usernames)
                user = User(username, fields[ID], fields[FORENAME], fields[MIDDLENAME], fields[SURNAME], fields[DEPARTMENT])
                users[(user.surname.lower(), user.forename.lower(), user.id)] = user
    print_users(users)

def generate_username(fields, usernames):
    username = ((fields[FORENAME][0] + fields[MIDDLENAME][:1] + fields[SURNAME]).replace('-', ""))
    username = original_username = username[:8].lower()
    count = 1
    while username in usernames:
        username = "{0}{1}".format(original_username, count)
        count += 1
    usernames.add(username)
    return username

def print_users(users):
    namewidth = 32
    usernamewidth = 9

    print("{0:<{nw}} {1:^6} {2:{uw}}".format("Name", "ID", "Username", nw=namewidth, uw=usernamewidth))
    print("{0:-<{nw}} {0:-<6} {0:-<{uw}}".format("", nw=namewidth, uw=usernamewidth))

    for user_name in sorted(users):
        user = users[user_name]

        print("{0.surname},{0.forename} {0.middlename:.<18} ({0.id:<}) {0.username}".format(user, nw=namewidth, uw=usernamewidth))

main()