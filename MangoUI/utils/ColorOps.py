import re
from PyQt6.QtGui import QColor


def RGBAstr_to_RGBAtuple(s):
    if not isinstance(s, str):
        raise TypeError(f'Invalid argument type {type(s)}, expected string')

    pattern = (
        r'^\s*rgba?\s*\(\s*(\d+)\s*,'
        r'\s*(\d+)\s*,\s*(\d+)\s*(?:,\s*(\d+)\s*)?\)\s*$'
    )
    search = re.search(pattern, s)

    if search is None or len(search.groups()) < 3:
        raise ValueError(f'Invalid RGBA string, {s}')

    tup = (
        int(search.group(1)),
        int(search.group(2)),
        int(search.group(3)),
        int(search.group(4)) if search.group(4) is not None else 255,
    )

    return tup


def RGBAtuple_to_RGBAstr(tup):
    if not isinstance(tup, tuple):
        raise TypeError(f'Invalid argument type {type(tup)}, expected tuple')

    if len(tup) < 3:
        raise ValueError(
            f'Missing RGBA values in tuple, {tup}, expected at least 3'
        )

    s = 'rgba('

    s += str(tup[0]) + ', '
    s += str(tup[1]) + ', '
    s += str(tup[2]) + ', '
    s += str(tup[3]) if len(tup) > 3 else '255'

    s += ')'

    return s


def HEXstr_to_RGBAtuple(s):
    if not isinstance(s, str):
        raise TypeError(f'Invalid argument type {type(s)}, expected string')

    pattern = r'^#?([0-9a-fA-F]{6,8})\S*$'
    search = re.search(pattern, s.replace(' ', ''))

    if search is None or len(search.groups()) < 1:
        raise ValueError(f'Invalid HEX string, {s}')

    tup = (
        int(search.group(1)[2:4], 16),
        int(search.group(1)[4:6], 16),
    )

    if len(search.group(1)) < 8:
        tup = (int(search.group(1)[0:2], 16),) + tup + (255,)
    else:
        tup += (
            int(search.group(1)[6:8], 16),
            int(search.group(1)[0:2], 16),
        )

    return tup


def RGBAtuple_to_HEXstr(tup):
    if not isinstance(tup, tuple):
        raise TypeError(f'Invalid argument type {type(tup)}, expected tuple')

    if len(tup) < 3:
        raise ValueError(
            f'Missing RGBA values in tuple, {tup}, expected at least 3'
        )

    s = str(format(tup[0], 'x').upper())
    s += str(format(tup[1], 'x').upper())
    s += str(format(tup[2], 'x').upper())
    s = str(format(tup[3], 'x').upper() if len(tup) > 3 else 'FF') + s

    s = '#' + s

    return s


def RGBAint_to_RGBAtuple(i):
    if not isinstance(i, int):
        raise TypeError(f'Invalid argument type {type(i)}, expected int')

    if i < 0 or i > (2**32) - 1:
        raise ValueError(
            f'Invalid integer argument, {i}, expected unsigned 32 bit integer'
        )

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
        raise ValueError(
            f'Missing RGBA values in tuple, {tup}, expected at least 3'
        )

    b = tup[2]
    g = tup[1] << 8
    r = tup[0] << 16
    a = tup[3] << 24 if len(tup) > 3 else 255 << 24

    i = a + r + g + b

    return i


def RGBAQColor_to_RGBAtuple(qcolor):
    if not isinstance(qcolor, QColor):
        raise TypeError(
            f'Invalid argument type {type(qcolor)}, expected QColor'
        )

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
        raise ValueError(
            f'Missing RGBA values in tuple, {tup}, expected at least 3'
        )

    qcolor = QColor(*tup)

    return qcolor


def to_RGBAtuple(color):
    if isinstance(color, tuple):
        if len(color) < 3:
            raise ValueError(
                f'Missing RGBA values in tuple, {color}, expected at least 3'
            )
        elif len(color) == 3:
            return color + (255,)
        else:
            return color[:4]
    elif isinstance(color, str):
        try:
            return RGBAstr_to_RGBAtuple(color)
        except ValueError:
            try:
                return HEXstr_to_RGBAtuple(color)
            except ValueError:
                raise ValueError(f'Invalid string, {color}')
    elif isinstance(color, int):
        return RGBAint_to_RGBAtuple(color)
    elif isinstance(color, QColor):
        return RGBAQColor_to_RGBAtuple(color)
    else:
        raise TypeError(f'Invalid argument type {type(color)}')
