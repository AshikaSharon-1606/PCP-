def print_divisors(num):
    if num <=0:
        print("Please enter a positive integer.")
        return
    
    print(f"divisors of {num}:")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i)
print_divisors(36)
print_divisors(37)