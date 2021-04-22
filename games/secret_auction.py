"""secret_auction_program"""
bids = {}
bidding_continue = True

def find_winner(bid_record):
    highest_bid = 0
    winner = ""
    for bidder in bid_record:
        bid_amount = bid_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

print("Welcome to the secret auction program.")

while bidding_continue:
    name = input("What is your name?: ")
    price = int(input("What's your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other users who want to bid? 'yes'/'no': ")

    if should_continue == "no":
        bidding_continue = False
        find_winner(bids)















