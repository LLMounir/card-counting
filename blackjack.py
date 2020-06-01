"""
start : 21-06-2019
end :

Blackjack Card Counter
"""
def setup_GUI():
    pass

def setup():
    decks = int(input("How many decks are being used ? "))
    balance = int(input("Current balance: "))
    min_bet = int(input("Minimal bet: "))
    max_bet = int(input("Maximal bet (0 for no max): "))
    cards = ['2','3','4','5','6','7','8','9','10','A','10','10','10']
    shoe = []
    for i in range(decks):
        shoe += cards
    dead_deck = []
    return decks, balance, min_bet, max_bet, shoe, dead_deck

def basic_start(player, dealer):
    if type(player) == tuple:
        """ SOFT HANDS + AA """
        if 'A' in player:
            if player[0] == player[1]:
                return "split" #AA vs ALL
            if player[1] == 'A':
                player = (player[1],player[0])
            if player[1] == '9':
                if dealer in ['7','8','9','10','A']:
                    return "stand" #A9 vs 7-A
                else:
                    return "double" #A9 vs 2-6
            if player[1] == '8':
                if dealer in ['7','8','9','10','A']:
                    return "stand" #A8 vs 7-A
                else:
                    return "double" #A8 vs 2-6
            if player[1] == '7':
                if dealer in ['9','10','A']:
                    return "hit" #A7 vs 9-A
                elif dealer in ['8','7']:
                    return "stand" #A7 vs 7-8
                else:
                    return "double" #A7 vs 2-6
            if player[1] == '6':
                if dealer in ['7','8','9','10','A','2']:
                    return "hit" #A6 vs 7-A // A6 vs 2
                else:
                    return "double" #A6 vs 3-6
            if player[1] == '5':
                if dealer in ['7','8','9','10','A','2','3']:
                    return "hit" #A5 vs 7-A // A5 vs 2-3
                else:
                    return "double" #A5 vs 4-6
            if player[1] == '4':
                if dealer in ['7','8','9','10','A','2','3']:
                    return "hit" #A4 vs 7-A // A4 vs 2-3
                else:
                    return "double" #A4 vs 4-6
            if player[1] == '3':
                if dealer in ['7','8','9','10','A','2','3','4']:
                    return "hit" #A3 vs 7-A // A3 vs 2-4
                else:
                    return "double" #A3 vs 5-6
            if player[1] == '2':
                if dealer in ['7','8','9','10','A','2','3','4']:
                    return "hit" #A2 vs 7-A // A2 vs 2-4
                else:
                    return "double" #A2 vs 5-6
        """ PAIRS """
        if player == ('10','10'):
            return "stand" #TT vs ALL
        if player == ('9','9'):
            if dealer in ['7','10','A']:
                return "stand" #99 vs 10-A // 99 vs 7
            else:
                return "split" #99 vs 8-9 // 99 vs 2-6
        if player == ('8','8'):
            return "split" #88 vs ALL
        if player == ('7','7'):
            if dealer in ['8','9','10','A']:
                return "hit" #77 vs 8-A
            else:
                return "split" #77 vs 2-7
        if player == ('6','6'):
            return "hit" #66 vs ALL
        if player == ('5','5'):
            if dealer in ['10','A']:
                return "hit" #55 vs 10-A
            else:
                return "double" #55 vs 2-9
        if player == ('4','4'):
            if dealer in ['2','3','4','7','8','9','10','A']:
                return "hit" #44 vs 7-A // 44 vs 2-4
            else:
                return "split" #44 vs 5-6
        if player == ('3','3'):
            if dealer in ['8','9','10','A']:
                return "hit" #33 vs 8-A
            else:
                return "split" #33 vs 2-7
        if player == ('2','2'):
            if dealer in ['8','9','10','A']:
                return "hit" #22 vs 8-A
            else:
                return "split" #22 vs 2-7

    """ HARD HANDS """
    if int(player) <= 8:
        return "hit"
    if int(player) == 9:
        if dealer in ['7','8','9','10','A','2']:
            return "hit"
        else:
            return "double"
    if int(player) == 10:
        if dealer in ['2','3','4','5','6','7','8','9']:
            return "double"
        else:
            return "hit"
    if int(player) == 11:
        if dealer in ['2','3','4','5','6','7','8','9','10']:
            return "double"
        else:
            return "hit"
    if int(player) == 12:
        if dealer in ['4','5','6']:
            return "stand"
        else:
            return "hit"
    if int(player) == 13:
        if dealer in ['2','3','4','5','6']:
            return "stand"
        else:
            return "hit"
    if int(player) == 14:
        if dealer in ['2','3','4','5','6']:
            return "stand"
        else:
            return "hit"
    if int(player) == 15:
        if dealer in ['2','3','4','5','6']:
            return "stand"
        else:
            return "hit"
    if int(player) == 16:
        if dealer in ['2','3','4','5','6']:
            return "stand"
        else:
            return "hit"
    if int(player) >= 17:
        return "stand"

    return "How did you fuck this up ??"

def single_round():
    """
    *updates les variables
        decks, balance, min_bet, max_bet, shoe, dead_deck,
    """
    #update shoe (return)
    #update dead_deck (return)
    #update TC
    pass

def init():
    """
    decks, balance, min_bet, max_bet, shoe, dead_deck, TC=0
    """
    pass

def main():
    """
    *init variables (optional)
        decks, balance, min_bet, max_bet, shoe, dead_deck, TC
    *boucle infinie
        single_round
        update_variables
    """
    pass

if __name__ == '__main__':
    main()
