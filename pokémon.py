
from enum import Enum

class Element(Enum):
    GRASS = 1,
    FIRE = 2,
    WATER = 3,
    AIR = 4,
    ELECTRIC = 5,
    FAIRY = 6,
    POISON = 7,
    GRASS_POISON = 8

class Effects(Enum):
    STUN = 1

class Pokémon:
    def __init__(self, name: str, element: Element):
        self.name = name
        self.element = element
        self.attacks = []

    def learn(self, attack, power, effects=[]):
        self.attacks.append((attack, power, effects))

class Player:
    def __init__(self, name):
        self.name = name
        self.pokéballs = []

    def capture(self, pokemon):
        self.pokéballs.append(pokemon)

    def battle(self, opponent):
        """
        TODO: make a fight happen

        Add hit points
        Take turns
        Allow the player to recall a pokemon
        Allow the player to choose a pokemon
        Allow the player to choose which attacks
        Implement effects like stun, etc

        """
        p1 = self.pokéballs[0]
        p2 = opponent.pokéballs[0]
        pow1 = p1.attacks[0][1]
        pow2 = p2.attacks[0][1]
        print(f"{self.name}: 'I choose you, {p1.name}!'")
        print(f"{opponent.name}: 'Go, {p2.name}!'")
        print(f"{self.name}'s {p1.name} uses {p1.attacks[0][0]} to do {pow1} damage")
        print(f"{opponent.name}'s {p2.name} uses {p2.attacks[0][0]} to do {pow2} damage")

        if pow1 > pow2:
            print(f"{self.name} wins!")
        elif pow1 < pow2:
            print(f"{opponent.name} wins!")
        else:
            print("It's a draw!")

def main():
    josh = Player("Josh")
    chris = Player("Chris")

    pika = Pokémon("Pikachu", Element.ELECTRIC)
    pika.learn("Static", 70, [Effects.STUN, 0.3])

    josh.capture(pika)

    bulby = Pokémon("Bulbasaur", Element.GRASS_POISON)
    bulby.learn("Seed Bomb", 55)
    chris.capture(bulby)

    josh.battle(chris)

if __name__ == "__main__":
    main()