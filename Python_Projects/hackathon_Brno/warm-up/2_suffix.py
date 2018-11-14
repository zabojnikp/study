    
user_input = input("Zadej jmeno souboru:")
file = user_input.rpartition(".") 
print("Output", file[2])
