def test(a, b, c):
    print("a=%d" % a)
    print("b=%d" % b)
    print("a=%d" % c)

test(11,b=2,c=3)  ###()内有多个参数时，左边为无名字的，右边为有名的且必须无名有名连在一起

#缺省参数也一样，无名的在左边，有名的在右边