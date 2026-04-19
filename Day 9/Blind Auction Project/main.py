# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
from art import logo
print(logo)
print("Welcome to the Silent Auction!\n")

#def bidder():
more_bidders = True
bidder_list = {}
while more_bidders:
    name = input("What is your name?\n")
    bid = int(input("How much would you like to bid?\n"))
    more = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
        #for person in bidder:
    #bidder_list += {
    bidder_list.update({
        name : bid
    })
    #print(bidder_list)

    if more == "no":
        more_bidders = False
    if more == "yes":
        print("\n" * 20)

max_bid = 0
# bidder_name = ""
# for name in bidder_list:
for name in bidder_list:
    #print(bidder_list[name])
    # bid_amount = bidder_list[bidder_name]
    # if bid_amount > max_bid:
    #     max_bid = bid_amount
    bid = bidder_list[name]
    if bid > max_bid:
        max_bid = bid
print(f"{name} has the winning bid!")
        # print(bid)
        # print(max_bid)
        # print(bidder_list)
        # #print(bidder_name[0][bid])


# print(bidder_list)

#bidder()
# print(name, bid)