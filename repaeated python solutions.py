# 1. Reverse a string
def reverse_string(s):
    return s[::-1]

# 2. Check if a string is a palindrome
def is_palindrome(s):
    return s == s[::-1]

# 3. Find the factorial of a number
def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

# 4. Print Fibonacci series up to N terms
def fibonacci(n):
    series = [0, 1]
    for i in range(2, n):
        series.append(series[-1] + series[-2])
    return series[:n]

# 5. Check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# 6. Find the sum of digits in a number
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

# 7. Swap two numbers without using a third variable
def swap(a, b):
    a, b = b, a
    return a, b

# 8. Find the largest of three numbers
def largest_of_three(a, b, c):
    return max(a, b, c)

# 9. Count the number of vowels in a string
def count_vowels(s):
    return sum(1 for char in s.lower() if char in 'aeiou')

# 10. Calculate the area of a circle (given radius)
def area_of_circle(radius):
    pi = 3.14159
    return pi * radius * radius

# 🟡 List & Dictionary Based Questions

# 11. Remove duplicates from a list
def remove_duplicates(lst):
    return list(set(lst))

# 12. Find the second largest number in a list
def second_largest(lst):
    lst = list(set(lst))
    lst.sort()
    return lst[-2] if len(lst) >= 2 else None

# 13. Count frequency of elements in a list
def count_frequency(lst):
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1
    return freq

# 14. Find common elements in two lists
def common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))

# 15. Sort a list without using sort()
def manual_sort(lst):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst

# 16. Merge two dictionaries
def merge_dicts(d1, d2):
    merged = d1.copy()
    merged.update(d2)
    return merged

# 17. Find the key with the maximum value in a dictionary
def max_value_key(d):
    return max(d, key=d.get)

# 18. Invert a dictionary (key ↔ value)
def invert_dict(d):
    return {v: k for k, v in d.items()}

# 19. Flatten a nested list
def flatten_list(nested):
    return [item for sublist in nested for item in sublist]

# 20. Sum of all values in a dictionary
def sum_dict_values(d):
    return sum(d.values())

# 🔵 String Manipulation Questions

# 21. Check if two strings are anagrams
def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

# 22. Count frequency of each character in a string
def char_frequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

# 23. Remove all punctuation from a string
def remove_punctuation(s):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    return ''.join(char for char in s if char not in punctuations)

# 24. Convert a string to title case
def to_title_case(s):
    return s.title()

# 25. Replace all spaces with hyphens in a string
def replace_spaces(s):
    return s.replace(' ', '-')

# 26. Find the first non-repeating character in a string
def first_non_repeating(s):
    for char in s:
        if s.count(char) == 1:
            return char
    return None

# 27. Reverse each word in a sentence
def reverse_each_word(sentence):
    return ' '.join(word[::-1] for word in sentence.split())

# 28. Count number of words in a sentence
def word_count(sentence):
    return len(sentence.split())

# 29. Remove duplicate characters from a string
def remove_duplicate_chars(s):
    result = ''
    for char in s:
        if char not in result:
            result += char
    return result

# 30. Check if two strings are rotations of each other
def is_rotation(s1, s2):
    return len(s1) == len(s2) and s2 in s1 + s1
# 🟣 Logic/Pattern/Number Questions

# 31. Print a number pattern (pyramid)
def number_pyramid(n):
    for i in range(1, n + 1):
        print(' ' * (n - i) + ' '.join(str(i) for _ in range(i)))

# 32. Find all Armstrong numbers in a range
def armstrong_numbers(start, end):
    result = []
    for num in range(start, end + 1):
        power = len(str(num))
        if num == sum(int(d)**power for d in str(num)):
            result.append(num)
    return result

# 33. Generate a random number within a range
import random
def random_in_range(start, end):
    return random.randint(start, end)

# 34. Find GCD and LCM of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

# 35. Check if a number is a perfect square
def is_perfect_square(n):
    return int(n**0.5)**2 == n

# 36. Find the missing number in a list (1 to N)
def find_missing(lst, n):
    return sum(range(1, n + 1)) - sum(lst)

# 37. Move all zeros to end of the list
def move_zeros_end(lst):
    non_zeros = [x for x in lst if x != 0]
    return non_zeros + [0] * (len(lst) - len(non_zeros))

# 38. Separate even and odd numbers from a list
def separate_even_odd(lst):
    even = [x for x in lst if x % 2 == 0]
    odd = [x for x in lst if x % 2 != 0]
    return even, odd

# 39. Find the longest word in a sentence
def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

# 40. Check if a year is a leap year
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# 🧠 Intermediate to Advanced Level

# 41. Simple calculator using functions
def calculator(a, b, op):
    if op == '+': return a + b
    elif op == '-': return a - b
    elif op == '*': return a * b
    elif op == '/': return a / b if b != 0 else 'Divide by 0 error'
    else: return 'Invalid operator'

# 42. Basic login/signup system
users = {}
def signup(username, password):
    if username in users:
        return "User already exists"
    users[username] = password
    return "Signup successful"

def login(username, password):
    return "Login successful" if users.get(username) == password else "Invalid credentials"

# 43. Read/write data to a file
def write_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content)

def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()

# 44. Shopping cart using dictionary
cart = {}
def add_to_cart(item, price):
    cart[item] = cart.get(item, 0) + price
    return cart

# 45. Count words in a file
def count_words_in_file(filename):
    with open(filename, 'r') as f:
        return len(f.read().split())

# 46. Sort a list of tuples by second value
def sort_by_second(tuples):
    return sorted(tuples, key=lambda x: x[1])

# 47. Group anagrams from a list of words
def group_anagrams(words):
    result = {}
    for word in words:
        key = ''.join(sorted(word))
        result.setdefault(key, []).append(word)
    return list(result.values())

# 48. Remove all duplicate rows from a list of lists
def remove_duplicate_rows(data):
    return [list(x) for x in set(tuple(row) for row in data)]

# 49. Rotate a list by K positions
def rotate_list(lst, k):
    k = k % len(lst)
    return lst[-k:] + lst[:-k]

# 50. Convert a Roman numeral to integer
def roman_to_int(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev = 0
    for char in reversed(s):
        if roman[char] < prev:
            total -= roman[char]
        else:
            total += roman[char]
        prev = roman[char]
    return total
