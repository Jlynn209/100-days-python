print("Welcome to the tip calculator ")
bill = input("What was the total bill? $ ")
number_of_people = input("How many people to split the bill? ")
percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")

my_share = float(bill) / float(number_of_people)
tip = my_share * (0.01 * float(percentage))
total = my_share + tip
print(f"${total:.2f}")