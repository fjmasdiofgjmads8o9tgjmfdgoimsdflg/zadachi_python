#  Дана строка. Замените в этой строке все цифры 1 на слово one

from random import choice
from string import ascii_letters
from string import digits

a = (''.join(choice(ascii_letters+digits) for i in range(20)))
print('Строка:', a, '\n')

b = a.replace('1', 'one')
print('Строка после замены:', b)
