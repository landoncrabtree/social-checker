import itertools

# Character set (Modify to meet your website's requirements)
alphabet = ["_", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
            "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# How many character combinations should you generate?
# ie; 3 would be every 3 character combination.
repeat = 3

# The filename to output to.
filename = "generated.txt"

keywords = [''.join(i) for i in itertools.product(alphabet, repeat=repeat)]
for word in keywords:
	file = open(filename, "w+")
	file.write(word + "\n")
	file.close()
