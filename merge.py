import convertmodules as zhmk
def hb():
    a = zhmk.zh("export/ip.txt")
    b = zhmk.zh("export/port.txt")
    d = open("export/combo.txt","w")
    i = 0
    print("开始合并IP与Port")
    try:
        while True:
            c = a[i]+":"+b[i]+"\n"
            i += 1
            d.write(c)
    except Exception as e:
        pass