disket = 1.44
pages = 100
raws = 50
symbols = 25
one_symb = 4
symb_in_book = pages * raws * symbols * one_symb
megabite = disket * 1024 * 1024
result = megabite / symb_in_book

print(f"Количество книг, помещающихся на дискету: {result:.0f}")
