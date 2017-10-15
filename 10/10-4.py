n1 = input("Enter the dividend.")
n2 = input("Enter the divisor.")

try:
    result = (int(n1) / int(n2))
except ZeroDivisionError:
    print("You cannot divide by 0!")
except ValueError:
    print("That is an invalid value!")
else:
    print(result)