Number = int(input('Введите число'+ ' ')) # кол-во раз которые цикл позволит ввести число далее
for i in range(Number): 
    numbermini = int(input('Введите еще число' + ' ')) # те самые разы
    if numbermini == 0: # условие заключается в том, что программа дает ввести N значений и каждый раз просматривает их на наличие 0
        print('YES') # как только программа находит 0 она прерывается и выводит YES 
        break
else:
    print('NO') # это случай когда программа за все N чисел не нашла 0 ей грустно(