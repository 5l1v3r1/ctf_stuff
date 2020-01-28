file = '/home/alien/Downloads/467b947ad54849203b6796daabebe9f6.brd'

data = open(file, 'rb').read()

sost = 4  # size of size type
result = 0


def to_int(num, endian='little'):
    return int.from_bytes(num, byteorder=endian, signed=True)


count = to_int(data[0:2])
data = data[2:]

for i in range(count):
    a, b, c = data[0:sost], data[sost: 2 * sost], data[sost * 2: sost * 3]
    a, b, c = to_int(a), to_int(b), to_int(c)

    type_balka = data[sost * 3]
    name_size = data[sost * 3 + 1]

    data = data[sost * 3 + 2 + name_size:]

    print(a, b, c, type_balka)

    if type_balka == 1:
        result += c

print(result)
