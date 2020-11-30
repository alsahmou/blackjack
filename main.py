############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import random 
import art
cards = [11, 2, 3, 4, 5 , 6, 7, 8, 9, 10, 10, 10, 10]

def deal(deal, cards=cards):
  return random.choice(cards)

def score(deal):
  score = 0
  for card in deal:
    score += card
  if score == 21 and len(deal) == 2:
    return 0
  if 11 in deal and score > 21:
    score -= 10
  return score

user_score = 0
comp_score = 0

choice = input('Do you want to play a game of Blackjack? Type: \'Y\' or \'N\'').lower()
while user_score < 22:
  user_deal = []
  comp_deal = []
  
  if choice == 'y':
    print(art.logo)
    user_deal.append(deal(user_deal))
    user_deal.append(deal(user_deal))
    comp_deal.append(deal(comp_deal))
    comp_deal.append(deal(comp_deal))
    user_score = score(user_deal)
    comp_score = score(comp_deal)
    print(f'Your cards: {user_deal}, current score is: {user_score}')
    print(f'Computer\'s first card: {comp_deal[0]}')
    if user_score == 0:
      print('Blackjack!')
      break
    if comp_score == 0:
      print('Comp Blackjack!')
      break
    keep_playing = input('Do you to get another card?').lower()
    if keep_playing == 'y':
      user_deal.append(deal(user_deal))
      comp_deal.append(deal(comp_deal))
      user_score = score(user_deal)
      comp_score = score(comp_deal)
      print(f'Your final hand: {user_deal}, final score is: {user_score}')
      print(f'Computer\'s final hand: {comp_deal}, computer\'s final score is: {comp_score}')
      break
if user_score > 22:
  print('You went over. You lose!')
else:
  if user_score > comp_score:
    print('You win!')
  elif comp_score > user_score:
    print('You lose!')
  else:
    print('It is a draw!')