def rshift(val, n):
    return val >> n if val >= 0 else (val + 0x100000000) >> n


def _b(a, b):
    for i in range(0, len(b) - 2, 3):
        c = b[i + 2]
        c = ord(c[0]) - 87 if "a" <= c else int(c)
        c = rshift(a, c) if "+" == b[i + 1] else a << c
        a = a + c & 4294967295 if "+" == b[i] else a ^ c
    return a


def tk(a, tkk="422388.3876711001"):
    e = tkk.split(".")
    h = int(e[0]) or 0
    g, d = {}, 0
    for i in range(len(a)):
        c = ord(a[i])
        if 128 > c:
            g[d] = c
            d += 1
        else:
            if 2048 > c:
                g[d] = c >> 6 | 192
                d += 1
            else:
                if 55296 == (c & 64512) and i + 1 < len(a) and 56320 == (a[i + 1] & 64512):
                    i += 1
                    c = 65536 + ((c & 1023) << 10) + (a[i] & 1023)
                    g[d] = c >> 18 | 240
                    d += 1
                    g[d] = c >> 12 & 63 | 128
                    d += 1
                else:
                    g[d] = c >> 12 | 224
                    d += 1
                    g[d] = c >> 6 & 63 | 128
                    d += 1
            g[d] = c & 63 | 128
            d += 1
    a = h
    for d in range(len(g)):
        a += g[d]
        a = _b(a, "+-a^+6")
    a = _b(a, "+-3^+b+-f")
    a ^= int(e[1]) or 0
    if 0 > a:
        a = (a & 2147483647) + 2147483648
    a %= 1e6
    return "%s.%s" % (int(a), int(a) ^ h)
