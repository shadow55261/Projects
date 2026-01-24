import random
import os
import time
def art_ascii():
    print("""
    
 _     _            _    _            _       _   _
| |   | |          | |  (_)          | |     / \_/ \
| |__ | | __ _  ___| | ___  __ _  ___| | __  |     |
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /   \   /
| |_) | | (_| | (__|   <| | (_| | (__|   <     \_/
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\ 
                       _/ |                
                      |__/   
    """)
def clear():
    os.system("cls" if os.name == "nt"else"clear")
def draw_card():
    """ترد رقم عشوائي"""
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10,]
    card=random.choice(cards)
    return card

def counting_cards(cards):
    """تحقق أذ كان فوز بلاك جاك و أستبدال رقم 11 بي 1 بحالة تعدى 21"""
    if sum(cards)==21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare_result(player_result, computer_result):

    results={
        "draw": "Player and computer tie😊\n\n",
        "player skipped 21": "Sorry I lost, skip 21😔\n\n",
        "skip computer 21": "I won the computer skip 21⭐\n\n",
        "blackjack_player":"Congratulations, you have won blackjack🔥👌😎\n\n",
        "computer_blackjack": "Sorry I lost to blackjack😰",
        "won": "Blessed he won🌟\n\n",
        "loss":"Sorry I lost😢\n\n"
    }
    if player_result == computer_result:
        return results["draw"]
    elif player_result > 21:
        return results["player skipped 21"]
    elif computer_result > 21:
        return results["skip computer 21"]
    elif  player_result == 0:
        return results["blackjack_player"]
    elif computer_result == 0:
        return results["computer_blackjack"]
    elif player_result > computer_result:
        return results["won"]
    else:
        return results["loss"]
def game():
    clear()
    print("Wait a bit the game is being prepared...")
    time.sleep(3)
    art_ascii() 
    player=[draw_card() for _ in range(2)]
    delray=[draw_card() for _ in range(2)]
    stop_or_continue = True
    while stop_or_continue:
        player_scope = counting_cards(player)
        computer_scope = counting_cards(delray)
        print(f"\n\nPlayer cards {player} Total cards {sum(player)}")
        print(f"The first card for the computer {delray[0]}")
        if player_scope == 0 or computer_scope == 0 or player_scope  > 21 or computer_scope > 21:
            stop_or_continue=False
        else: 
            answer=input("\n\nDo you want to withdraw another card? (y/n) ").lower()
            if answer == "y":
                player.append(draw_card())
            else:
                stop_or_continue = False

    while computer_scope != 0 and computer_scope < 17:
        delray.append(draw_card())
        computer_scope = counting_cards(delray)
    print(f"\n\nPlayer cards {player} Total cards {sum(player)}")
    print(f"The first card for the computer {delray} Total computer {sum(delray)}")
    print(compare_result(player_scope, computer_scope))
while input("Choose a game to start..... \n\n1-Froggy\n2-Twenty one \n3-Snake\n\n-------\n\n").lower() == "twenty one":
    game()

        
     


    
    
