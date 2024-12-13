from modules.input import get_numbers, get_operation
from modules.processing import add, subtract, multiply, divide
from modules.output import print_result, append_to_file

def main():
    num1, num2 = get_numbers()
    operation = get_operation()
    if operation == 'add':
        result = add(x, y)
    elif operation == 'subtract':
        result = subtract(x, y)
    elif operation == 'multiply':
        result = multiply(x, y)
    elif operation == 'divide':
        result = divide(num1, num2)
    else:
        result = "Invalid operation"
        print_result(operation, num1, num2, result)
    append_to_file(operation, num1, num2, result)
if __name__ == "__main__":
   main()
 