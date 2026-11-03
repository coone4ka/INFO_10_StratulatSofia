from enum import Enum 
class Anotimp(Enum):
    PRIMAVARA = 1
    VARA = 2
    TOAMNA = 3
    IARNA = 4
a = Anotimp.PRIMAVARA
b = Anotimp.VARA
c = Anotimp.TOAMNA
d = Anotimp.IARNA
print('cod = ', a.value)
print('cod = ', b.value)
print('cod = ', c.value)
print('cod = ', d.value)


