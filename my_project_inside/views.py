from django.shortcuts import render
from django.core.cache import cache
from . import words_db


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
