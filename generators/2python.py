def generate_even_numbers_up_to_n(n):
    for i in range(0, n + 1, 2):
        yield i

n = int(input())

even_numbers_generator = generate_even_numbers_up_to_n(n)
even_numbers_str = ','.join(map(str,even_numbers_generator))

print(even_numbers_str)

