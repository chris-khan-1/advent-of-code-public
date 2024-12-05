from collections import OrderedDict, defaultdict
from itertools import combinations

shop_details = {
    "weapons": {
        "dagger": {"cost": 8, "damage": 4, "armour": 0},
        "shortsword": {"cost": 10, "damage": 5, "armour": 0},
        "warhammer": {"cost": 25, "damage": 6, "armour": 0},
        "longsword": {"cost": 40, "damage": 7, "armour": 0},
        "greataxe": {"cost": 74, "damage": 8, "armour": 0},
    },
    "armour_item": {
        "leather": {"cost": 13, "damage": 0, "armour": 1},
        "chainmail": {"cost": 31, "damage": 0, "armour": 2},
        "splintmail": {"cost": 53, "damage": 0, "armour": 3},
        "bandedmail": {"cost": 75, "damage": 0, "armour": 4},
        "platemail": {"cost": 102, "damage": 0, "armour": 5},
        "no_armour": {"cost": 0, "damage": 0, "armour": 0},
    },
    "rings": {
        "damage+1": {"cost": 25, "damage": 1, "armour": 0},
        "damage+2": {"cost": 50, "damage": 2, "armour": 0},
        "damage+3": {"cost": 100, "damage": 3, "armour": 0},
        "defense+1": {"cost": 20, "damage": 0, "armour": 1},
        "defense+2": {"cost": 40, "damage": 0, "armour": 2},
        "defense+3": {"cost": 80, "damage": 0, "armour": 3},
    },
}


def get_value_from_items(
    attribute: str, weapon: str, armour_item: str, rings: tuple
) -> int:
    return (
        shop_details["weapons"][weapon][attribute]
        + shop_details["armour_item"][armour_item][attribute]
        + sum([shop_details["rings"][ring][attribute] for ring in rings])
    )


def get_player_stats_combos():
    combos = defaultdict(dict)
    combo = 0

    ring_combos = []
    for i in range(3):
        for j in combinations(shop_details["rings"], i):
            ring_combos.append(j)

    for weapon in shop_details["weapons"]:
        for armour_item in shop_details["armour_item"]:
            for rings in ring_combos:
                combos[combo] = {
                    "weapon": weapon,
                    "armour_item": armour_item,
                    "rings": rings,
                    "cost": get_value_from_items(
                        attribute="cost",
                        weapon=weapon,
                        armour_item=armour_item,
                        rings=rings,
                    ),
                    "damage": get_value_from_items(
                        attribute="damage",
                        weapon=weapon,
                        armour_item=armour_item,
                        rings=rings,
                    ),
                    "armour": get_value_from_items(
                        attribute="armour",
                        weapon=weapon,
                        armour_item=armour_item,
                        rings=rings,
                    ),
                    "hit_points": 100,
                }

                combo += 1
    return OrderedDict(sorted(combos.items(), key=lambda item: item[1]["cost"]))


def get_winner(player_stats: dict, boss_stats: dict) -> str:
    attacker = 0
    while True:
        if attacker == 0:
            # at least 1 damage
            damage = max(player_stats["damage"] - boss_stats["armour"], 1)
            boss_stats["hit_points"] = boss_stats["hit_points"] - damage
            if boss_stats["hit_points"] <= 0:
                return "player"
            else:
                attacker += 1
        if attacker == 1:
            # at least 1 damage
            damage = max(boss_stats["damage"] - player_stats["armour"], 1)
            player_stats["hit_points"] = player_stats["hit_points"] - damage
            if player_stats["hit_points"] <= 0:
                return "boss"
            else:
                attacker -= 1


def get_cheapest_win(boss_stats: dict) -> int | None:
    possible_player_stats = get_player_stats_combos()
    for player_stats in possible_player_stats.values():
        # copy to get same input again
        winner = get_winner(player_stats=player_stats, boss_stats=boss_stats.copy())
        if winner == "player":
            return player_stats["cost"]
    return None


def get_most_expensive_loss(boss_stats: dict) -> int | None:
    possible_player_stats = get_player_stats_combos()
    for player_stats in reversed(possible_player_stats.values()):
        winner = get_winner(player_stats=player_stats, boss_stats=boss_stats.copy())
        if winner == "boss":
            return player_stats["cost"]
    return None


if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))

    import helpers

    input_path = "./src/aoc_2015/day_21/input.txt"
    result_path = "./src/aoc_2015/day_21/result.txt"

    boss_stats = {"hit_points": 109, "damage": 8, "armour": 2}
    cheapest_win = get_cheapest_win(boss_stats=boss_stats)
    most_expensive_loss = get_most_expensive_loss(boss_stats=boss_stats)

    result = f"""\
        Part 1: The cheapest win costs {cheapest_win} gold.
        Part 2: The most expensive loss costs {most_expensive_loss} gold.
        """

    helpers.write_file(file_path=result_path, contents=result)
