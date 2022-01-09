import gmpy2
import binascii

#中国剩余定理
def chinese_remainder_theorem(items):
    N = 1
    for a, n in items:
        N *= n
        result = 0
    for a, n in items:
        m = N//n
        d, r, s = egcd(n, m)
        if d != 1:
            N = N//n
            continue
        result += a*s*m
    return result % N, N

def low_e_5():
    sessions=[{"c": cs[3],"n": ns[3]},
    {"c":cs[8] ,"n":ns[8]},
    {"c":cs[12],"n":ns[12]},
    {"c":cs[16],"n":ns[16]},
    {"c":cs[20],"n":ns[20]}]
    data = []
    for session in sessions:
        data = data+[(session['c'], session['n'])]
    x, y = chinese_remainder_theorem(data)
    # 直接开五次方根
    plaintext3_8_12_16_20 = gmpy2.iroot(gmpy2.mpz(x),5)
    return binascii.a2b_hex(hex(plaintext3_8_12_16_20[0])[2:])

if __name__ == "__main__":
    ns = []
    cs = []
    es = []
    for i in range(21):
        f=open("./Frame"+str(i), "r")
        s = f.read()
        ns.append(int(s[0:256],16))
        es.append(int(s[256:512],16))
        cs.append(int(s[512:768],16))
        f.close()

plaintext3_8_12_16_20 = low_e_5()
print(plaintext3_8_12_16_20)
