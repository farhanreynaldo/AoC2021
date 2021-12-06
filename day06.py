SAMPLES = """3,4,3,1,2"""


def fish_count(input, days):
    initial_state = [int(num) for num in input.split(",")]
    fish_frequency = [initial_state.count(num) for num in range(9)]
    for _ in range(days):
        # pull the first index (0 days left)
        birth = fish_frequency.pop(0)
        # reset the 0 days to 6 days
        fish_frequency[6] += birth
        # add the 8 days based on number of births
        fish_frequency.append(birth)
    return sum(fish_frequency)


assert fish_count(SAMPLES, 18) == 26
assert fish_count(SAMPLES, 80) == 5934
input = open("input/day06.txt").read()
print(fish_count(input, 80))
print(fish_count(input, 256))
