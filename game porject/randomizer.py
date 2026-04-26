import random
import Datamodule

def scramble(w):
    letters = list(w)
    random.shuffle(letters)
    return ''.join(letters)

# Pick random quote
chosen = random.choice(Datamodule.level3)
words = chosen["words"]
quote = chosen["quote"]

scrambled_words = [scramble(words[0]), scramble(words[1]), scramble(words[2]), scramble(words[3])]
w1 = scrambled_words[0]
w2 = scrambled_words[1]
w3 = scrambled_words[2]
w4 = scrambled_words[3]