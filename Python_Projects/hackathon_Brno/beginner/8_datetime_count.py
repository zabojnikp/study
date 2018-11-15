from datetime import date
date01 = date(2017,1,1)
date02 = date(2017,3,4)
diff = abs(date02 - date01)
print(diff.days)