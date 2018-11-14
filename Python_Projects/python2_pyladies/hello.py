bohata = input("Jsi bohata?") == "ano"
stastna = input("Jsi stastna?") == "ano"

if bohata and stastna:
    print("gratuluji, bohata a strastna")

elif bohata and not stastna:
    print("jen bohata")  

elif stastna and not bohata:
    print("jen stastna")  

else:
    print("smutna a chuda")