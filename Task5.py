number = int(input('Введите число' + ' ')) 
maximum = number # это нужно чтобы прогромамма с самого начала имела предствалнение о максимальном числе (на тот момент)
kaka = 1 # счетчик для подсчета сколько максимальных чисел мы имеем 
while number != 0: # Программа будет запрашивать число до момента пока мы не введем 0 (то есть бесконечно)
    number = int(input('Введите число' + ' ')) # и теперь расматриваем 2 случая  
    if number > maximum: # первый это если нововведенное число больше максимума то мы обнуляем счетчик и начинаем считать заново
        maximum = number
        kaka = 1 
    elif number == maximum: # второй же случай просто продолжает считать и добовляет единицу к самому счетчику 
        kaka += 1 
print(kaka)
