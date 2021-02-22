import random 
random.seed(34)

hole_sizes = [random.randint(1, i) for i in range(1, 101)]
random.shuffle(hole_sizes)

# hole sizes in mm
average_size = 0
total = 0.0
min_size = 100
max_size = 0
for i in hole_sizes:
    average_size = average_size + i
    if min_size > i:
        min_size = i
    if max_size < i:
        max_size = i
    if i < 20:
        total += 1.3
    elif i < 70:
        total += 1.6
    else:
        total += 2.1

print(f'Average hole size is {average_size / 100:.2f}')
print( f'Average hole repair cost is {total / 100:.3f}')
print(f'Total hole repair code is {total:.2f}')
print(f'max hole size is {max_size}')
print(f'min hole size is {min_size}')
