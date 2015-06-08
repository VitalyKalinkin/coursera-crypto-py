import binascii
from builtins import zip, bytearray
from Crypto.Cipher import AES


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

def programming_assignment():
    pa_question1()
    pa_question2()

def pa_question1():
    print("Question 1:")

    ct_str = '4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee' \
             '2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81'

    key = '140b41b22a29beb4061bda66b6747e14'

    decode(key, ct_str)

def pa_question2():
    print("Question 2:")

    ct_str = '5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48' \
             'e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253'

    key = '140b41b22a29beb4061bda66b6747e14'

    decode(key, ct_str)

def decode(key, ct_str):
    iv = binascii.a2b_hex(ct_str[:32])
    ct = binascii.a2b_hex(ct_str[32:])
    pt = bytes()
    
    for i in range(len(ct) // 16):
        cipher = AES.new(binascii.a2b_hex(key), AES.MODE_CBC, iv)
        ct_block = ct[i * 16 : (i + 1) * 16]
        pt += cipher.decrypt(ct_block)
        iv = ct_block

    print("Message padded with %d bytes" % pt[-1])
    pt_wo_padding = pt[:-pt[-1]]
    print("Decoded message: '%s'" % pt_wo_padding.decode("ascii"))

