width = 30
height = 30
bell_rings = 50

#probs = [[[0.0 for _ in xrange(y)] for _ in xrange(x)] for _ in xrange(b)]
probs = []
for i in xrange(bell_rings+1):
	probs.append([])
	print("i:{}".format(i))

	for f in xrange(width * height):
		probs[i].append([])

		for x in xrange(width):
			probs[i][f].append([])
			for y in xrange(height):
				if i == 0:
				 	if f == y * width + x:
						probs[i][f][x].append(1.0)
					else:
						probs[i][f][x].append(0.0)
				else:
					prob = 0.0
					last_iter = probs[i-1][f]

					for h, v in [(-1,0), (0,-1), (1,0), (0,1)]:
						if x + h < 0 or y + v < 0: continue
						try:
							divider = 4
							if (x+h) % (width - 1) == 0:
								divider -= 1
							if (y+v) % (height - 1) == 0:
								divider -= 1
							prob += last_iter[x+h][y+v] / divider
						except IndexError:
							pass
					probs[i][f][x].append(prob)

# for f in xrange(height * width):
# 	print([
# 		"{0:.3f}".format(probs[1][f][i / height][i % height]) for i in xrange(width*height)
# 	])

for f in xrange(height*width):
	print("flea {0}".format(f))
	for y in xrange(height):
		print(["{0:.2f}".format(probs[2][f][x][y]) for x in xrange(width)])
#print(probs[0][4])

ev = 0.0
for i in xrange(width):
	for j in xrange(height):
		empty_prob = 1.0
		for f in xrange(width * height):
			empty_prob *= (1 - probs[bell_rings][f][i][j])
		ev += empty_prob

print(ev)







