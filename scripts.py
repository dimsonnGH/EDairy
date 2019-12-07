from  datacenter.models import Schoolkid, Mark, Chastisement, Lesson, Subject, Commendation, Teacher
import random
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

def get_schoolkid(part_of_name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains = part_of_name)
    except ObjectDoesNotExist:
        print("Ошибка. Не найден ученик: ", part_of_name)
        schoolkid = None
    except MultipleObjectsReturned:
        print("Ошибка. Найдено несколько учеников: ", part_of_name)
        schoolkid = None
    else:
        print("Найден ученик ", schoolkid)

    return schoolkid

def fix_marks(schoolkid):
    if schoolkid:
        Mark.objects.filter(schoolkid = schoolkid, points__in = [2, 3]).update(points = 5)

def remove_chastisements(schoolkid):
    if schoolkid:
        chastisements = Chastisement.objects.filter(schoolkid = schoolkid)
        chastisements.delete()

def create_commendation(part_of_name, subject__title):
    schoolkid = get_schoolkid(part_of_name)
    if schoolkid:

        list_of_commendation = [
            "Молодец!",
            "Отлично!",
            "Хорошо!",
            "Гораздо лучше, чем я ожидал!",
            "Ты меня приятно удивил!",
            "Великолепно!",
            "Прекрасно!",
            "Ты меня очень обрадовал!",
            "Именно этого я давно ждал от тебя!",
            "Сказано здорово – просто и ясно!",
            "Ты, как всегда, точен!",
            "Очень хороший ответ!",
            "Талантливо!",
            "Ты сегодня прыгнул выше головы!",
            "Я поражен!",
            "Уже существенно лучше!",
            "Потрясающе!",
            "Замечательно!",
            "Прекрасное начало!",
            "Так держать!",
            "Ты на верном пути!",
            "Здорово!",
            "Это как раз то, что нужно!",
            "Я тобой горжусь!",
            "С каждым разом у тебя получается всё лучше!",
            "Мы с тобой не зря поработали!",
            "Я вижу, как ты стараешься!",
            "Ты растешь над собой!",
            "Ты многое сделал, я это вижу!",
            "Теперь у тебя точно все получится!"]

        text = random.choice(list_of_commendation)
        lesson = Lesson.objects.filter(year_of_study = schoolkid.year_of_study, group_letter = schoolkid.group_letter, subject__year_of_study = schoolkid.year_of_study, subject__title = subject__title).order_by("date").last()
        Commendation.objects.create(text = text, created = lesson.date, schoolkid = schoolkid, subject = lesson.subject, teacher = lesson.teacher)

