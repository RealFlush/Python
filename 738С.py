def read_int():
    return map(int, input().split())
n, k, s, t = read_int()
cars = []
for i in range(n):
    cars.append(read_int())

stations = list(read_int())
stations.sort()

distances = []
prev = 0
for station in stations:
    distances.append(station - prev)
    prev = station

distances.append(s - prev)

# поиск мин. объема
beyond_max = max(distances) * 2 + 1

min_v = 0
max_v = beyond_max
while min_v < max_v:
    v = (min_v + max_v) // 2

    can_reach = True
    min_time = 0
    for distance in distances:
        if distance > v:
            can_reach = False
            break

        if v >= distance*2:
            tm = distance
        else:
            tm = distance*2 - (v-distance)
        min_time += tm

        if min_time > t:
            can_reach = False
            break

    if can_reach:
        max_v = v
    else:
        min_v = v + 1

min_price = -1
if min_v < beyond_max:
    for c, v in cars:
        if v >= min_v:
            if min_price == -1 or min_price > c:
                min_price = c

print(min_price)
