print("Welcome tot he secret auction program.")

bidders = {}
highest_bid = 0
winner = ""

is_running = True

while is_running:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))

    bidders[name] = bid

    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()

    if other_bidders == "no":
        is_running = False

for person in bidders:
    bid_amount = bidders[person]
    
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = person

        

print(f"{winner} with the bid {highest_bid}")
print(f"Results: \n")


items = list(bidders.items())

for i in range(len(items)):
    for j in range(0, len(items)-i-1):
        if items[j][1] < items[j+1][1]:
            items[j], items[j+1] = items[j+1], items[j]

for name, amount, in items:
    print(name, amount)