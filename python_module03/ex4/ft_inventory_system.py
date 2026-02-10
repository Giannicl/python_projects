def add_player(inventory: dict, player: str) -> None:
    inventory[player] = {}


def add_item(inventory: dict, player: str, item: str) -> None:
    inventory[player][item] = {}


def add_feature(
    inventory: dict, player: str, item: str, feature: str, value: str | int
) -> None:
    inventory[player][item][feature] = value


def count_amount_type(
    inventory: dict, player: str, feature: str, value: str | int
) -> int:
    count = 0
    for item_detail in inventory[player].values():
        if item_detail[feature] == value:
            count += item_detail["amount"]
    return count


def transfer_items(
    inventory: dict, player1: str, player2: str,
    item: str, feature: str, quantity: int
) -> None:
    inventory[player1][item][feature] -= quantity
    inventory[player2][item][feature] += quantity
    print("Transaction successful!")


def most_valuable_player(inventory: dict) -> str:
    most_valuable = ""
    max_gold = 0
    gold = 0
    for player in inventory.keys():
        gold = inventory[player]["gold"]["amount"]

        if gold > max_gold:
            max_gold = gold
            most_valuable = player
    return most_valuable


def player_most_items(inventory: dict) -> str:
    player_most_items = ""
    max_item_count = 0
    count = 0
    for player in inventory.keys():
        count = len(inventory[player])
        if count > max_item_count:
            max_item_count = count
            player_most_items = player
    return player_most_items


def rarest_items(inventory: dict) -> None:
    count = 0
    list_rarest_items = []
    list_size = 0
    for player in inventory.keys():
        for item in inventory[player].keys():
            count = 0
            for other_player in inventory.keys():
                if item in inventory[other_player]:
                    count += 1
            if count == 1:
                list_rarest_items += [item]
    list_size = len(list_rarest_items)
    i = 0
    while i < list_size:

        if i < list_size - 1:
            print(f"{list_rarest_items[i]}", end=", ")
        else:
            print(f"{list_rarest_items[i]}")
        i += 1


def test_inventory_system() -> None:

    inventory = {}
    player1 = "Alice"
    item = "sword"
    add_player(inventory, player1)
    add_item(inventory, player1, item)
    add_feature(inventory, player1, item, "type", "weapon")
    add_feature(inventory, player1, item, "rarity", "rare")
    add_feature(inventory, player1, item, "price", 500)
    add_feature(inventory, player1, item, "amount", 1)
    item = "potion"
    add_item(inventory, player1, item)
    add_feature(inventory, player1, item, "type", "consumable")
    add_feature(inventory, player1, item, "rarity", "common")
    add_feature(inventory, player1, item, "price", 50)
    add_feature(inventory, player1, item, "amount", 5)
    item = "shield"
    add_item(inventory, player1, item)
    add_feature(inventory, player1, item, "type", "armor")
    add_feature(inventory, player1, item, "rarity", "uncommon")
    add_feature(inventory, player1, item, "price", 200)
    add_feature(inventory, player1, item, "amount", 1)
    item = "gold"
    add_item(inventory, player1, item)
    add_feature(inventory, player1, item, "type", "currency")
    add_feature(inventory, player1, item, "amount", 850)
    item = "magic_ring"
    add_item(inventory, player1, item)
    add_feature(inventory, player1, item, "type", "relic")
    add_feature(inventory, player1, item, "rarity", "rare")
    add_feature(inventory, player1, item, "price", 20000)
    add_feature(inventory, player1, item, "amount", 1)
    player2 = "Bob"
    add_player(inventory, player2)
    add_item(inventory, player2, "potion")
    add_feature(inventory, player2, "potion", "type", "consumable")
    add_feature(inventory, player2, "potion", "rarity", "common")
    add_feature(inventory, player2, "potion", "price", 50)
    add_feature(inventory, player2, "potion", "amount", 1)
    item = "gold"
    add_item(inventory, player2, item)
    add_feature(inventory, player2, item, "amount", 300)
    item = "shield"
    add_item(inventory, player2, item)
    add_feature(inventory, player2, item, "type", "armor")
    add_feature(inventory, player2, item, "rarity", "uncommon")
    add_feature(inventory, player2, item, "price", 100)
    add_feature(inventory, player2, item, "amount", 3)

    print("=== Player Inventory System ===")
    print("\n=== Alice's Inventory ===")
    sword_type = inventory["Alice"]["sword"]["type"]
    sword_rarity = inventory["Alice"]["sword"]["rarity"]
    sword_amount = inventory["Alice"]["sword"]["amount"]
    sword_price = inventory["Alice"]["sword"]["price"]
    print(
        f"sword ({sword_type}, "
        f"{sword_rarity}): "
        f"{sword_amount}"
        f"x @ {sword_price} gold each "
        f"= {sword_amount * sword_price} gold"
    )
    potion_type = inventory["Alice"]["potion"]["type"]
    potion_rarity = inventory["Alice"]["potion"]["rarity"]
    potion_amount = inventory["Alice"]["potion"]["amount"]
    potion_price = inventory["Alice"]["potion"]["price"]
    print(
        f"potion ({potion_type}, {potion_rarity}): "
        f"{potion_amount}x @ {potion_price} gold each "
        f"= {potion_amount * potion_price} gold"
    )
    shield_type = inventory["Alice"]["shield"]["type"]
    shield_rarity = inventory["Alice"]["shield"]["rarity"]
    shield_amount = inventory["Alice"]["shield"]["amount"]
    shield_price = inventory["Alice"]["shield"]["price"]
    print(
        f"shield ({shield_type}, {shield_rarity}): "
        f"{shield_amount}x @ {shield_price} gold each "
        f"= {shield_amount * shield_price} gold"
    )
    sword_value = sword_amount * sword_price
    potion_value = potion_amount * potion_price
    shield_value = shield_amount * shield_price
    inventory_value = sword_value + potion_value + shield_value
    item_count = sword_amount + potion_amount + shield_amount
    print(f"\nInventory value: {inventory_value} gold")
    print(f"Item count: {item_count} items")
    print(
        f"Categories: weapon({count_amount_type(inventory,
                                                player1, "type", "weapon")}), "
        f"consumable({count_amount_type(inventory,
                                        player1, "type", "consumable")}), "
        f"armor({count_amount_type(inventory, player1, "type", "armor")})"
    )
    print("\n=== Transaction: Alice gives Bob 2 potions ===")
    transfer_items(inventory, player1, player2, "potion", "amount", 2)
    print("\n=== Updated Inventories ===")
    print(f"Alice potions: {inventory[player1]["potion"]["amount"]}")
    print(f"Bob potions: {inventory[player2]["potion"]["amount"]}")
    print("\n=== Inventory Analytics ===")
    most_valuable = most_valuable_player(inventory)
    print(
        "Most valuable player: "
        f"{most_valuable} ({inventory[most_valuable]["gold"]["amount"]} gold)"
    )
    most_items = player_most_items(inventory)
    print(f"Most items: {most_items} ({len(inventory[most_items])} items)")
    print("Rarest items: ", end="")
    rarest_items(inventory)


if __name__ == "__main__":
    test_inventory_system()
