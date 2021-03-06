# https://www.codewars.com/kata/5b180e9fedaa564a7000009a/python
# Fix string case
# given a string that may have mixed uppercase and lowercase letters and your
# task is to convert that string to either lowercase only or uppercase only
# based on:

# make as few changes as possible.
# if the string contains equal number of uppercase and lowercase letters, convert the string to lowercase.


def fix_string_case(s):
    lower_count = sum(map(str.islower, s))
    upper_count = sum(map(str.isupper, s))
    if lower_count >= upper_count:
        return s.lower()
    else:
        return s.upper()


samplestring = input("Enter any string: ").strip()
print(fix_string_case(samplestring))
