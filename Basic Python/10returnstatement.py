# a function that accepts one argument/parameter
def order(item):
    # if the parameter is a string burger, it should return 1
    if item == "burger":
        return 1

# input that accepts item_name
item_name = input("Enter the item name: ")

# assign the function call to result
result = order(item_name)

# if the function call returns 1
# execute the command below
if result == 1:
    print("$5, Thank you for shopping")
    
# if the function call doesnt return 1
# execute the command below
else:
    print('No discount')

