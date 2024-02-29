# если надо по одтельному чтобы они делились на 3 и 4 то исходя из прошлой задачи можем прописать каждому функцию и задать собственный обьект генератор

# def generate_even_numbers_up_to_n(n):
#     for i in range(0, n + 1, 3):
#         yield i

# n = int(input())

# even_numbers_generator = generate_even_numbers_up_to_n(n)
# even_numbers_str = ','.join(map(str,even_numbers_generator))

# print(even_numbers_str)

# def generate_even_numbers_up_to_n(n):
#     for i in range(0, n + 1, 4):
#         yield i

# n = int(input())

# even_numbers_generator = generate_even_numbers_up_to_n(n)
# even_numbers_str = ','.join(map(str,even_numbers_generator))

# print(even_numbers_str)

# а если нужно чтобы число вместе делилась на 3 и 4 то он должен делиться на 12 то есть будет выглядить так:


# я оставлю этот пример 

def generate_even_numbers_up_to_n(n):
    for i in range(0, n + 1, 12):
        yield i

n = int(input())

even_numbers_generator = generate_even_numbers_up_to_n(n)
even_numbers_str = ','.join(map(str,even_numbers_generator))

print(even_numbers_str)

