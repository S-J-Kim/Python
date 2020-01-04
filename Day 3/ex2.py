distance_to_road = int(input())
maximum_noise_floor = int(0.2467 * distance_to_road + 4.159)

print(f'The most noisiest floor is {maximum_noise_floor}')
