# 1
#date = '2025-12-31'
#new_date = tuple(date.split('-')[::-1])
#print(new_date)
# 2
#lst = ['1', '2', '3', '4', '5']
#sum_of_elements = sum(int(x) for x in lst)
#print(sum_of_elements)
# 3
#lst = [1, 2, 3, 4, 5, 6]
#mid = len(lst) // 2

#first_half_sum = sum(lst[:mid])
#second_half_sum = sum(lst[mid:])

#result = first_half_sum / second_half_sum

#print(result)

# 4
#def find_divisors(numbers):
#result = []
#for num in numbers:
#divisors = []
#for i in range(1, num+1):
#if num % i == 0:
#divisors.append(i)
#result.append(divisors)
#return resul
#  5
#dct1 = {
#'a': 1,
#'b': 2,
#}
#dct2 = {
#'c': 3,
#'d': 4,
#}
# 6
#def find_min_max(numbers):
#result = {}
#result['max'] = max(numbers)
#result['min'] = min(numbers)
#return result
# 7
# def find_divisors(numbers):
#result = []
#for num in numbers:
#divisors = []
#for i in range(1, num+1):
#if num % i == 0:
#divisors.append(i)
#result.append(divisors)
#return result
# 8
#def generate_random_numbers(N, start, end):
#result = []
#previous_number = None
#for _ in range(N):
#number = random.randint(start, end)
#while number == previous_number:
#number = random.randint(start, end)
#result.append(number)
#previous_number = number
#return result
# 9
#def random_color():
# Список доступных цветов
#colors = ["красный", "синий", "зеленый", "желтый", "оранжевый", "фиолетовый", "розовый", "голубой"]

# Выбираем случайный цвет из списка
#random_index = random.randint(0, len(colors) - 1)
#return colors[random_index]

# Пример использования функции
#random_color_result = random_color()
#print("Случайный цвет:", random_color_result)
# 10
#def split_into_syllables(word):
#vowels = "аеёиоуыэюя"
#syllables = []

#word = word.lower()
#i = 0

#while i < len(word):
#if word[i] in vowels:
#start = i
#while i + 1 < len(word) and word[i + 1] not in vowels:
#i += 1
#syllables.append(word[start:i+1])
#i += 1

#return syllables

#word_example = "программирование"
#print(split_into_syllables(word_example))
# 11
#import random

#def shuffle_list(input_list):
#shuffled_list = input_list.copy()  # Создаем копию исходного списка, чтобы не изменять его
#random.shuffle(shuffled_list)     # Перемешиваем копию списка
#return shuffled_list

# Пример использования функции:
#my_list = [1, 2, 3, 4, 5]
#shuffled = shuffle_list(my_list)
#print(shuffled)