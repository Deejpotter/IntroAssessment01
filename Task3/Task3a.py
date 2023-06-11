# Written by Daniel Potter. Student ID: A00124220

"""
(f) Write a Python program to print the following string in a specific format (see the output). Use
  escape sequences in the string ‘\t’ and ‘\n’ Sample String:
  "Baby baby, Yes Mama, Eating sugar, No Mama, Telling a lie, No Mama, Open your mouth, Ha
  Ha Ha!"
  Expected Output:
  Baby baby,
                Yes Mama,
  Eating sugar,
                No Mama,
  Telling a lie,
                No Mama,
  Open your mouth,
                Ha Ha Ha!

  vii. ‘b’ raised to power a

Print the results of all operations on variables
"""

# Set the initial string. It looks like the string in the question is indented by 4 tabs.
string = "Baby baby,\n\t\t\t\tYes Mama,\nEating sugar,\n\t\t\t\tNo Mama,\nTelling a lie,\n\t\t\t\tNo Mama,\nOpen your mouth,\n\t\t\t\tHa Ha Ha!\n"

# Print the string
print(string)

# b raised to power a
a = int(input("Enter the exponent for the operation: "))  # Cast the input to an int
b = int(input("Enter the base for the operation: "))  # Cast the input to an int
print(b, "raised to power", a, "is", str(b ** a))  # Cast the result to a string for printing
