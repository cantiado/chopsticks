class Player():
    def __init__(self, h1: int = 1, h2: int = 1) -> None:
        if h1 > h2:
            h1, h2 = h2, h1
        self.hands = (h1, h2)
    
    def __repr__(self) -> str:
        return str(self.hands)

    def set_hands(self, h1: int, h2: int) -> None:
        if h1 > h2:
            h1, h2 = h2, h1
        self.hands = (h1, h2)
    

class Game():
    def __init__(self, players: int = 2) -> None:
        self.players: list[Player] = [Player()] * players

    def __repr__(self) -> str:
        out = ["Player\tHands"]
        for n, player in enumerate(self.players):
            out.append(f"{n: 5}.\t{str(player)}")
        return "\n".join(out)

    def _attack(self, p: int, target: int, value: int) -> None:
        p_hands = self.players[p]
        new_value = (p_hands[target] + value) % 5
        old_value = p_hands[(target + 1) % 2]
        self.players[p].set_hands(new_value, old_value)

    def _divide(self, p: int) -> None:
        p_hands = self.players[p].hands
        if p_hands == (0, 2):
            self.players[p].set_hands(1, 1)
        elif p_hands == (0, 3):
            self.players[p].set_hands(1, 2)
        else:
            option = ""
            while option not in {"1", "2"}:
                option = input("Divide into 1. (1, 3) OR 2. (2, 2)? ")
            if option == "1":
                self.players[p].set_hands(1, 3)
            else:
                self.players[p].set_hands(2, 2)
    
    def _transfer(self, p: int) -> None:
        next_hands = {
            (1, 3): self.players[p].set_hands(2, 2),
            (2, 2): self.players[p].set_hands(1, 3),
            (1, 4): self.players[p].set_hands(2, 3),
            (2, 3): self.players[p].set_hands(1, 4),
            (2, 4): self.players[p].set_hands(3, 3),
            (3, 3): self.players[p].set_hands(2, 4)
        }
        next_hands[self.players[p].hands]

    def _can_divide(self, p: int) -> bool:
        return self.players[p].hands in {(0, 2), (0, 3), (0, 4)}
    
    def _can_transfer(self, p: int) -> bool:
        return self.players[p].hands in {(1, 3), (2, 2), (1, 4), (2, 3), (2, 4), (3, 3)}
    

if __name__ == "__main__":
    print(Game())