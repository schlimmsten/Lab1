#print("Количество книг, помещающихся на дискету:", ...)
file_size = 1.44 * 1024 ** 2 #размерность дискеты в байтах
book_pages = 100
string_on_page = 50
string_symbols = 25
symbol_size = 4
result = file_size // (book_pages * string_on_page * string_symbols * symbol_size)
print("Количество книг, помещающихся на дискету:", int(result))

