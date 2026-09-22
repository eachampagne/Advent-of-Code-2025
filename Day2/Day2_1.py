#f = open("sample.txt")
f = open("input.txt")

def is_invalid(id):
    string = str(id)
    if len(string) % 2 != 0:
        return False
    midpoint = len(string) // 2
    if string[:midpoint] == string[midpoint:]:
        return True
    else:
        return False

for i in f:
    ranges = i.strip().split(',')

sum = 0

for i in ranges:
    [str_min, str_max] = i.split('-')
    int_min = int(str_min)
    int_max = int(str_max)

    for j in range(int_min, int_max + 1):
        if is_invalid(j):
            sum += j
    
print(sum)
