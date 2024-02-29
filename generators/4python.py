def square_generator(a,b):
    for number in range(a, b+1):
        yield number**2
        
a = int(input())
b = int(input())

square_numbers = square_generator(a,b)

print(', '.join(map(str,square_numbers)))