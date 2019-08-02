
single = {
	0: '',
	1: 'one',
	2: 'two',
	3: 'three',
	4: 'four',
	5: 'five',
	6: 'six',
	7: 'seven',
	8: 'eight',
	9: 'nine'
}

teen = {
	0: 'ten',
	1: 'eleven',
	2: 'twelve',
	3: 'thriteen',
	4: 'fourteen',
	5: 'fifteen',
	6: 'sixteen',
	7: 'seventeen',
	8: 'eighteen',
	9: 'nineteen'
}

second = {
	0: '',
	# 1 separate case
	2: 'twenty',
	3: 'thirty',
	4: 'forty',
	5: 'fifty',
	6: 'sixty',
	7: 'seventy',
	8: 'eighty',
	9: 'ninety'
}

if __name__ == "__main__":
	total_len = 0
	for number in range(1, 1000, 1):
		encoded = ''
		number_len = len(str(number))
		digits = [0 for _ in range(3-number_len)]
		digits.extend([int(el) for el in list(str(number))])

		if digits[0] != 0:
			encoded += f'{single.get(digits[0])}hundred'
			if not (digits[1] == 0 and digits[2] == 0):
				encoded += 'and'

		if digits[1] == 1:
			encoded += f'{teen.get(digits[2])}'
		else:
			encoded += f'{second.get(digits[1])}'
			encoded += f'{single.get(digits[2])}'
		
		encoded_len = len(encoded)
		total_len += encoded_len
	total_len += len('onethousand')
	print(total_len)
