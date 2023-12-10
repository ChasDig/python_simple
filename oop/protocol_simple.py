from collections import namedtuple
from random import shuffle


Card = namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    """
            Класс реализует базовые методы Протокола Последовательности:
        - __getitem__ и __len__.
    """
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __getitem__(self, item):
        return self._cards[item]

    def __len__(self):
        return len(self._cards)


#  Благодаря Протоколу Последовательности, класс FrenchDeck имеет возможность реализовывать соответствующие методы:
dec_1 = FrenchDeck()
print(dec_1[0])
print(dec_1[:len(dec_1) - 1])
print(dec_1[:-1])


# -------- #
# Проблематика: Последовательность FrenchDeck неизменяемая. Для реализации изменяемости, реализуем __setitem__
# (в нашем случае, динамически). Пример - реализация monkey patching:
def set_card(deck: FrenchDeck, position, card):
    deck._cards[position] = card


FrenchDeck.__setitem__ = set_card
# Благодаря данной реализации появилась возможность "перетасовки" колоды карт (IDE может ругаться):
print(dec_1[:3])
# Стоит учитывать, что данный пример реализует понятие "Динамического протокола", т.к. методу shuffle не столь
# принципиально какие методы реализованы в передаваемом объекте. Главное - наличие определенных магических методов!
shuffle(dec_1)
print(dec_1[:3])

# -------- #
#  Пример реализации Быстрого Отказа (актуально при работе с сырыми данными):
q = "Din,Sam,David"
a = ("Din", "Sam", "David")
try:
    w = q.replace(',', ' ').split(' ')
    print(w)
except AttributeError:
    pass
print("other operations")


# -------- #
#  Sized распознает MySized как свой подкласс, т.к. в нем правильно и при правильных условиях(!) реализованы магические
#  методы:
from collections.abc import Sized


class MySized:

    def __len__(self):
        return len(self)


print(issubclass(MySized, Sized))
