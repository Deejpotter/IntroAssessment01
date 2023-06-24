# Written by Daniel Potter. Student ID: A00124220

"""
You are hired as a software coder for LoseWeightNow Pty Ltd located in Redfern, NSW, Australia. Your
task is to build a simple software program that receives input from the patients including their first name, last name,
age, body weight, and body height; your software program is to calculate the body mass index (BMI) of the patient, and
display the output as

“Welcome + First Name + Last Name. Your age is Age and your BMI is BMI Value”.

For example, if Adam Smith, 19 years old having BMI of 22.5 will display

“Welcome Adam Smith. You are 19 years old and your BMI is 22.5”

Write software program to accomplish the above given task.

"""

# Get the user's information
firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
age = int(input("Enter your age: "))  # Convert the age to an integer
weight = float(input("Enter your weight in kilograms: "))  # Convert the weight to a float
height = float(input("Enter your height in metres: "))  # Convert the height to a float

# Calculate the user's BMI. To calculate your BMI, divide your weight in kilograms by the square of your height in metres.
# https://www.health.gov.au/topics/overweight-and-obesity/bmi-and-waist
bmi = weight / (height ** 2)  # Get the square of the height first, then divide the weight by the square of the height

# Print the user's information
print("Welcome", firstName, lastName, ". You are", str(age), "years old and your BMI is", str(bmi))  # Convert the age and BMI to strings

# I referenced the Module 2 Resources for this code.
