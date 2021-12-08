import decimal
from statistics import mean, median

SAMPLES = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
"""


def count_1478(input):
    lines = [line.split(" | ")[1] for line in input.strip().split("\n")]
    digits = [len(digit) for line in lines for digit in line.split()]
    return sum(digit in (2, 4, 3, 7) for digit in digits)


assert count_1478(SAMPLES) == 26
input = open("input/day08.txt").read()
print(count_1478(input))


def find_three(one, five_letters):
    """yang 5 huruf itu 2, 3, dan 5. Kalau ada sequence di intersect dengan 1,
    dan sisanya 3, berarti itu angka 3"""
    for signal in five_letters:
        if len(set(signal) - set(one)) == 3:
            return signal


def find_nine(four, six_letters):
    """yang 6 huruf itu 0, 6, dan 9. Kalau ada sequence di intersect dengan 4,
    dan sisanya 2, berarti itu angka 9"""
    for signal in six_letters:
        if len(set(signal) - set(four)) == 2:
            return signal


def find_five(nine, five_letters):
    """9 dengan 2 dan 5 dicek, kalau sisa 0 berarti angka 5"""
    for signal in five_letters:
        if len(set(signal) - set(nine)) == 0:
            return signal


def find_six(five, six_letters):
    """5 dengan 0 dan 6 dicek, kalau sisa 1 berarti angka 6"""
    for signal in six_letters:
        if len(set(signal) - set(five)) == 1:
            return signal


def decode_signals(digits):
    signals = {}
    for signal in digits.split():
        if len(signal) == 2:
            signals[1] = signal
        elif len(signal) == 3:
            signals[7] = signal
        elif len(signal) == 4:
            signals[4] = signal
        elif len(signal) == 7:
            signals[8] = signal

    five_letters = [signal for signal in digits.split() if len(signal) == 5]
    six_letters = [signal for signal in digits.split() if len(signal) == 6]
    signals[3] = find_three(signals[1], five_letters)
    five_letters.remove(signals[3])
    signals[9] = find_nine(signals[4], six_letters)
    six_letters.remove(signals[9])
    signals[5] = find_five(signals[9], five_letters)
    five_letters.remove(signals[5])
    signals[6] = find_six(signals[5], six_letters)
    six_letters.remove(signals[6])
    signals[2] = five_letters[0]
    signals[0] = six_letters[0]
    signals = {k: "".join(sorted(v)) for k, v in signals.items()}
    return signals


def decipher_values(signals, values):
    signals = {v: k for k, v in signals.items()}
    values = ["".join(sorted(value)) for value in values.split()]
    return "".join(str(signals[value]) for value in values)


def sum_values(input):
    total = 0
    for line in input.strip().split("\n"):
        digits, values = line.split(" | ")
        signals = decode_signals(digits)
        values = decipher_values(signals, values)
        total += int(values)
    return total


assert sum_values(SAMPLES) == 61229
print(sum_values(input))
