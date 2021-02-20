import re
from PyQt5.QtGui import QColor

def RGBAstr_to_RGBAtuple(s):
    if not isinstance(s, str):
        raise TypeError(f'Invalid argument type {type(s)}, expected string')

    pattern = '^\s*rgba?\s*\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*(?:,\s*(\d+)\s*)?\)\s*$'
    search = re.search(pattern, s)

    if search == None or len(search.groups()) < 3:
        raise ValueError('Invalid RGBA string')

    tup = (
        int(search.group(1)),
        int(search.group(2)),
        int(search.group(3)),
        int(search.group(4)) if search.group(4) != None else 255
    )

    return tup

def RGBAtuple_to_RGBAstr(tup):
    if not isinstance(tup, tuple):
        raise TypeError(f'Invalid argument type {type(tup)}, expected tuple')

    if len(tup) < 3:
        raise ValueError('Missing RGBA values in tuple, expected at least 3')

    s = 'rgba('

    s += str(tup[0]) + ', '
    s += str(tup[1]) + ', '
    s += str(tup[2]) + ', '
    s += str(tup[3]) if len(tup) > 3 else '255'

    s += ')'

    return s

def RGBAint_to_RGBAtuple(i):
    if not isinstance(i, int):
        raise TypeError(f'Invalid argument type {type(i)}, expected int')

    if i < 0 or i > (2 ** 32) - 1:
        raise ValueError('Invalid integer argument, expected unsigned 32 bit integer')

    b = i & 255
    g = (i >> 8) & 255
    r = (i >> 16) & 255
    a = (i >> 24) & 255

    tup = (r, g, b, a)

    return tup

def RGBAtuple_to_RGBAint(tup):
    if not isinstance(tup, tuple):
        raise TypeError(f'Invalid argument type {type(tup)}, expected tuple')

    if len(tup) < 3:
        raise ValueError('Missing RGBA values in tuple, expected at least 3')

    b = tup[2]
    g = tup[1] << 8
    r = tup[0] << 16
    a = tup[3] << 24 if len(tup) > 3 else 255 << 24

    i = a + r + g + b

    return i

def RGBAQColor_to_RGBAtuple(qcolor):
    if not isinstance(qcolor, QColor):
        raise TypeError(f'Invalid argument type {type(qcolor)}, expected QColor')

    r = qcolor.red()
    g = qcolor.green()
    b = qcolor.blue()
    a = qcolor.alpha()

    tup = (r, g, b, a)

    return tup

def RGBAtuple_to_RGBAQColor(tup):
    if not isinstance(tup, tuple):
        raise TypeError(f'Invalid argument type {type(tup)}, expected tuple')

    if len(tup) < 3:
        raise ValueError('Missing RGBA values in tuple, expected at least 3')

    qcolor = QColor(*tup)

    return qcolor

def to_RGBAtuple(color):
    if isinstance(color, tuple):
        if len(color) < 3:
            raise ValueError('Missing RGBA values in tuple, expected at least 3')
        elif len(color) == 3:
            return color + (255,)
        else:
            return color[:4]
        return color
    elif isinstance(color, str):
        return RGBAstr_to_RGBAtuple(color)
    elif isinstance(color, int):
        return RGBAint_to_RGBAtuple(color)
    elif isinstance(color, QColor):
        return RGBAQColor_to_RGBAtuple(color)
    else:
        raise TypeError(f'Invalid argument type {type(color)}')

if __name__ == '__main__':
    i = 32434243
    t = (23, 23, 43)
    q = QColor(222, 121, 32, 231)
    f = 123.2
    print(to_RGBAtuple(i))
    print(to_RGBAtuple(t))
    print(to_RGBAtuple(q))
    print(to_RGBAtuple(f))