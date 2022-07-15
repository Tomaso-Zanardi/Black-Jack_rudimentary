# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 16:04:46 2022

@author: Utente
"""


import random as rn
from random import shuffle as shf
import time

import sys

suits = ['♠', '♥', '♦', '♣']
cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
cards_values = {"A": 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}

##############################################################################
def deck(suits, cards, cards_values):
    
    """
    This function generates and returns a deck of cards given a list of suits,
    a list of cards for each suits, and a dictionary of values for each card.
    
    """
    
    deck = []
    for suit in suits:
        for card in cards:
            deck.append([suit, card, cards_values[card]])
    return deck
############################################################################## 

##############################################################################
def pointIncrement(partecipant_cards):
    """
    This function is used to calculate the value of the hand of one of the players


    Parameters
    ----------
    partecipant_cards : it is a list of lists, where the formers are individual cards.

    Returns
    -------
    partecipantTotalPoints : integer
        it is the total points corresponding to the sum of all the cards individual values

    """
    
    partecipantTotalPoints = 0
    pp = 0

    # these loops increment the values of players' hands

    for tk in partecipant_cards:
    
        partecipantTotalPoints = partecipantTotalPoints + (partecipant_cards[pp])[2]
        pp = pp + 1
        
    return partecipantTotalPoints
##############################################################################


##############################################################################
def dealerForcedChoice(dealer_points, dealer_hand, dk):
    """
    

    Parameters
    ----------
    dealer_points : integer
        is the dealer total points.
    dealer_hand : list of lists
        is the dealer's cards.
    dk : list of lists
        is the deck of cards.

    Returns
    -------
    dealer_points :same as the above (but updated after the forced choices the dealer has to make).
        same as the above (but updated after the forced choices the dealer has to make).
    dealer_hand :same as the above (but updated after the forced choices the dealer has to make).
        same as the above (but updated after the forced choices the dealer has to make).

    """
    while dealer_points < 17:
        dealer_hand.append(dk.pop())
        print("dealer's hand : [ %s ]" % dealer_hand)
        dealer_points = pointIncrement(dealer_hand)
    return dealer_points, dealer_hand
##############################################################################


##############################################################################
def deal(dk,playerhand):
    """
    This function deals one card

    Parameters
    ----------
    dk : list of lists
        DESCRIPTION.
    playerhand : list of lists
        DESCRIPTION.

    Returns
    -------
    playerhand : list of lists
        DESCRIPTION.

    """
    playerhand.append(dk.pop())
    return playerhand
##############################################################################

##############################################################################
def ace(hand):
    """
    this function checks for aces and update the value from 11 to 1

    Parameters
    ----------
    hand : list of list
        it is a list of lists. the formers are the player's cards.

    Returns
    -------
    hand :same as the above (but updated after the forced choices the dealer has to make).
        same as the above (but updated after the forced choices the dealer has to make).

    """
    
    c = 0
    while c < len(hand):
        if hand[c][2] == 11:
            hand[c][2] = 1
            c += 1
        else:
            c+= 1
    return hand
##############################################################################



if __name__ == '__main__':
    mazzo = deck(suits, cards, cards_values)

# print(type(mazzo[1]))
# here I check that the object mazzo (italian for 'deck' is a list of tuples)



## here is the game part of the program

    player_cards = []
    dealer_cards = []

    rn.shuffle(mazzo)
    rn.shuffle(mazzo)
    rn.shuffle(mazzo)

    c = 0


# this section of the program deals the first 2 cards to the player and the dealer

    while len(player_cards) < 2 and len(dealer_cards) < 2:
        deal(mazzo,player_cards)
        deal(mazzo, dealer_cards)
        c = c + 1
        time.sleep(2)
        if c < 2:
            print("dealer's hand: [?] ")
            print("player's hand : %s" % player_cards)
            print("/---------------------------------------/")
            print("/---------------------------------------/")

        else:
            print("dealer's hand:[?] [ {} ]".format(dealer_cards[1]))
            print("player's hand : [ %s ]" % player_cards)
        

# these variables keep track of the dealer's and player's hands and assign values to some counter needed to increment the points of the players




    playerTotalPoints = pointIncrement(player_cards)
    dealerTotalPoints = pointIncrement(dealer_cards)

# the following if statements assign a value of 1 to 1 ace in case one player has a couple of aces in the first deal
    if dealer_cards[0][1] == 'A' and dealer_cards[1][1] == 'A':
        dealer_cards[1][2] = 1

    if player_cards[0][1] == 'A' and player_cards[1][1] == 'A':
        player_cards[1][2] = 1
# these if statements check for black jacks out of the bat

    if playerTotalPoints == 21:
        print("BLACKJACK!!!")


    pChoice = ''
    while playerTotalPoints < 21:
        pChoice = input(" do you hit or do you stay? (h/s) ")
        if pChoice == 'h' or pChoice == 'hit':
            deal(mazzo, player_cards)
            print("player's hand : [ %s ]" % player_cards)
            playerTotalPoints = pointIncrement(player_cards)
        else:
            break
        if playerTotalPoints > 21:
            ace(player_cards)
            pointIncrement(player_cards)
            if playerTotalPoints > 21:
                break
        

    if playerTotalPoints > 21:
        print("you went over 21, you lose!")
    elif playerTotalPoints == 21:
        print('it-s a blackjack, you won!')
    elif playerTotalPoints < 21:
        dealerForcedChoice(dealerTotalPoints, dealer_cards, mazzo)
        pointIncrement(dealer_cards)
    
    print("player's hand : %s" % player_cards)
    print("")
    print("/---------------------------------------/")
    print("/---------------------------------------/")
    print("")
    print('player total points: '+str(playerTotalPoints))
    print('dealer total points: '+str(dealerTotalPoints))


    if playerTotalPoints > 21:
        sys.exit()
    elif dealerTotalPoints > playerTotalPoints:
        print("dealers wins!")
    elif dealerTotalPoints < playerTotalPoints:
        print("players wins!")
    elif dealerTotalPoints == playerTotalPoints:
        print("it's a draw!")
