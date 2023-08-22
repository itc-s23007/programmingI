mountain_in_japan = {'fuji': 3376, 'kitadake': 3193, 'okuhodakadake': 3190, 'dummy': 0}
mauntain_in_japan_sorted = sorted(mountain_in_japan.items(), key=lambda x: x[1],
 revarse=True)
print(mountain_in_japan_sorted)

