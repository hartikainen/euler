from __future__ import print_function
import functools

FILEPATH = "./data/p054_poker.txt"

@functools.total_ordering
class Card(object):
  RANKS = [
    '2', '3', '4', '5', '6', '7', '8', '9',
    'T', 'J', 'Q', 'K', 'A'
  ]

  def __init__(self, card):
    #print("card: {}, type(card): {}".format(card, type(card)))
    self.value = Card.RANKS.index(card[0])
    self.color = card[1]

  def get_char_value(self):
    return Card.RANKS[self.value]

  def char_exists(self, c):
    self_c = self.get_char_value()
    return self_c == c

  def __lt__(self, other):
    return self.value < other.value

  def __eq__(self, other):
    return self.value == other.value

  def __repr__(self):
    return "{}{}".format(self.value, self.color)


@functools.total_ordering
class Hand():
  RANKS = [
    "high card",
    "one pair",
    "two pairs",
    "three of a kind",
    "straight",
    "flush",
    "full house",
    "four of a kind",
    "straight flush",
    "royal flush",
  ]
# High Card: Highest value card.
# One Pair: Two cards of the same value.
# Two Pairs: Two different pairs.
# Three of a Kind: Three cards of the same value.
# Straight: All cards are consecutive values.
# Flush: All cards of the same suit.
# Full House: Three of a kind and a pair.
# Four of a Kind: Four cards of the same value.
# Straight Flush: All cards are consecutive values of same suit.
# Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
  def __init__(self, card_strings):
    self.cards = [
      Card(c) for c in card_strings
    ]

    # print("creating hand: {}".format([str(c) for c in self.cards]))

    self.ranks = self.parse_rank()

  def parse_rank(self):
    values, colors = zip(*[[c.value, c.color] for c in self.cards])
    distinct_values = list(set(values))
    distinct_colors = list(set(colors))

    flush = len(distinct_colors) == 1
    # print("values: {}".format(values))
    num_kinds = [
      sum([v == d for v in values])
      for d in distinct_values
    ]
    # if highest_kinds > 2:
    #   print("highest kinds: {}".format(highest_kinds))

    values = sorted(values, reverse=True)
    diffs = [values[i-1] - values[i] for i in xrange(1, len(values))]

    if any(c.char_exists('A') for c in self.cards):
      straight = ((0 in values and
                   1 in values and
                   2 in values and
                   3 in values) or
                  (8 in values and
                   9 in values and
                   10 in values and
                   11 in values))
    else:
      straight = all(diff == 1 for diff in diffs)

    RANKS = Hand.RANKS
    if straight and flush:
      king_exists = any(c.char_exists('K') for c in self.cards)
      ace_exists = any(c.char_exists('A') for c in self.cards)

      if ace_exists and king_exists:
        rank = RANKS.index('royal flush')
        return {rank: values}
      else:
        rank = RANKS.index('straight flush')
        if ace_exists:
          values.remove(12)
          values.append(-1)
        return {rank: values}

    if 4 in num_kinds:
      rank = RANKS.index('four of a kind')
      value_of_4s = distinct_values[num_kinds.index(4)]
      return {
        rank: [value_of_fours],
        RANKS.index('high card'): filter(
          lambda x: x != value_of_4s, values)
      }

    if 3 in num_kinds and 2 in num_kinds:
      rank = RANKS.index('full house')
      value_of_3s = distinct_values[num_kinds.index(3)]
      value_of_2s = distinct_values[num_kinds.index(2)]
      return {
        rank: [value_of_3s, value_of_2s]
      }
    if flush:
      rank = RANKS.index('flush')
      return { rank: values }
    if straight:
      rank = RANKS.index('straight')
      king_exists = any(c.char_exists('K') for c in self.cards)
      ace_exists = any(c.char_exists('A') for c in self.cards)

      if ace_exists and not king_exists:
        values.remove(12)
        values.append(-1)
      return { rank: values }
    if 3 in num_kinds:
      rank = RANKS.index('three of a kind')
      value_of_3s = distinct_values[num_kinds.index(3)]
      values = filter(lambda x: x != value_of_3s, values)
      return {
        rank: [value_of_3s],
        RANKS.index('high card'): values
      }
    if num_kinds.count(2) == 2:
      rank = RANKS.index('two pairs')
      value_of_1st_2s = distinct_values[num_kinds.index(2)]
      values = filter(
          lambda x: x != value_of_1st_2s, values)
      distinct_values.remove(value_of_1st_2s)

      num_kinds = [
        sum([v == d for v in values])
        for d in distinct_values
      ]
      value_of_2nd_2s = distinct_values[num_kinds.index(2)]
      values = filter(
          lambda x: x != value_of_2nd_2s, values)
      return {
        rank: [value_of_1st_2s, value_of_2nd_2s],
        RANKS.index('high card'): values
      }
    if 2 in num_kinds:
      rank = RANKS.index('one pair')
      value_of_2s = distinct_values[num_kinds.index(2)]
      values = filter(lambda x: x != value_of_2s, values)
      return {
        rank: [value_of_2s],
        RANKS.index('high card'): values
      }
    return {RANKS.index('high card'): values}

  def high_card(self):
    return max(c.value for card in self.cards)

  def __lt__(self, other):
    own_ranks = sorted(self.ranks.keys(), reverse=True)
    other_ranks = sorted(other.ranks.keys(), reverse=True)
    for i in xrange(len(own_ranks)):
      # if i >= len(other_ranks): return False
      if own_ranks[i] == other_ranks[i]:
        own_values = sorted(self.ranks[own_ranks[i]], reverse=True)
        other_values = sorted(other.ranks[other_ranks[i]], reverse=True)
        # print("got tie: {} ({}) vs. {} ({})!".format(own_ranks[i], own_values, other_ranks[i], other_values), end="")
        for j in xrange(len(own_values)):
          # if j >= len(other_values): return False
          if own_values[j] == other_values[j]:
            print("got tie({}): {} vs {}, ranks: {} vs {}, values: {} vs {}".format(
              Hand.RANKS[own_ranks[i]], self, other, own_ranks, other_ranks, own_values, other_values))
            print("j={}, own_values[j]={}, other_values[j]={}".format(j, own_values[j], other_values[j]))
          else:
            return own_values[j] < other_values[j]
          # return own_values[i] < other_values[i]
      else:
        return own_ranks[i] < other_ranks[i]
    return False

  def __eq__(self, other):
    own_ranks = sorted(self.ranks.keys(), reverse=True)
    other_ranks = sorted(other.ranks.keys(), reverse=True)
    max_len_i = max(len(own_ranks), len(other_ranks))

    for i in xrange(max_len_i):
      if own_ranks[i] == other_ranks[i]:
        own_values = sorted(self.ranks[own_ranks[i]], reverse=True)
        other_values = sorted(other.ranks[other_ranks[i]], reverse=True)
        max_len_j = max(len(own_values), len(other_values))
        for j in xrange(max_len_j):
          if own_values[j] == other_values[j]: continue
          return False
        continue
      else:
        return False
    if len(own_ranks) == len(other_ranks):
      if all(len(self.ranks[i]) == len(other.ranks[i]) for i in own_ranks):
        return True
    return False

  def __repr__(self):
    return str(self.cards)

def compare_hands(h1, h2):
  # print("comparing hands: {} and hand2: {}".format(h1, h2))
  if h1 > h2:
    return 0
  elif h1 < h2:
    return 1
  else:
    return None
  return None

def poker_hands(filepath):
  wins = [0, 0]
  with open(filepath) as f:

    for line in f:
      cards = line.strip().split(" ")
      hand1 = Hand(cards[:5])
      hand2 = Hand(cards[5:])
      winner = compare_hands(hand1, hand2)
      if winner is not None:
        wins[winner] += 1

      h1_ranks = sorted(hand1.ranks.keys(), reverse=True)
      h2_ranks = sorted(hand2.ranks.keys(), reverse=True)
      print("winner: {}".format(winner))
      # if (h1_ranks[0] == 0 and h2_ranks[0] == 0):
      #   raw_input("{} vs {} winner {} ({} vs {})\n".format(
      #           hand1, hand2, winner,
      #           Hand.RANKS[h1_ranks[0]], Hand.RANKS[h2_ranks[0]])
      #   )
      # raw_input("{} vs. {}, winner {}".format(hand1, hand2, winner))

  return wins

print(poker_hands(FILEPATH))
