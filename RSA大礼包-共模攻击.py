import binascii


# 欧几里得算法
def Ex_Euclid(a,b):
  if 0==b:
    x=1;y=0;q=a
    return x,y,q
  xyq=Ex_Euclid(b,a%b)
  x=xyq[0];y=xyq[1];q=xyq[2]
  temp=x;x=y;y=temp-a//b*y
  return x,y,q
def Get_Inverse(a,b):
  return Ex_Euclid(a,b)[0]

# 公共模数攻击
def same_modulus_attack():
    # 寻找公共模数
    for i in range(21):
        for j in range(i+1, 21):
            if ns[i] == ns[j]:
                print(str(i)+' and '+str(j))
                e1 = es[i]
                e2 = es[j]
                n = ns[i]
                c1 = cs[i]
                c2 = cs[j]
                s1,s2,p= Ex_Euclid(e1, e2)
    # 求模反元素
    if s1<0:
        s1 = - s1
        c1 = Get_Inverse(c1, n)
    elif s2<0:
        s2 = - s2
        c2 = Get_Inverse(c2, n)

    m = pow(c1,s1,n)*pow(c2,s2,n) % n
    result = binascii.a2b_hex(hex(m)[2:])
    return result


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
    # 使用公共模数攻击的方法还原出Frame0和Frame4
    # Frame0: My secre
    # Frame4: My secre
    m0_and_4 = same_modulus_attack()
    print(m0_and_4)
