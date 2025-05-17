import sys
import random
import time

HeroesLate = ["Witch Doctor", "Lion", "IO", "Oracle", "Sniper", "Pudge", "Pugna", "Spirit Breaker", "Rubik", "Techies", "Hoddwing", 
              "Ringmaster", "Monkey King", "Tinker", "Wind Ranger", "Weaver"]
HeroesFelix = ["Dark Seer", "Bristleback", "Axe", "Windranger", "Brewmaster", "Clockwerk", "Bounty Hunter", "Spirit Breaker",
               "Enchantress", "Ogre Magi", "Night Stalker", "Batrider", "Dawnbreaker", "Kunkka"]



def get_x_of_list(x: int, list: list):
    """
    takes x entries of a list and removes them in the process
    """
    random_generator = random.Random()
    return_list = []
    for i in range(0, x):
        entry = list[random_generator.randrange(0, len(list))]
        return_list.append(entry)
        list.remove(entry)
    return return_list

def print_waiter():
    print(f"Calculating...  [---------]")
    time.sleep(0.2)
    print(f"Calculating...  [+++------]")
    time.sleep(0.2)
    print(f"Calculating...  [++++++---]")
    time.sleep(0.2)
    print(f"Calculating...  [++++++++-]")
    time.sleep(0.2)
    print(f"Calculating...  [+++++++++]")
    time.sleep(0.2)



if __name__ == "__main__":
    print_waiter()
    hero_list = HeroesLate
    # hero_list = HeroesFelix
    if len(sys.argv) < 2:
        winner = get_x_of_list(1, hero_list)
        print(f"And the winner is: {winner}")
    elif int(sys.argv[1]) > len(hero_list):
        print("Too many, select less please")
    else:
        winners = get_x_of_list(int(sys.argv[1]), hero_list)
        n = 1
        print(f"And the winners are:")
        for winner in winners:
            print(f"{n}: {winner}")
            n += 1
