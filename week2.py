import binascii
from builtins import zip, bytearray
from Crypto.Cipher import AES
from Crypto.Util import Counter

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
    pa_question3()
    pa_question4()

def pa_question1():
    print("Question 1:")

    ct_str = '4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee' \
             '2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81'

    key = '140b41b22a29beb4061bda66b6747e14'

    decode_cbc(key, ct_str)

def pa_question2():
    print("Question 2:")

    ct_str = '5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48' \
             'e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253'

    key = '140b41b22a29beb4061bda66b6747e14'

    decode_cbc(key, ct_str)

def decode_cbc(key, ct_str):
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

def pa_question3():
    print("Question 3:")

    ct_str = '69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc3' \
             '88d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329'

    key = '36f18357be4dbd77f050515c73fcf9f2'

    decode_ctr(key, ct_str)

def pa_question4():
    print("Question 4:")

    ct_str = '770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa' \
             '0e311bde9d4e01726d3184c34451'

    key = '36f18357be4dbd77f050515c73fcf9f2'

    decode_ctr(key, ct_str)

def decode_ctr(key, ct_str):
    counter = Counter.new(128, initial_value=int.from_bytes(binascii.a2b_hex(ct_str[:32]), byteorder="big"))
    ct = binascii.a2b_hex(ct_str[32:])
    pt = bytes()
    
    for i in range((len(ct) + 15) // 16):
        cipher = AES.new(binascii.a2b_hex(key), AES.MODE_CTR, counter=counter)
        pt += cipher.decrypt(ct[i * 16 : (i + 1) * 16])

    print("Decoded message: '%s'" % pt.decode("ascii"))
