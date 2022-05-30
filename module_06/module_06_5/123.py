import datetime


def clean():
    data = datetime.date(2010, 10, 10)  # '2010-10-10'
    today = datetime.date.today()
    delta = (today - data).days / 365

    if delta < 18:
        print('Регистрация не возможна')


clean()
