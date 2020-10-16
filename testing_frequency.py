
original = {"v":"t", "g":"a","h":"o","z":"r","r":"s","m":"i","i":"h","f":"d","x":"l","l":"f","d":"c",\
              "k":"m","s":"u","w":"g","o":"y","t":"p","b":"w","e":"b", "u":"v","n":"k","y":"x","p":"j"}


subs_table = {"v":"e", "g":"t","h":"s","z":"a","r":"i","m":"n","i":"r","f":"u","x":"c","l":"o","d":"w",\
              "k":"p","s":"h","w":"d","o":"l","t":"g","b":"y","e":"v", "u":"f","n":"m","y":"b","p":"k"}

def frequency(s):
    size = 0
    for let in s:
        if let.lower().isalpha():
            size+=1
    print(size)
    d= dict()
    d1 = dict()
    for i in s:
        if i.lower() in d.keys() :
            d[i.lower()]+=1
        elif i.isalpha():
            d[i.lower()]=1

    for k in d.keys():
        perc = round(d[k]/size*100,4)
        d1[k] = perc
    print(len(d))
    d1 = {k : v for k, v in sorted(d1.items(), key=lambda item : item[1])}

    for j in d1.keys():
        print("The letter: {}, occurrence: {}".format(j,d1[j]))


def change_text(s):
    res = ""
    for letter in s:
        if letter.isalpha():
            res+=subs_table[letter]
        else:
            res+=letter
    return res


if __name__ == "__main__":
    frequency("Vevib ztv, vevib xfogfiv, vevib xfhgln zmw gizwrgrlm szh rgh ldm xszizxgvi, rgh ldm dvzpmvhh\
                zmw rgh ldm hgivmtgs, rgh yvzfgrvh zmw ftormvhh; zxxvkgh xvigzrm hfuuvirmth zh nzggvih lu\
                xlfihv, kfgh fk kzgrvmgob drgs xvigzrm veroh.")
    res = change_text("vevib ztv, vevib xfogfiv, vevib xfhgln zmw gizwrgrlm szh rgh ldm xszizxgvi, rgh ldm dvzpmvhh\
                zmw rgh ldm hgivmtgs, rgh yvzfgrvh zmw ftormvhh; zxxvkgh xvigzrm hfuuvirmth zh nzggvih lu\
                xlfihv, kfgh fk kzgrvmgob drgs xvigzrm veroh.")
    print(res)