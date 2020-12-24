import itertools

alphabet = ["_", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
            "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
keywords = [''.join(i) for i in itertools.product(alphabet, repeat=3)]
for word in keywords:
	file = open("3char.txt", "a")
	file.write(word + "\n")
	file.close()