import re

def RGBAstr_to_RGBAtuple(s):
    pattern = "^\s*rgba?\s*\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*(?:,\s*(\d+)\s*)?\)\s*$"
    search = re.search(pattern, s)

    tup = (
        int(search.group(1)),
        int(search.group(2)),
        int(search.group(3)),
        int(search.group(4)) if search.group(4) != None else 255
    )

    return tup

def RGBAtuple_to_RGBAstr(tup):
    s = "rgba("

    s += str(tup[0]) + ", "
    s += str(tup[1]) + ", "
    s += str(tup[2]) + ", "
    s += str(tup[3]) if len(tup) > 3 else "255"

    s += ")"

    return s

def RGBAint_to_RGBAtuple(i):
    b = i & 255
    g = (i >> 8) & 255
    r = (i >> 16) & 255
    a = (i >> 24) & 255

    return (r, g, b, a)