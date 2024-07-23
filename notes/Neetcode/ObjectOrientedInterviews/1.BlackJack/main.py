from enum import Enum
import random
from abc import ABC, abstractmethod

class Suit(Enum):
    CLUBS, DIAMONDS, HEARTS, SPADES = 'clubs', 'diamonds', 'hearts', 'spades'

class Card:

    def __init__(self, suit, value):
        self._suit = suit
        self._value = value

    def getSuit(self):
        return self._suit
    
    def getValue(self):
        return self._value
    
    def print(self):
        print(self.getSuit(), self.getValue())

class Deck:
    def __init__(self):
        self._cards = []
        for suit in Suit:
            for value in range(1, 14):
                self._cards.append(Card(suit, min(value, 10)))

    def print(self):
        for card in self._cards:
            card.print()

    def draw(self):
        return self._cards.pop()
    
    def shuffle(self):
        for i in range(len(self._cards)):
            j = random.randint(0,51)
            self._cards[i], self._cards[j] = self._cards[j], self._cards[i]

class Hand:
    def __init__(self):
        self._score = 0
        self._cards = []

    def addCard(self, card):
        self._cards.append(card)
        if card.getValue() == 1:
            self._score += 11 if self._score + 11 <= 21 else 1
        else:
            self._score += card.getValue()

    def getScore(self):
        return self._score
    
    def getCards(self):
        return self._cards
    
    def print(self):
        for card in self.getCards():
            print(card.getSuit(), card.getValue())

class Player(ABC):
    def __init__(self, hand):
        self._hand = hand

    def getHand(self):
        return self._hand
    
    def clearHand(self):
        self._hand = Hand()

    def addCard(self, card):
        self._hand.addCard(card)

    @abstractmethod
    def makeMove(self):
        pass

class UserPlayer(Player):
    def __init__(self, balance, hand):
        super().__init__(hand)
        self._balance = balance

    def getBalance(self):
        return self._balance
    
    def placeBet(self, amount):
        if amount > self._balance:
            raise ValueError('Insufficient funds')
        self._balance -= amount
        return amount
    
    def receiveWinnings(self, amount):
        self._balance += amount

    def makeMove(self):
        if self.getHand().getScore() > 21:
            return False
        move = input('Draw card? [y/n]: ')
        return move == 'y'
    
class Dealer(Player):
    def __init__(self, hand):
        super().__init__(hand)
        self.targetScore = 17

    def updateTargetScore(self, score):
        self._targetScore = score
    
    def makeMove(self):
        return self.getHand().getScore() < self.targetScore
    
class GameRound:
    def __init__(self, player, dealer, deck):
        self._player = player
        self._dealer = dealer
        self._deck = deck
    
    def getBetUser(self):
        amount = int(input('Enter bet amount: '))
        return amount
    
    def dealInitialCards(self):
        for i in range(2):
            self._player.addCard(self._deck.draw())
            self._dealer.addCard(self._deck.draw())
        print('Player hand: ')
        self._player.getHand().print()
        dealerCard = self._dealer.getHand().getCards()[0]
        print("Dealer's first card: ")
        dealerCard.print()

    def cleanUpRound(self):
        self._player.clearHand()
        self._dealer.clearHand()
        print('Player balance: ', self._player.getBalance())

    def play(self):
        self._deck.shuffle()

        userBet = self.getBetUser()
        self._player.placeBet(userBet)

        self.dealInitialCards()

        # User makes move
        while self._player.makeMove():
            drawnCard = self._deck.draw()
            print('Player draws ')
            drawnCard.print()
            self._player.addCard(drawnCard)
            print('Player score: ', self._player.getHand().getScore())

        if self._player.getHand().getScore() > 21:
            print('Player busts!')
            self.cleanUpRound()
            return
        
        # Dealer makes move
        while self._dealer.makeMove():
            self._dealer.addCard(self._deck.draw())

        if self._dealer.getHand().getScore() > 21:
            print('Player wins')
            self._player.receiveWinnings(userBet*2)
        elif self._dealer.getHand().getScore() > self._player.getHand().getScore():
            print('Player loses')
        else:
            print('Game ends in a draw')
            self._player.receiveWinnings(userBet)
        self.cleanUpRound()
        print('Balance: ', player.getBalance())

player = UserPlayer(balance=1000, hand=Hand())
dealer = Dealer(hand=Hand())

while player.getBalance() > 0:
    gameRound = GameRound(player, dealer, Deck()).play()
