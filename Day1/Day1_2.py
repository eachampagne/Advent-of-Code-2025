import math

#f = open("sample.txt")
#f = open("r1000_sample.txt")
#f = open("extra_sample.txt")
f = open("input.txt")

dial = 50
dial_size = 100
zero_count = 0
#just in case I was misunderstanding the directions, I included a count that increments at most per step
once_per_rotation_count = 0
#sanity check that part 1 still works
zero_at_end_count = 0

for i in f:
    i = i.strip()
    direction = i[0]
    distance = int(i[1:])

    #WHY did moving this here fix it
    #figured it out. I needed to adjust distance by next_rotation, not dial or dist
    #so I was double counting in some edge cases - I think specifically when I was starting
    #at zero and doing more than a full turn
    #moving this logic out here meant I reduced my distances to < 100 before I hit the bug
    zero_count += math.floor(distance / dial_size)
    distance = distance % 100

    increment = False

    if direction == "L":
        next_rotation = 100 if dial == 0 else dial
        if (distance < next_rotation):
            dial = dial - distance
            dial = dial % dial_size
        else: 
            distance -= next_rotation #dial
            dial = 0
            zero_count += 1 + math.floor(distance / dial_size)
            dial = -distance % dial_size
            increment = True
    else:
        diff = dial_size - dial
        next_rotation = 100 if diff == 0 else diff
        if (distance < diff):
            dial = dial + distance
            dial = dial % dial_size
        else:
            distance -= next_rotation #diff
            dial = 0
            zero_count += 1 + math.floor(distance / dial_size)
            dial = distance % dial_size
            increment = True
    if dial == 0:
        zero_at_end_count += 1

    if increment:
        once_per_rotation_count += 1

    #print(i + "\t" + str(dial) + "\t" + str(zero_count))

print(zero_count)
#print(once_per_rotation_count)
#print(zero_at_end_count)
