import sys
import re

# Assignment 6 - Cristobal Lara
a = sys.argv[1]
b = sys.argv[2]
c = sys.argv[3]
d = sys.argv[4]
e = sys.argv[5]

entries = [a,b,c,d,e]

def is_number_regex(input):
    return bool(re.match(r'^\d+[.]?\d*$', str(input)))

def all_entries_are_numbers(entryList):
    for val in entryList:
        if not is_number_regex(val):
            return False
    return True

def extract_positive_numbers(numberList):
    newList = []
    for val in numberList:
        if float(val) >= 0:
            newList.append(float(val))
    return newList

def calculate_average(numberList):
    avg = 0
    for num in numberList:
        avg += float(num)
    return avg / len(numberList)

if not all_entries_are_numbers(entries):
    print("<h2>Error: All values must be valid numbers</h2>")
else:
    possitive_values = extract_positive_numbers(entries)

    if len(possitive_values) != len(entries):
        print("<h2>You have inserted one or more than one negative value</h2>")

    avg_result = calculate_average(entries)

    if avg_result > 50:
        print(f"<h2>The average of all the insterted numbers {avg_result} is greater than 50</h2>")
    
    possitive_values_count = len(possitive_values)
    even_or_odd="even"

    if possitive_values_count & 1 == 1:
        even_or_odd="odd"
    print(f"<h2>The count of possitives numbers in the entries list is {possitive_values_count} and it is an {even_or_odd} number</h2>")

    filtered_numbers = [num for num in possitive_values if float(num) > 10]
    sorted_list = sorted(filtered_numbers)

    print(f"<h2>The original list is: {entries}</h2>")
    print(f"<h2>Filter with values > 10: {filtered_numbers}</h2>")
    print(f"<h2>Final sorted list is: {sorted_list}</h2>")
