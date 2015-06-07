import binascii
from builtins import zip, bytearray


def question4(out64, out32and32):
    out64bytes = binascii.a2b_hex(out64)
    out32and32bytes = binascii.a2b_hex(out32and32)

    b = bytearray(x ^ y for (x, y) in zip(out64bytes, out32and32bytes))

    return binascii.b2a_hex(b)

def question4_solve():
    print(question4("e86d2de2e1387ae9", "1792d21db645c008"))
    print(question4("7c2822ebfdc48bfb", "325032a9c5e2364b"))
    print(question4("9d1a4f78cb28d863", "75e5e3ea773ec3e6"))
    print(question4("7b50baab07640c3d", "ac343a22cea46d60"))

