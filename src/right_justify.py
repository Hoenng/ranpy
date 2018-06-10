#!/usr/local/bin/python3

def right_justify(aword):
	num_space = 70 - len(aword)

	print(' ' * num_space + aword)
    
right_justify('juice')
right_justify('averybigword')	