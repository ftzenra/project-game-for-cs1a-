import Datamodule
import random
import utilitty
# Parent Class
class GameMode:
    def __init__(self, words_list, health=3):
        self.words = words_list
        self.health = health
        self.score = 0
        self.current_index = 0
        self.hints = 2
        self.word_passes = 1
        self.revealed_count = 0
        self.correct_words = [False] * len(words_list)
        
    def scramble_word(self, word):
        letters = list(word)
        random.shuffle(letters)
        return ''.join(letters)
    
    def display_message(self):
        pass
    
    def check_answer(self, user_answer):
        return user_answer == self.words[self.current_index]
    
    def next_word(self):
        self.current_index += 1
    
    def is_complete(self):
        return self.current_index >= len(self.words)
    
    def show_hint(self, current_word):
        if self.hints > 0:
            self.hints -= 1
            self.revealed_count += 1
            hint_display = list("_" * len(current_word))
            for i in range(min(self.revealed_count, len(current_word))):
                hint_display[i] = current_word[i]
            return ' '.join(hint_display)
        return None
    
    def give_reward(self):
        rewards = ["health", "hints", "word_pass"]
        reward = random.choice(rewards)
        
        if reward == "health":
            self.health += 1
        elif reward == "hints":
            self.hints += 1
        else:
            self.word_passes += 1
        
        return reward


# Easy Mode Child Class
class EasyMode(GameMode):
    def __init__(self):
        words_list = D
        super().__init__(words_list, health=5)
    
    def display_message(self):
        return "🎮 EASY MODE - 5 Health 🎮"


# Medium Mode Child Class
class MediumMode(GameMode):
    def __init__(self):
        words_list = ["square", "guitar", "beauty", "emerge", "adjust"]
        super().__init__(words_list, health=3)
    
    def scramble_word(self, word):
        letters = list(word[::-1])
        random.shuffle(letters)
        return ''.join(letters)
    
    def display_message(self):
        return "⚡ MEDIUM MODE - 3 Health ⚡"


# Hard Mode Child Class
class HardMode(GameMode):
    def __init__(self):
        words_list = ["boundary", "heritage", "decorate", "marriage", "explicit"]
        super().__init__(words_list, health=2)
    
    def scramble_word(self, word):
        letters = list(word)
        if len(letters) > 1:
            letters[0], letters[-1] = letters[-1], letters[0]
        random.shuffle(letters)
        return ''.join(letters)
    
    def display_message(self):
        return "🔥 HARD MODE - 2 Health 🔥"


# Quote Mode Child Class
class QuoteMode(GameMode):
    def __init__(self):
        quote_data = random.choice(Datamodule.mode2)
        words_list = quote_data["words"]
        self.quote = quote_data["quote"]
        super().__init__(words_list, health=4)
        self.hints = 3
        self.word_passes = 2
    
    def display_message(self):
        return f"📖 QUOTE MODE - Build the hidden quote! 📖"
    
    def get_quote(self):
        return self.quote