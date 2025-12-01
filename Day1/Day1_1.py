#f = open("sample.txt")
f = open("input.txt")

dial = 50
dial_size = 100
zero_count = 0

for i in f:
    i = i.strip()
    direction = i[0]
    distance = int(i[1:])
    
    dial = (dial - distance) % dial_size if direction == "L" else (dial + distance) % dial_size
    if dial == 0:
        zero_count += 1

print(zero_count)
