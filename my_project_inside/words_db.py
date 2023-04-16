import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_project_inside.settings')
django.setup()

from my_project_inside.models import Words, Wordauthors

def db_get_words_for_table():
    words = []
    for i, item in enumerate(Words.objects.all()):
        words.append([i+1, item.word, item.translation])
    return words

def db_write_word(new_word, new_translation):
    word = Words(word=new_word, translation=new_translation)
    word.save()
    word_addition = Wordauthors(wordid=word.wordid, wordsource='user')
    word_addition.save()

def db_get_words_stats():
    db_words = len(Wordauthors.objects.filter(wordsource='db'))
    user_words = len(Wordauthors.objects.filter(wordsource='user'))
    words = Words.objects.all()
    stats = {
        'words_all': db_words + user_words,
        'words_own': db_words,
        'words_added': user_words,
    }
    return stats