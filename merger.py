first = input("first filename, e.g usa.txt:  ")
second = input("second filename; will be coinjoined to second file e.g usa_phones.txt:  ")
third = input("third filename,where both conjoined files will be stored e.g usa_full.txt:  ")

combine = []

with open(second, encoding= 'utf-8') as xh:
    with open(first, encoding= 'utf-8') as yh:
        with open(third,mode = "w",encoding='utf-8') as zh:
            xlines = xh.readlines()
            ylines = yh.readlines()

for i in range(len(xlines)):
   line = ylines[i].strip() + ' ' + xlines[i]
   with open(third, mode = "a",encoding = 'utf-8' ) as zh:
       zh.write(line)









