def replace_string(retezec, pozice, znak):
    """Zameni znak na dane pozici
    vrati retezec, ktery ma na dane pozici znak;
    jinak je  stejny jako vstupni retezec
    """

    return retezec[:pozice] + znak + retezec[pozice + 1:]

