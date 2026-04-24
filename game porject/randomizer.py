
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

w1 = scramble(words[0])
w2 = scramble(words[1])
w3 = scramble(words[2])
w4 = scramble(words[3])


    