# TODO Найдите количество книг, которое можно разместить на дискете
obuem = 1.44
numder = 100
kolichestvo = 50
sumbols = 25
obuem_2 = 1.44 * 1024 * 1024
one_symbol = 4
obshi_obuem = numder * kolichestvo * sumbols * one_symbol
kol_knig = obuem_2 //  obshi_obuem
print("Количество книг, помещающихся на дискету:", int(kol_knig))
