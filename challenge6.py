import random 
random.seed(34)

hole_sizes = [random.randint(1, i) for i in range(1, 101)]
random.shuffle(hole_sizes)

# hole sizes in mm
average_size = 0
total = 0.0
tmp = 0.0
for i in hole_sizes:
    average_size = average_size + i
    if i < 20:
        tmp = 1.3
    elif i < 70:
        tmp = 1.6
    else:
        tmp = 2.1
    total = total + tmp

print(average_size / 100)
print(total / 100)
print(total)
