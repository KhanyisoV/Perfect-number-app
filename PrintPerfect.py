max_value = int(input("Enter a maximum integer: "))

print("\nPerfect numbers between 1 and", max_value, "are:")
for num in range(1, max_value + 1):
    sum_of_divisors = 0
    for i in range(1,num):
        if num % i == 0:
            sum_of_divisors += i
            if sum_of_divisors == num:
                print(num)