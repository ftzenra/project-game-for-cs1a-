import utility
import random
import Datamodule

# eto gawa nya na list then iterarte nya ung bawat letter tapos ung join para combine
def scramble(w):
    letters = list(w)
    random.shuffle(letters)
    return ''.join(letters)

# Pick random quote
chosen = random.choice(Datamodule.mode2)
words = chosen["words"]
quote = chosen["quote"]

# eto ung iteration ng bawat letter 
scrambled_words = [scramble(words[0]), scramble(words[1]), scramble(words[2]), scramble(words[3])]
w1 = scrambled_words[0]
w2 = scrambled_words[1]
w3 = scrambled_words[2]
w4 = scrambled_words[3]

#gift to basta yun
def gifts():
    rewards = [utility.health, utility.hints, utility.word_pass]
    pick_reward = random.choice(rewards)
    
    if pick_reward == utility.health:
        utility.health += 1
        reward_type = "health"
    elif pick_reward == utility.hints:
        utility.hints += 1
        reward_type = "hints"
    elif pick_reward == utility.word_pass:
        utility.word_pass += 1
        reward_type = "word_pass"
    
    return reward_type, pick_reward
reward_type, reward_value = gifts()







