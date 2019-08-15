
from p042codedtriangle import is_triangle
from p044pentagon import is_pentagonal

above = 40755

def hex_gen():
	n = 0
	while True:
		n += 1
		res = n*(2*n - 1)
		yield res

if __name__ == "__main__":
	for hex_num in hex_gen():
		if is_pentagonal(hex_num) and is_triangle(hex_num) and (hex_num > above):
			print(hex_num)
			break