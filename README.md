# Perfect-number-app
Python 
# Step 1: Request a maximum integer from the user
max_value = int(input("Enter a maximum integer: "))

print("\nPerfect numbers between 1 and", max_value, "are:")

 Step 2: Loop through numbers from 1 to max_value
for num in range(1, max_value + 1):
    sum_of_divisors = 0  # Step 3: Initialize sum of divisors

Step 4: Find divisors and sum them
    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i
 Step 5: Check if the number is perfect
    if sum_of_divisors == num:
        print(num)
