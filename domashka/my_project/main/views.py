from django.shortcuts import render

info = {
    'text00': 'PowerMyMac',
    'text01': 'Сделайте свой',
    'text02': 'Mac',
    'text03': 'лучше',
    'text04_btn': 'Попробуйте бесплатно',
    'text05_btn': 'Купить',
    'text06': f'PowerMyMac поможет вам оптимизировать и очистить ваш Mac. Простые клики, '
              'чтобы освободить место на Mac, ускорить работу MacBook или iMac. Держите свой\n'
              'Mac всегда в лучшем виде',
    'text07': 'чтобы освободить место на Mac, ускорить работу MacBook или iMac. Держите свой',
    'text08': 'Mac всегда в лучшем виде'
}
indexs = {
    'txt1': '5200+',
    'txt2': 'Projects completed',
    'txt3': '500+',
    'txt4': 'Active clients+',
    'txt5': '4500+',
    'txt6': 'Happy clients',
    'txt7': 'What Service We’re Offerin',
    'txt8': 'Website desig',
    'txt9': 'Need something changed or is ',
    'txt10': 'there something not quite working the',
    'txt11': 'best service',
    'txt12': 'We Provide the Best Web services',
    'txt13': 'Business Consultant Landing Page',
    'txt14': 'Food delivery Web Design',
    'txt15': 'Messenger landing Page',
    'txt16': 'Doctor’s Consultant Landing Page',
    'txt17': 'e-Leraning Web Design',
    'txt18': 'Job Finder landing Page',
    'txt19': 'View all Projects',
    'txt20': 'Meet Our Team',
    'txt21': 'кайфово? НЕТ!',
    'txt22': '',
    'txt23': '',
    'txt24': '',
    'txt25': '',
    'txt26': '',
    'txt27': '',
    'txt28': '',
    'txt29': '',


}


def index(request):
    return render(request, "main/index.html", indexs)


def main(request):
    return render(request, "main/card.html", info)


def mymac(request):
    return render(request, "main/index123.html", info)
# Create your views here.
