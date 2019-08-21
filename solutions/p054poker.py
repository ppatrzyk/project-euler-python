
import requests
from collections import Counter

mapping = {
	'T': 10,
	'J': 11,
	'Q': 12,
	'K': 13,
	'A': 14
}

def is_flush(hand):
	res = (len(set(((el['color'] for el in hand)))) == 1)
	return res

def is_straight(hand):
	ranks = sorted([el['rank'] for el in hand])
	straight = list(range(min(ranks), max(ranks)+1))
	res = (ranks == straight)
	return res

def higher_p1(p1, p2):
	for i in range(5):
		if int(p1[i]['rank']) > int(p2[i]['rank']):
			return True
		elif int(p1[i]['rank']) < int(p2[i]['rank']):
			return False
		else:
			continue
	return None

def check_hand(hand):
	"""
	High Card: 0
	One Pair: 100
	Two Pairs: 200
	Three of a Kind: 300
	Straight: 400
	Flush: 500
	Full House: 600
	Four of a Kind: 700
	Straight Flush: 800
	Royal Flush 900
	"""
	current_max = None
	ranks = [el['rank'] for el in hand]
	count = Counter(ranks)
	pair = 0
	three = 0
	four = 0
	pair_val = []
	for key, val in count.items():
		if val == 4:
			four += 1
			card_val = key
			break
		if val == 3:
			three += 1
			card_val = key
		if val == 2:
			pair += 1
			pair_val.append(key)
	if four == 1:
		current_max = 700 + card_val
	if three == 1:
		if pair == 1:
			current_max = 600 + card_val
		else:
			current_max = 300 + card_val
	else:
		if pair == 1:
			current_max = 100 + max(pair_val)
		elif pair == 2:
			current_max = 200 + max(pair_val)
		else:
			current_max = 0
	flush = is_flush(hand)
	straight = is_straight(hand)
	if flush and straight:
		if 14 in ranks:
			return 900
		else:
			return 800 + max(ranks)
	elif flush:
		flush_val = 500 + max(ranks)
		return max([flush_val, current_max])
	elif straight:
		straight_val = 400 + max(ranks)
		return max([straight_val, current_max])
	else:
		return current_max

if __name__ == "__main__":
	counter = 0
	raw_poker = requests.get('https://projecteuler.net/project/resources/p054_poker.txt')
	games = []
	for line in raw_poker.text.split('\n'):
		cards_raw = line.split(' ')
		if len(cards_raw) != 10:
			continue
		cards = [{'rank': str(el[0]), 'color': str(el[1])} for el in cards_raw]
		games.append(cards)
	for cards in games:
		for card in cards:
			if not str(card['rank']).isdigit():
				original_rank = card.pop('rank')
				coded_rank = mapping.get(original_rank)
				card['rank'] = coded_rank
			else:
				card['rank'] = int(card['rank'])
		p1 = sorted(cards[:5], key=lambda c: c['rank'], reverse=True)
		p2 = sorted(cards[5:], key=lambda c: c['rank'], reverse=True)
		p1_score = check_hand(p1)
		p2_score = check_hand(p2)
		if p1_score > p2_score:
			counter += 1
		elif p1_score == p2_score:
			if higher_p1(p1, p2):
				counter += 1
		else:
			continue
	print(counter)
		
