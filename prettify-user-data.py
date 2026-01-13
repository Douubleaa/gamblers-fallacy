import json

all_parameters = ["proxyWallet", "side", "asset", "conditionId", "size", "price", "timestamp", "title", "slug", "icon", "eventSlug", "outcome", "outcomeIndex", "name", "pseudonym", "bio", "profileImage", "profileImageOptimized", "transactionHash"]

desired_parameters = ["proxyWallet", "side", "asset", "conditionId", "size", "price", "timestamp", "title", "slug", "eventSlug", "outcome", "outcomeIndex", "transactionHash"]

def prettify(user_id):
    # Load raw data
    with open(f"raw_users/{user_id}.txt") as file:
        data = file.read()
    data = json.loads(data)

    # Generate a list containing desired parameters of each trade
    trades = []
    for trade in data:
        pretty_trade = []
        for parameter in trade:
            if parameter in desired_parameters:
                pretty_trade.append((parameter, trade[parameter]))
        trades.append(pretty_trade)
    return trades

# TODO - generate the list of users from existing file names in raw_users folder
users = [
    "0x63ce342161250d705dc0b16df89036c8e5f9ba9a",
    ]

for user_id in users:
    pretty_data = prettify(user_id)
    for trade in pretty_data:
        print(trade)