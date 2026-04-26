import utility
import random
import Datamodule

# eto gawa nya na list then iterate nya ung bawat letter tapos ung join para combine
def scramble(w):
    letters = list(w)
    random.shuffle(letters)
    return ''.join(letters)

# Rarity system
# Common (Health) = 60% chance
# Rare (Hints) = 30% chance  
# Epic (Word Pass) = 10% chance
RARITY_CHANCES = {
    "health": 60,      # COMMON
    "hints": 30,       # RARE
    "word_pass": 10    # EPIC
}

def get_reward_by_rarity():
    """Select reward based on rarity percentages using random number"""
    roll = random.randint(1, 100)
    
    if roll <= 60:  # 60% chance to un ung rarity nya
        return "health"
    elif roll <= 90:  # dto 30 percent ata
        return "hints"
    else:  # tas eto sure ako 10 percent
        return "word_pass"

#gift
def gifts():
    # mga gifts lang to naka def pra madali tawagin
    reward_type = get_reward_by_rarity()
    
    if reward_type == "health":
        utility.health += 1
        reward_value = 1
        # Common reward message
        print(f"REWARD: COMMON +1 Health!")

    elif reward_type == "hints":
        utility.hints += 1
        reward_value = 1
        # Rare reward message
        print(f"REWARD: RARE! +1 Hint!")
        
    elif reward_type == "word_pass":
        utility.word_pass += 1
        reward_value = 1
        
        print(f"REWARD: 🌟🌟🌟 EPIC 🌟🌟🌟 +1 Word Pass!")
    
    return reward_type, reward_value

def reward():
    reward_type, reward_value = gifts()

# Function to get a random quote (called when game starts)
def get_random_quote():
    """Returns a random quote from mode2"""
    chosen = random.choice(Datamodule.mode2)
    words = chosen["words"]
    quote = chosen["quote"]
    scrambled_words = [scramble(words[0]), scramble(words[1]), scramble(words[2]), scramble(words[3])]
    return chosen, words, quote, scrambled_words