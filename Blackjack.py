
import random

#Variables
player_dealt = []
player_total = 0
dealer_dealt = []
dealer_total = 0

#Written by Bernie
def find_total(cards):
  total = 0
  for x in cards:
    card = x.split()
    if card[0] != 'J' and card[0] !='Q' and card[0] != 'K' and card[0] != 'A':
      total += int(card[0])
    else:
      if card[0] == 'J'or card[0] == 'Q' or card[0] == 'K':
        total += 10
      elif card[0] == 'A':
        if total < 11:
          total += 11
        else:
          total += 1
  return total
  
#Written by Henry
def random_card():
  suites = ["S", "H", "C", "D"]
  card = []
  card_temp = str(random.randint(1, 13))
  if card_temp == '11':
    card.append('J')
  elif card_temp == '12':
    card.append('Q')
  elif card_temp == '13':
    card.append('K')
  elif card_temp == '1':
    card.append('A')
  else:
    card.append(card_temp)
  card.append(random.choice(suites))
  return " ".join(card)
  
#Written by Henry
def deal_card(player):
  card = random_card()
  if card not in player:
    player.append(card)
  else:
    deal_card(player)

#Written by Bernie
def show_score():
  print("Your cards are " + str(player_dealt))
  print("The dealer's cards are " + str(dealer_dealt))
  print("Your score is " + str(player_total))
  print("The dealer's total is " + str(dealer_total))
  
#Written by Bernie
def dealer_deals():
  global dealer_total
  while True:
    if dealer_total == player_total:
      print("Draw, both players had a score of " + str(player_total))
      break
    elif dealer_total > 21:
      print("You win, as your score is " + str(player_total) + " and the dealers score is " + str(dealer_total))
      break
    elif dealer_total > player_total:
      print("You lost, as your score is " + str(player_total) + " and the dealers score is " + str(dealer_total))
      break
    else:
      deal_card(dealer_dealt)
      dealer_total = find_total(dealer_dealt)
      show_score()
      
#Main Game loop
#Written by Henry
def game():
  global player_total
  global dealer_total
  for i in range(2):
    deal_card(player_dealt)
    deal_card(dealer_dealt)
  while True:
    player_total = find_total(player_dealt)
    dealer_total = find_total(dealer_dealt)
    show_score()
    if dealer_total == 21:
      print("You lost, as your score is " + str(player_total) + " and the dealers score is " + str(dealer_total))
      break
    elif player_total == 21:
      print("Blackjack! You won!")
      break
    elif player_total > 21:
      print("You lost, as your score is " + str(player_total) + ", which is over 21")
      break
    print("Hit or stand?")
    decision = input()
    if decision == "Hit":
      deal_card(player_dealt)
    elif decision == "Stand":
      print("Your score is " + str(player_total))
      dealer_deals()
      break
    else:
      print("Please either 'Hit' or 'Stand'")

game()


