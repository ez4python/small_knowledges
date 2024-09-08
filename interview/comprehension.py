"""
--------- Python Comprehensions ---------
"""

# 1. List Comprehension
squares = [x ** 2 for x in range(10)]
print(squares)

# 2. Set Comprehension
unique_squares = {x ** 2 for x in range(10)}
print(unique_squares)

# 3. Dictionary Comprehension
squares_dict = {x: x ** 2 for x in range(10)}
print(squares_dict)

# 4. Generator Comprehension
squares_gen = (x for x in range(10))
for square in squares_gen:
    print(square, end=' ')
print()

# Generation & Iteration
gen = (x for x in range(10))
iterator = iter(gen)
while True:
    try:
        item = next(iterator)
        print(item)
        print(id(item))
    except StopIteration:
        print('End of iterator reached.')
        break
