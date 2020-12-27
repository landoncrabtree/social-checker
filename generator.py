import itertools


# Character set (Modify to meet your website's requirements)

# 0-9, a-z
alphabet0 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
            "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# a-z
alphabet1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
            "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# 0,9, a-z, _
alphabet2 = ["_", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
            "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# a-z, _
alphabet3 = ["_", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
            "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# Which alphabet should the generator use?
alphabet = alphabet1

# How many character combinations should you generate?
# ie; 3 would be every 3 character combination.
repeat = 4

# The filename to output to.
filename = "generated.txt"

keywords = [''.join(i) for i in itertools.product(alphabet, repeat=repeat)]
file = open(filename, "w+")
file.close()

for word in keywords:
	file = open(filename, "a")
	file.write(word + "\n")
	file.close()
