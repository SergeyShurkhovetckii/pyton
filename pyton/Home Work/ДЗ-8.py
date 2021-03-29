a = 'AB' * 52
print(a)

while 'AA' in a or 'BB' in a or 'AB' in a :
    if 'AA' in a :
        a=a.replace('AA', 'B',1)
    if 'BB' in a :
        a=a.replace('BB', 'A',1)
    if 'AB' in a :
        a=a.replace('AB','BA',1)

print(a)