import random
from my_project_inside import words_db

class Cards:
    def __init__(self):
        self.words = words_db.db_get_words_for_table()

    def get_shuffled_list(self):
        random.shuffle(self.words)
        return self.words
