import random
import randomizer
import Datamodule
import utility


def gifts():
    rewards = [utility.health, utility.hints ,utility.word_pass]
    pick_reward= random.choice(rewards)

    if pick_reward == utility.health:
        utility.health +=1

    elif pick_reward == utility.hints:
        utility.hints +=1
    else:
        utility.word_pass +=1

print(utility.health)
print(utility.hints)
print(utility.word_pass)

gifts()
print(utility.health)
print(utility.hints)
print(utility.word_pass)


