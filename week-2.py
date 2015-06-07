import binascii
from builtins import zip, bytearray


def question4(out64, out32and32):
    out64bytes = binascii.a2b_hex(out64)
    out32and32bytes = binascii.a2b_hex(out32and32)

    b = bytearray(x ^ y for (x, y) in zip(out64bytes, out32and32bytes))

    return binascii.b2a_hex(b)

def question4_solve():
    print(question4("7c2822ebfdc48bfb", "325032a9c5e2364b"))
    print(question4("290b6e3a39155d6f", "d6f491c5b645c008"))
    print(question4("4af532671351e2e1", "87a40cfa8dd39154"))
    print(question4("5f67abaf5210722b", "bbe033c00bc9330e"))

question4_solve()
