from django.shortcuts import render, redirect
from django.core.cache import cache
from my_project_inside import words_db, quiz, flashcards


def index(request):
    return render(request, "index.html")


def terms_list(request):
    words = words_db.db_get_words_for_table()
    return render(request, "term_list.html", context={"words": words})


def add_term(request):
    return render(request, "term_add.html")


def send_term(request):
    if request.method == "POST":
        cache.clear()
        user_name = request.POST.get("name")
        new_word = request.POST.get("new_word", "")
        new_translation = request.POST.get("new_translation", "").replace(";", ",")
        context = {"user": user_name}
        if len(new_translation) == 0:
            context["success"] = False
            context["comment"] = "Описание должно быть не пустым"
        elif len(new_word) == 0:
            context["success"] = False
            context["comment"] = "Термин должен быть не пустым"
        else:
            context["success"] = True
            context["comment"] = "Ваш термин принят"
            words_db.db_write_word(new_word, new_translation)
        if context["success"]:
            context["success-title"] = ""
        return render(request, "term_request.html", context)
    else:
        add_term(request)


def show_stats(request):
    stats = words_db.db_get_words_stats()
    return render(request, "stats.html", stats)

"""Глобальная переменная, в которой хранится словарь:
ключи -- ключи сессий, значения -- объекты Quiz."""
global quizzes


def start_quiz(request):
    if not request.session.session_key:
        request.session.create()

    global quizzes
    if 'quizzes' in globals():
        quizzes[request.session.session_key] = quiz.Quiz()
    else:
        quizzes = dict()
        quizzes[request.session.session_key] = quiz.Quiz()

    return render(request, "quiz.html", context={"words": quizzes[request.session.session_key].qna,
                                                 "quiz_start": True})


def check_quiz(request):
    if request.method == "POST":
        my_list = quiz.Quiz()
        list_length = my_list.list_length()
        global quizzes
        for i in range(1, list_length+1):
            quizzes[request.session.session_key]\
                .record_user_answer(request.POST.get("answer" + "-" + str(i)))
        answers = quizzes[request.session.session_key].get_user_answers()
        marks = quizzes[request.session.session_key].check_quiz()
        return render(request, "quiz.html", context={"words": quizzes[request.session.session_key].qna,
                                                     "quiz_start": False,
                                                     "answers": answers,
                                                     "marks": marks})
    return redirect("/quiz")

def open_flashcards(request):
    cards = flashcards.Cards()
    random_words = cards.get_shuffled_list()
    return render(request, "flashcards.html", context={"random_words":random_words})
