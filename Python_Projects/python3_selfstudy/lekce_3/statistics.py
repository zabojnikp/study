import collections
import sys

Statistics = collections.namedtuple("Statistics", "count mean mode median")

def main():
    if len(sys.argv) == 1 or sys.argv[1] in ('-h', '--help'):
        print('{0} <filename>'.format(sys.argv[0]))
        sys.exit()

    numbers = []
    frequencies = collections.defaultdict(int)

    for filename in sys.argv[1:]:
        for iteration, line in enumerate(open(filename, encoding='ascii'), start=1):
            for fields in line.split():
                try:
                    number = float(fields)
                    numbers.append(number)
                    frequencies[number] += 1
                
                except ValueError as err:
                    print("{filename}:{iteration}: skipping {fields}:{err}".format(**locals()))
    
    if numbers:
        statistics = count_statistics(numbers, frequencies)
        print(print_results(statistics)) 

    else:
        print("No numbers found")   


def count_statistics(numbers, frequencies):
    count = len(numbers)
    mean = sum(numbers) / len(numbers)
    mode = count_mode(frequencies, 3)
    median = count_median(numbers)
    return Statistics(count, mean, mode, median)

def count_mode(frequencies, max_mode):
    max_frequency = max(frequencies.values())
    mode = [number for number, frequency in frequencies.items() if frequency == max_frequency]

    if not (1 <= len(mode) <= max_mode):
        mode = None
    else:
        mode.sort()
    return mode

def count_median(numbers):
    numbers = sorted(numbers)
    middle = len(numbers) // 2
    median = numbers[middle]
    if len(numbers) % 2 == 0:
        median = (median + numbers[middle - 1]) / 2
    return median

def print_results(statistics):
    print("""
    count   = {0.count:6}
    mode    = {0.mode}
    mean    = {0.mean:9.2f}
    median  = {0.median:9.2f}""".format(statistics))

main()