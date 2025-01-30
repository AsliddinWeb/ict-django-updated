from django.shortcuts import render

from settings_app.models import *
from .models import *
from more_app.models import OqituvchiKategoriyalari

# Create your views here.
def home_page(request):

    barcha_kategoriyalar = OqituvchiKategoriyalari.objects.all()

    # Main
    HOME_WELCOME = HomeWelcome.objects.last()
    HOME_YONALISHLAR = HomeYonalishlar.objects.last()
    HOME_YONALISHLAR_FOR = HomeYonalishlarDivs.objects.all()
    HOME_MAVJUD_YONALISHLAR = HomeMavjudYonalishlar.objects.all()
    HOME_ABOUT_ME = HomeAboutMe.objects.last()
    HOME_MEHNAT_FAOLIYATIM = HomeMehnatFaoliyatim.objects.last()
    HOME_MEHNAT_FAOLIYATIM_DIVS = HomeMehnatFaoliyatiDivs.objects.all()[:3]
    HOME_APP = HomeApp.objects.last()
    HOME_TELEGRAM_GROUP = HomeTelegramGroup.objects.last()
    HOME_QUESTION = HomeQuestion.objects.last()
    HOME_SLIDERS = HomeSlider.objects.all()

    ctx = {

        'FAYLLAR_KATEGORIYASI': barcha_kategoriyalar,

        # Main
        'HOME_WELCOME': HOME_WELCOME,
        'HOME_YONALISHLAR': HOME_YONALISHLAR,
        'HOME_YONALISHLAR_FOR': HOME_YONALISHLAR_FOR,
        'HOME_MAVJUD_YONALISHLAR': HOME_MAVJUD_YONALISHLAR,
        'HOME_ABOUT_ME': HOME_ABOUT_ME,
        'HOME_MEHNAT_FAOLIYATIM': HOME_MEHNAT_FAOLIYATIM,
        'HOME_MEHNAT_FAOLIYATIM_DIVS': HOME_MEHNAT_FAOLIYATIM_DIVS,
        'HOME_APP': HOME_APP,
        'HOME_TELEGRAM_GROUP': HOME_TELEGRAM_GROUP,
        'HOME_QUESTION': HOME_QUESTION,
        'HOME_SLIDERS': HOME_SLIDERS,
    }
    return render(request, 'index.html', ctx)
