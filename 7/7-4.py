print("Please enter your pizza toppings. Press enter after each topping, and type 'quit' to end your order.")
end = False
while end == False:
    topping = input("What is your topping?")
    if topping == 'quit':
        end = True
    else:
        print(topping.title() + "will be added to your pizza.")
print("Thank you for ordering!")