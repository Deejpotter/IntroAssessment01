# Written by Daniel Potter. Student ID: A00124220

"""
(e) Now, try entering the following arithmetic expressions using only a single operator in each case.
Note the response from the interpreter in each case and describe the answers and what you
understand from it. (To describe the answers, you can use comments in code or alternatively
use ‘print’ Python statement to display your answer).
4 + 2
4 + 2.0
3.5 – 4.0
5 * 7
23 / 4
23 / 4.0
23 % 4
3 ** 2
9 ** 0.5
"""

int_add = 4 + 2
print("4 + 2 =", int_add, "\nThe type of the result is", type(int_add), "\nAdding two integers results in an integer or a whole number.\n")

float_add = 4 + 2.0
print("4 + 2.0 =", float_add, "\nThe type of the result is", type(float_add),
      "\nAdding an integer and a float results in a floating point number which is a number with a decimal point.",
      "The integer is converted to a float.\n")

float_minus = 3.5 - 4.0
print("3.5 - 4.0 =", float_minus, "\nThe type of the result is", type(float_minus),
      "\nSubtracting two floats results in a float. In this case, the result is a negative number.\n")

int_multiply = 5 * 7
print("5 * 7 =", int_multiply, "\nThe type of the result is", type(int_multiply),
      "\nMultiplying two integers results in an integer.\n")

int_divide = 23 / 4
print("23 / 4 =", int_divide, "\nThe type of the result is", type(int_divide),
      "\nDividing two integers results in a float. In this case, the result is a decimal number or float.\n")

float_divide = 23 / 4.0
print("23 / 4.0 =", float_divide, "\nThe type of the result is", type(float_divide),
      "\nDividing an integer and a float results in a float.\n")

int_modulus = 23 % 4
print("23 % 4 =", int_modulus, "\nThe type of the result is", type(int_modulus),
      "\nThe modulus operator (%) returns the remainder of the division of the first number by the second number.",
      "Useful for checking if one number is divisible by another.\n")

int_exponent = 3 ** 2
print("3 ** 2 =", int_exponent, "\nThe type of the result is", type(int_exponent),
      "\nThe exponent operator (**) raises the first number to the power of the second number.",
      "That means the first number is multiplied by itself the second number of times.\n")

float_exponent = 9 ** 0.5
print("9 ** 0.5 =", float_exponent, "\nThe type of the result is", type(float_exponent),
      "\nAlso uses the exponent operator (**). In this case, the second number is a float so the result is converted to a float.")
