
START = 1901
END = 2000
first_date = (1900, 1, 0) 
# y, m, weekday offset (0 is monday, 6 sunday)

def is_leap(year):
	if year == 1900:
		return False
	leap = not (year % 4)
	return leap

month_len = {
	1: 31,
	3: 31,
	4: 30,
	5: 31,
	6: 30,
	7: 31,
	8: 31,
	9: 30,
	10: 31,
	11: 30,
	12: 31,
}

def move_month(state):
	year = state[0]
	month = state[1]
	offset = state[2]
	if month == 2:
		if is_leap(year):
			length = 29
		else:
			length = 28
	else:
		length = month_len.get(month)
	offset += (length % 7)
	offset = (offset % 7)
	if month == 12:
		return (year+1, 1, offset)
	else:
		return (year, month+1, offset)

if __name__ == "__main__":
	sundays = 0
	state = first_date
	while True:
		state = move_month(state)
		if state[0] > END:
			break
		if state[0] >= START and (state[2] == 6):
			sundays += 1
	print(sundays)
