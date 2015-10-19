import random
import string
width = 12
height = 12

grid = [random.choice(string.uppercase) for i in xrange(0, width)] for j in xrange(0, height)
print grid