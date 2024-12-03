import random

class Player:
    def __init__(self, name, is_human=True):
        self.name = name
        self.is_human = is_human
        self.health = 100

    def choose(self):
        if self.is_human:
            choice = input(f"{self.name}, escolha entre Pedra, Papel, Tesoura, Lagarto, ou Spock: ").capitalize()
            while choice not in options:
                choice = input(f"Escolha inválida. Tente novamente: ").capitalize()
        else:
            choice = random.choice(options)
        print(f"{self.name} escolheu: {choice}")
        return choice

# Mapeia como cada escolha vence ou perde
def determine_winner(player1_choice, player2_choice):
    if player1_choice == player2_choice:
        return None
    elif player2_choice in rules[player1_choice]:
        return 1
    else:
        return 2

options = ["Pedra", "Papel", "Tesoura", "Lagarto", "Spock"]
rules = {
    "Pedra": ["Tesoura", "Lagarto"],
    "Papel": ["Pedra", "Spock"],
    "Tesoura": ["Papel", "Lagarto"],
    "Lagarto": ["Spock", "Papel"],
    "Spock": ["Tesoura", "Pedra"]
}

# Função principal
def main():
    print("Bem-vindo ao Pedra, Papel, Tesoura, Lagarto, Spock!")
    print("Regras: Pedra > Tesoura e Lagarto, Papel > Pedra e Spock, etc.\n")

    player1 = Player("Jogador 1")
    player2 = Player("Computador", is_human=False)

    while player1.health > 0 and player2.health > 0:
        print(f"\n{player1.name} Vida: {player1.health} | {player2.name} Vida: {player2.health}")
        
        player1_choice = player1.choose()
        player2_choice = player2.choose()

        winner = determine_winner(player1_choice, player2_choice)
        if winner is None:
            print("Empate! Ambos mantêm suas vidas.")
        elif winner == 1:
            print(f"{player1.name} venceu esta rodada!")
            player2.health -= 20
        else:
            print(f"{player2.name} venceu esta rodada!")
            player1.health -= 20

    if player1.health > 0:
        print(f"\n{player1.name} venceu o jogo!")
    else:
        print(f"\n{player2.name} venceu o jogo!")

if __name__ == "__main__":
    main()
