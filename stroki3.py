#  Дана строка. Если в этой строке буква f встречается только один раз, выведите её индекс. Если она встречается два и более раз, выведите индекс её первого и последнего появления. Если буква f в данной строке не встречается, вывести -1.

from random import choice
from string import ascii_letters
from string import digits

a = (''.join(choice(ascii_letters + digits) for i in range(20)))
print('Строка:', a, '\n')

if a.count('f', 0) == 1:
    print('Номер элемента:', a.find('f', 0))
if a.count('f', 0) >= 2:
    print('Первый элемент:', a.find('f', 0), '\nПоследний элекмент:', a.rfind('f', 0))
if a.count('f', 0) == 0:
    print('-1')
