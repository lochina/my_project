from my_project_inside import words_db
import random
from random import choices


class Quiz:
    def __init__(self):
        random_terms = words_db.db_get_words_for_table()
        random.shuffle(random_terms)

        self.qna = []
        cnt = 0
        for rt in random_terms:
            qna_item = []
            cnt += 1
            qna_item.append(cnt)
            qna_item = qna_item + rt[1:]
            self.qna.append(qna_item)

        self.user_answers = []

    def list_length(self):
        return len(self.qna)

    def record_user_answer(self, a):
        """Добавляет ответ пользователя в переменную экземпляра (список ответов)"""
        self.user_answers.append(a)

    def get_user_answers(self):
        return self.user_answers

    def check_quiz(self):
        """Проверяет ответы и возвращает список эмодзи"""
        correct_answers = [qna_item[2] for qna_item in self.qna]
        answers_true_false = [i == j for i, j in zip(self.user_answers, correct_answers)]
        answers_emoji = [str(atf).replace('False', '❌').replace('True', '✅') for atf in answers_true_false]
        return answers_emoji
