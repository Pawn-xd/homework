import binascii

def gcd(a, b):#欧几里得算法
    if b == 0:
        return a
    return gcd(b, a % b)
def Ex_Euclid(a,b): #扩展欧几里得算法
  if 0==b:
    x=1;y=0;q=a
    return x,y,q
  xyq=Ex_Euclid(b,a%b)
  x=xyq[0];y=xyq[1];q=xyq[2]
  temp=x;x=y;y=temp-a//b*y
  return x,y,q
def Get_Inverse(a,b): #求模逆
  return Ex_Euclid(a,b)[0]

# p-1 分解
def p_1(n, e, c, b):
    k = 1
    for i in range(b):
        k *= i + 1
    p = gcd(pow(2, k, n) - 1, n)
    if p == 1 or p == n:
        return 0
    q = n // p
    if p * q != n:
        return 0
    phi = (p - 1) * (q - 1)
    d = Get_Inverse(e, phi)
    if d<0:
        d = - d
        c = Get_Inverse(c, n)
    return pow(c, d, n)

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

    for i in range(1, 21):
        temp = p_1(ns[i], es[i], cs[i], 11111)
        if temp > 0:
            print(i, ":", binascii.a2b_hex(hex(temp)[2:]))
