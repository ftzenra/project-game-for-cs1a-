import random
import utility
import randomizer
import Datamodule

# Parent Class
class GameMode:
    def __init__(self, health=3):
        self.health = health
        self.score = 0
        self.hints = utility.hints
        self.word_passes = utility.word_pass
        self.revealed_count = 0
        
    def scramble_word(self, word):
        """Use randomizer's scramble function"""
        return randomizer.scramble(word)
    
    def check_answer(self, user_answer, correct_word):
        return user_answer == correct_word
    
    def show_hint(self, current_word):
        if self.hints > 0:
            self.hints -= 1
            utility.hints = self.hints
            self.revealed_count += 1
            hint_display = list("_" * len(current_word))
            for i in range(min(self.revealed_count, len(current_word))):
                hint_display[i] = current_word[i]
            return ' '.join(hint_display)
        return None
    
    def give_reward(self):
        """Use randomizer's gift system"""
        reward_type, reward_value = randomizer.gifts()
        
        if reward_type == "health":
            self.health += 1
            utility.health = self.health
        elif reward_type == "hints":
            self.hints +=1
            utility.hints = 1
        elif reward_type == "word_pass":
            self.word_passes +=1
            utility.word_pass = self.word_passes
        
        return f"{reward_type} = +1"


# Mode 1: per level pero tawag namin infinite 
class InfiniteMode(GameMode):
    def __init__(self):
        super().__init__(health=3)
        self.current_level = 1
        self.level_words = {
            1: Datamodule.level1,
            2: Datamodule.level2,
            3: Datamodule.level3,
            4: Datamodule.level4,
            5: Datamodule.level5,
            6: Datamodule.level6,
            7: Datamodule.level7
        }
        self.load_level()
    
    def load_level(self):
        """Load words for current level and shuffle them randomly"""
        if self.current_level in self.level_words:
            self.words = self.level_words[self.current_level].copy()  # Make a copy
            random.shuffle(self.words)  #mahalaga to pang random ng word kanina kasi same word lagi e
            self.current_word_index = 0
            self.words_completed = 0
    
    def get_current_word(self):
        return self.words[self.current_word_index]
    
    def scramble_word(self, word):
        """Use randomizer's scramble function"""
        return randomizer.scramble(word)
    
    def next_word(self):
        self.current_word_index += 1
        self.words_completed += 1
        
        # tignan if complete mona ba ung 5 word para sa isang level
        if self.current_word_index >= len(self.words):
            self.current_level += 1
            if self.current_level in self.level_words:
                self.load_level()
                return f"LEVEL UP! Now at Level {self.current_level}"
            else:
                return "VICTORY! You completed all levels!"
        return None
    
    def is_game_over(self):
        return self.health <= 0
    
    def is_victory(self):
        return self.current_level > len(self.level_words)
    
    def get_mode_info(self):
        return f"Level {self.current_level}/7 - Word {self.words_completed + 1}/5"


# Mode 2: eto nag build ng qoutes
class QuoteBuilderMode(GameMode):
    def __init__(self):
        super().__init__(health=3)
        self.hints = utility.hints
        self.word_passes = utility.word_pass
        utility.hints = self.hints
        utility.word_pass = self.word_passes
        self.load_quote()
    
    def load_quote(self):
        """Load random quote from mode2"""
        self.quote_data = random.choice(Datamodule.mode2)
        self.words = self.quote_data["words"]
        self.target_quote = self.quote_data["quote"]
        self.current_word_index = 0
        self.correct_words = [False] * len(self.words)
    
    def get_current_word(self):
        return self.words[self.current_word_index]
    
    def scramble_word(self, word):
        """Use randomizer's scramble function"""
        return randomizer.scramble(word)
    
    def next_word(self):
        self.correct_words[self.current_word_index] = True
        self.current_word_index += 1
        
        if self.current_word_index >= len(self.words):
            return "QUOTE COMPLETE!"
        return None
    
    def is_game_over(self):
        return self.health <= 0
    
    def is_victory(self):
        return self.current_word_index >= len(self.words)
    
    def get_current_progress(self):
        """Show which words are completed"""
        progress = []
        for i, completed in enumerate(self.correct_words):
            if completed:
                progress.append(self.words[i])
            else:
                progress.append("_____")
        return ' '.join(progress)
    
    def get_complete_quote(self):
        return self.target_quote
    
    def get_mode_info(self):
        return f"Word {self.current_word_index + 1}/{len(self.words)}"


# Mode 3: Extreme Mode (sobrang dami neto)
class ExtremeMode(GameMode):
    def __init__(self):
        super().__init__(health=3)
        self.hints = 1
        self.word_passes = 1
        utility.hints = self.hints
        utility.word_pass = self.word_passes
        self.load_extreme_words()
    
    def load_extreme_words(self):
        """Load the longest words from all levels"""
        all_words = (Datamodule.mode3 + Datamodule.mode3 + Datamodule.mode3 + 
                    Datamodule.mode3 + Datamodule.mode3 + Datamodule.mode3 + 
                    Datamodule.mode3)
        
        # pang filter para dapat 8 letter words lang sa extreme
        self.words = [word for word in all_words if len(word) >= 7]
        random.shuffle(self.words)
        self.words = self.words[:8]  
        self.current_word_index = 0
    
    def scramble_word(self, word):
        # gamitin ung randomizer para ma scramble
        scrambled = randomizer.scramble(word)
        # prang scramble to para sa extreme
        if random.choice([True, False]):
            letters = list(scrambled)
            if len(letters) > 2:
                letters[0], letters[-1] = letters[-1], letters[0]
            scrambled = ''.join(letters)
        return scrambled
    
    def get_current_word(self):
        return self.words[self.current_word_index]
    
    def next_word(self):
        self.current_word_index += 1
        
        if self.current_word_index >= len(self.words):
            return "EXTREME CHALLENGE COMPLETE!"
        return None
    
    def is_game_over(self):
        return self.health <= 0
    
    def is_victory(self):
        return self.current_word_index >= len(self.words)
    
    def get_mode_info(self):
        remaining = len(self.words) - self.current_word_index
        return f"{remaining} words remaining"