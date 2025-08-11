# 1. Simple greeting
def name(name):
    print(f"Hello, {name}!")

name("Ali")


# 2. Greeting with default argument
def greets(name="friend"):
    return f"Hello {name}"

print(greets())
print(greets("Sara"))


# 3. Sum of three numbers
def multiple_arg(a, b, c):
    return a + b + c

print(multiple_arg(1, 2, 3))


# 4. Sum and product
def sum_product(num1, num2):
    total_sum = num1 + num2
    product = num1 * num2
    return total_sum, product

print(sum_product(4, 5))


# 5. Largest, smallest, and average
def filter_stats(list_nums):
    if not list_nums:
        return None, None, None
    
    largest = max(list_nums)
    smallest = min(list_nums)
    average = sum(list_nums) / len(list_nums)
    return largest, smallest, average

print(filter_stats([3, 7, 1, 9, 4]))
