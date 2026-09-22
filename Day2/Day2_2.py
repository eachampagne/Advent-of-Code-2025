#f = open("sample.txt")
f = open("input.txt")

def clone_string(string, times):
    new_string = ""
    for i in range(times):
        new_string += string
    return new_string

def is_invalid(id):
    string = str(id)
    string_length = len(string)

    for chunk_length in range(1, string_length): # don't include string_length or every string will be itself x1
        if string_length % chunk_length == 0:
            base = string[:chunk_length]
            repetitions = string_length // chunk_length   
            if string == clone_string(base, repetitions):
                return True
    
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
