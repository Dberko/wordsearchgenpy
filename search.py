import random
import string

width = 12
height = 12


def put_word(word, grid):
	word = random.choice([word, word[::-1]])

	d = random.choice([[1, 0], [0, 1], [1, 1]])
	xs = width if d[0] == 0 else width   - len(word)
	ys = height if d[1] == 0 else height - len(word)

	x = random.randrange(0, xs)
	y = random.randrange(0, ys)

	print [x, y]

	for i in xrange(0, len(word)):
		grid[y + d[1] * i][x + d[0] * 1] = word[i]

	return grid

grid = [[random.choice(string.uppercase) for i in xrange(0, width)] for j in xrange(0, height)]

for word in ["TEST", "DOCTOR", "WHO"]:
	grid = put_word(word, grid)

print "\n".join(map(lambda row: " ".join(row), grid))
