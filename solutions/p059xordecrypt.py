
import itertools
import requests
import re
import string

ciper_address = 'https://projecteuler.net/project/resources/p059_cipher.txt'

keys_raw = itertools.product(string.ascii_lowercase, repeat = 3)
possible_keys = (tuple(ord(letter) for letter in key) for key in keys_raw)

def get_text(val_list):
	res = ''.join([chr(el) for el in val_list])
	return res

def decrypt(val_list, key):
	message_len = len(val_list)
	key_cycle = []
	for i, letter in enumerate(itertools.cycle(key), start=1):
		key_cycle.append(letter)
		if i == message_len:
			break
	res = [el^key for el, key in zip(val_list, key_cycle)]
	return res

if __name__ == "__main__":
	raw_cipher = requests.get(ciper_address)
	cipher = [int(el) for el in raw_cipher.text.split(',')]
	for key in possible_keys:
		xored = decrypt(cipher, key)
		decrypted_text = get_text(xored)
		if re.search('have', decrypted_text, re.IGNORECASE):
			# print(decrypted_text)
			result = sum(xored)
			print(result)
			break