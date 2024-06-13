#1. The Calculator App
#Task 1:
def add_nums(num1, num2):
    return num1 + num2

def sub_nums(num1, num2):
    return num1 - num2

def multiply_nums(num1, num2):
    return num1 * num2

def divide_nums(num1, num2):
    return num1 / num2
    

#Task 2
def main():
    print("""
    Please choose from the list below using the number associated:
          1. Addition
          2. Subtraction
          3. Multiplication
          4. Division
""")
    while True:
        response = input("What would you like to do?")
        if response == "1":
            print("Addition!")
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            print("Result: ", add_nums(num1, num2))
        elif response == "2":
            print("Subtraction!")
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            print("Result: ", sub_nums(num1, num2))
        elif response == "3":
            print("Multiplication!")
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            print("Result: ", multiply_nums(num1, num2))
        elif response == "4":
            print("Division!")
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            print("Result: ", divide_nums(num1, num2))
        else:
            print("Invalid, Please try again")

main()
    

#2. The Shopping List Maker
#Task 1:
shopping_list = []

def add_item(shopping_list):
    item = input("What would you like to add to the shopping list?")
    shopping_list.append(item)
    print(f"{item} was added to your shopping list")

#Task 2.
def remove_item(shopping_list):
    item = input("Which would you like to remove from the shopping list? ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} was removed from your shopping list")
    else:
        print(f"{item} is not in your cart.")



def main(shopping_list):
    print("""
    Please choose from the list below:
          1. Add item to shopping list
          2. Remove item from shopping list
          3. See current shopping list
""")
    while True:
        response = input("What would you like to do?")
        if response == "1":
            add_item(shopping_list)
        elif response == "2":
            remove_item(shopping_list)
        elif response == "3":
            print("Here's what's in your current list...")
            print(shopping_list)
                
        else: 
            print("Please choose a valid option 1, 2, or 3")


main(shopping_list)