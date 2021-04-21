# Reads in a list of floating point numbers either from a textfile passed as an argument to the script or via stdin.
# Numbers are separated by space characters and may contain either , or . as decimal separator.
# Prints out the mean, median, and standard deviation for these on stdout.
# The script should only use built-in commands, the math module (for math.sqrt()), and the sys module (for sys.argv and sys.stdin).

# Imports
import sys
import math


# import numbers from file or stdout
# found at https://www.knowledgehut.com/blog/programming/sys-argv-python-examples
def input_numbers():
    # control if a textfile is passed as an argument
    if len(sys.argv) > 1:
        raw_numbers = open(sys.argv[1]).read()
        return raw_numbers
    # if there is no argument, ask for user input
    else:
        print(
            "Please enter a series of floating point numbers (with dot or comma as decimal separator), separated by spaces: ")
        raw_numbers = sys.stdin.readline()
        return raw_numbers


# save input_numbers in an array
def list_numbers(raw_numbers):
    # replace decimal separator and split
    numbers = (str(raw_numbers).replace(",", ".")).split()
    clean_numbers = list()

    for i in numbers:
        clean_numbers.append(float(i))

    return clean_numbers


# calculate the mean
def get_mean(numbers):
    print(str(sum(numbers)))
    print(str(len(numbers)))
    return sum(numbers) / len(numbers)


# calculate the median
def get_median(numbers):
    # sort numbers
    numbers_sorted = sorted(numbers)
    numbers_length = len(numbers)
    # check if the number is even or odd and calculate median
    # since arrays start counting at 0, this must be taken into account in the calculation and the standard formulas are not used.
    if numbers_length % 2 == 0:
        median = sum(numbers_sorted[(numbers_length / 2):((numbers_length / 2) - 1)]) / 2
        return median
    else:
        median = numbers_sorted[(numbers_length - 1) // 2]
        return median


# calculate the standard deviation
def get_sd(numbers):
    mean = get_mean(numbers)
    numbers_length = len(numbers)
    var = 0
    for i in numbers:
        var += ((i - mean) ** 2) / (numbers_length - 1)
    sd = math.sqrt(var)
    return sd


if __name__ == "__main__":
    input_numbers = input_numbers()
    list_numbers = list_numbers(input_numbers)
    if len(list_numbers) < 3:
        print("Please restart and provide at least three numbers to get all calculations")
    else:
        print("The mean for your numbers is: " + str(get_mean(list_numbers)))
        print("The median for your numbers is: " + str(get_median(list_numbers)))
        print("The standard deviation for your numbers is: " + str(get_sd(list_numbers)))
