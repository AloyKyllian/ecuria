def suppr_heure(data, heure):
    print(data, heure)
    if heure in data:
        del data[heure]
    return data
