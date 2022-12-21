def abc_delete(massage):
    find_txt = 'абв'
    lst = [i for i in massage.split() if find_txt not in i]
    return " ".join(lst)