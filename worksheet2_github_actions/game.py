from yatzy import Yatzy

def main():
    game = Yatzy()
    rolls_left = 3

    while rolls_left > 0:
        print(f"\nDice: {game.display_dice()}")
        cmd = input(f"You have {rolls_left} rolls left. Lock dice (e.g., 0 2 4) or press Enter to roll all: ")
        
        game.unlock_all()  # Reset all locks
        if cmd.strip():
            indices = list(map(int, cmd.strip().split()))
            game.lock_dice(indices)
        game.roll()
        rolls_left -= 1

    print(f"\nFinal Dice: {game.display_dice()}")
    print(f"Scores: Ones={game.Ones()}, Twos={game.Twos()}, Threes={game.Threes()}")
    print(f"One Pair: {game.OnePair()}, Full House: {game.FullHourse()}, Yatzy: {game.Yatzy()}")

if __name__ == "__main__":
    main()
