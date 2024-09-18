# Initialize an empty dictionary to store guests
guests = {}

# Get the number of people joining
num_people = int(input("Enter the number of people joining (including you): "))

# Check if the number is valid
if num_people <= 0:
    print("No one is joining for the party")
else:
    # Iteratively take input for each person's name
    for i in range(num_people):
        name = input(f"Enter the name of person {i+1}: ")
        guests[name] = 0  # Initialize each person's value to 0

    # Print the resulting dictionary
    print(guests)

if num_people <= 0:
    for i in range(bill):
        bill_amount = int(input("Enter the bill value: "))
        bill_split = bill_amount // num_people



