from django.shortcuts import render
from django.views import View


class Regions(View):
    def get(self, request):

        print('=' * 20, request.GET)
        return render(request, 'advertisement/city.html', {'region': request.GET['region']})

    def post(self, request):
        print('=' * 20, request.POST)
        answer = 'Данные успешно добавлены'
        return render(request, 'advertisement/regions_1.html', {'answer': answer,
                                                                'login': request.POST['login'],
                                                                'password': request.POST['password']})


def region(request):
    regions = {
        'Москва': [
            'Щелково', 'Садовое кольцо'
        ],
        'Новосибирск': [
            'Студенческая', 'Речной вокзал'
        ]
    }
    print('func_region: ', request.GET)
    return render(request, 'advertisement/regions.html', {'regions': regions})


def advertisement_list(request):
    titles = {
        'contacts': 'Просмотр контактов администрации',
        'about': 'Бесплатные объявлениям',
        'private': 'Частные объявления',
        'region': 'Города и регионы'
    }
    return render(request, 'advertisement/advertisement_list.html', {'titles': titles})


def contacts_list(request):
    contacts = {'Мартынов Виктор': {'тел.': '8-923-227-3248', 'email': 'spas-1@rambler.ru'},
                'Мартынова Елена': {'тел.': '8-962-842-1028', 'email': 'map_len@mail.ru'}
                }
    return render(request, 'advertisement/contact_list.html', {'contacts': contacts})


def about(request):
    abouts = [
        'Бесплатные объявления'
    ]
    return render(request, 'advertisement/about.html', {'abouts': abouts})


def about_list(request):
    company = {
        'Строительство': ['Ремонтно-отделочные работы', 'Продам буры для перфоратора',
                          'Печи для бани', 'Ремонт и отделка квартир под ключ'],
        'Развлечение': ['Игры для плейстейшен', 'диски А.Розенбаума', 'Цифровой плеер', 'Проводные фитнес наушники'],
        'Транспорт': ['Покупаем масла для спецтехники', 'Услуги ассенизатора', 'Профессиональное асфальтирование дорог',
                      'Аренда самосвалов', 'Перевезу грузы']
    }
    return render(request, 'advertisement/about_list.html', {'company': company})


def board_list(request):
    exist = {
        'Автопогрузчик': ['Аренда вилочного автопогрузчика грузоподъемностью 10тн - 2500 руб./час с оператором'
                          '( минимум 8 часов ) + доставка.',
                          'Так же возможна холодная аренда !!!',
                          'Сдаем в аренду Автопогрузчик TCM FD100Z8',
                          'Вид топлива Дизель',
                          'Год выпуска 2016',
                          'Грузоподъемность(1кг) 10000',
                          'Высота подъема(мм) 3000'],
        'Котедж': ['Псковская область, Себежский район, от Санкт-Петербурга 480 км (5-6ч).',
                   'Жилая площадь дома 154,8+ мансарда, лоджия, большие чердачные и подвальные помещения;',
                   '2 с/у, 2 ванны, на участке баня, хоз-постройки, беседка, гараж д/2-ух машин + яма.',
                   'На территории растут яблони, смородина, крыжовник, малина, виноград, клубника. Интернет.',
                   'Вокруг посёлка сосновый лес(грибы, ягоды), озеро 2 км..до п. Идрица 13 км, г. Себеж 14 км'],
        'Шпитц': ['Очень красивый мальчишка, милый топтыжка ждёт своих мам и пап.',
                  'Море густой шерсти, ходит на пелёнку,',
                  'кушает проф. корм. Приезжайте, забирайте. Уместен небольшой торг.']
    }
    return render(request, 'advertisement/advertisement_private.html', {'exist': exist})

