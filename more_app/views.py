import os
from django.http import HttpResponse
from django.conf import settings

from django.shortcuts import render, get_object_or_404

from settings_app.models import *
from .models import MeyoriyXujjatlar, OqituvchiKategoriyalari

# Pdf
from django.template.loader import get_template
from xhtml2pdf import pisa

def generate_pdf(request):
    avg_control = float(request.GET.get('avg_control', 0))
    avg_experiment = float(request.GET.get('avg_experiment', 0))
    effectiveness = float(request.GET.get('effectiveness', 0))

    # PDF yaratish uchun kontekst
    context = {
        'avg_control': avg_control,
        'avg_experiment': avg_experiment,
        'effectiveness': effectiveness,
    }

    # HTML shablonni yuklash
    template = get_template('pdf_template.html')
    html = template.render(context)

    # PDF yaratish
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="results.pdf"'

    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse('Xatolik yuz berdi PDF yaratishda', status=500)

    return response


def more_page(request, category_id):
    # Required
    SEO_SETTINGS = SeoSettings.objects.last()
    FOOTER_SETTINGS = FooterSettings.objects.last()
    SOCIAL_SETTINGS = SocialSettings.objects.all()
    LOGO_SETTINGS = LogoSettings.objects.last()
    ONE_HEADER = OneHeader.objects.all()
    TWO_HEADER = TwoHeader.objects.all()
    RIGHT_BUTTON_SETTINGS = RightButtonSettings.objects.last()
    PHONE_EMAIL_SETTINGS = PhoneEmailSettings.objects.last()

    # Main
    barcha_kategoriyalar = OqituvchiKategoriyalari.objects.all()
    kategoriya = get_object_or_404(OqituvchiKategoriyalari, id=category_id)

    fayllar = MeyoriyXujjatlar.objects.filter(kategoriyasi=kategoriya)

    ctx = {
        # Required
        'SEO_SETTINGS': SEO_SETTINGS,
        'FOOTER_SETTINGS': FOOTER_SETTINGS,
        'SOCIAL_SETTINGS': SOCIAL_SETTINGS,
        'LOGO_SETTINGS': LOGO_SETTINGS,
        'ONE_HEADER': ONE_HEADER,
        'TWO_HEADER': TWO_HEADER,
        'RIGHT_BUTTON_SETTINGS': RIGHT_BUTTON_SETTINGS,
        'PHONE_EMAIL_SETTINGS': PHONE_EMAIL_SETTINGS,

        # Main
        'FAYLLAR_KATEGORIYASI': barcha_kategoriyalar,
        'FAYLLAR': fayllar,
        'KATEGORIYA': kategoriya,
    }
    return render(request, 'more/oqituvchilarga.html', ctx)

def download_media_file(request, pk):
    media_file = get_object_or_404(MeyoriyXujjatlar, pk=pk)

    # Increment the download count
    media_file.yuklashlar_soni += 1
    media_file.save()

    # Serve the file for download
    file_path = os.path.join(settings.MEDIA_ROOT, str(media_file.fayl))
    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/force-download')
        response['Content-Disposition'] = 'attachment; filename=%s' % os.path.basename(file_path)
        return response

def communal_page(request):
    # Required
    SEO_SETTINGS = SeoSettings.objects.last()
    FOOTER_SETTINGS = FooterSettings.objects.last()
    SOCIAL_SETTINGS = SocialSettings.objects.all()
    LOGO_SETTINGS = LogoSettings.objects.last()
    ONE_HEADER = OneHeader.objects.all()
    TWO_HEADER = TwoHeader.objects.all()
    RIGHT_BUTTON_SETTINGS = RightButtonSettings.objects.last()
    PHONE_EMAIL_SETTINGS = PhoneEmailSettings.objects.last()

    # Main

    ctx = {
        # Required
        'SEO_SETTINGS': SEO_SETTINGS,
        'FOOTER_SETTINGS': FOOTER_SETTINGS,
        'SOCIAL_SETTINGS': SOCIAL_SETTINGS,
        'LOGO_SETTINGS': LOGO_SETTINGS,
        'ONE_HEADER': ONE_HEADER,
        'TWO_HEADER': TWO_HEADER,
        'RIGHT_BUTTON_SETTINGS': RIGHT_BUTTON_SETTINGS,
        'PHONE_EMAIL_SETTINGS': PHONE_EMAIL_SETTINGS,

        # Main
    }

    return render(request, 'actions/communal.html', ctx)

def gaz_page(request):
    # Required
    SEO_SETTINGS = SeoSettings.objects.last()
    FOOTER_SETTINGS = FooterSettings.objects.last()
    SOCIAL_SETTINGS = SocialSettings.objects.all()
    LOGO_SETTINGS = LogoSettings.objects.last()
    ONE_HEADER = OneHeader.objects.all()
    TWO_HEADER = TwoHeader.objects.all()
    RIGHT_BUTTON_SETTINGS = RightButtonSettings.objects.last()
    PHONE_EMAIL_SETTINGS = PhoneEmailSettings.objects.last()

    # Main

    ctx = {
        # Required
        'SEO_SETTINGS': SEO_SETTINGS,
        'FOOTER_SETTINGS': FOOTER_SETTINGS,
        'SOCIAL_SETTINGS': SOCIAL_SETTINGS,
        'LOGO_SETTINGS': LOGO_SETTINGS,
        'ONE_HEADER': ONE_HEADER,
        'TWO_HEADER': TWO_HEADER,
        'RIGHT_BUTTON_SETTINGS': RIGHT_BUTTON_SETTINGS,
        'PHONE_EMAIL_SETTINGS': PHONE_EMAIL_SETTINGS,

        # Main
    }

    return render(request, 'actions/gaz.html', ctx)

def kredit_page(request):
    # Required
    SEO_SETTINGS = SeoSettings.objects.last()
    FOOTER_SETTINGS = FooterSettings.objects.last()
    SOCIAL_SETTINGS = SocialSettings.objects.all()
    LOGO_SETTINGS = LogoSettings.objects.last()
    ONE_HEADER = OneHeader.objects.all()
    TWO_HEADER = TwoHeader.objects.all()
    RIGHT_BUTTON_SETTINGS = RightButtonSettings.objects.last()
    PHONE_EMAIL_SETTINGS = PhoneEmailSettings.objects.last()

    # Main

    ctx = {
        # Required
        'SEO_SETTINGS': SEO_SETTINGS,
        'FOOTER_SETTINGS': FOOTER_SETTINGS,
        'SOCIAL_SETTINGS': SOCIAL_SETTINGS,
        'LOGO_SETTINGS': LOGO_SETTINGS,
        'ONE_HEADER': ONE_HEADER,
        'TWO_HEADER': TWO_HEADER,
        'RIGHT_BUTTON_SETTINGS': RIGHT_BUTTON_SETTINGS,
        'PHONE_EMAIL_SETTINGS': PHONE_EMAIL_SETTINGS,

        # Main
    }

    return render(request, 'actions/kredit.html', ctx)

def ish_haqi(request):
    # Required
    SEO_SETTINGS = SeoSettings.objects.last()
    FOOTER_SETTINGS = FooterSettings.objects.last()
    SOCIAL_SETTINGS = SocialSettings.objects.all()
    LOGO_SETTINGS = LogoSettings.objects.last()
    ONE_HEADER = OneHeader.objects.all()
    TWO_HEADER = TwoHeader.objects.all()
    RIGHT_BUTTON_SETTINGS = RightButtonSettings.objects.last()
    PHONE_EMAIL_SETTINGS = PhoneEmailSettings.objects.last()

    # Main

    ctx = {
        # Required
        'SEO_SETTINGS': SEO_SETTINGS,
        'FOOTER_SETTINGS': FOOTER_SETTINGS,
        'SOCIAL_SETTINGS': SOCIAL_SETTINGS,
        'LOGO_SETTINGS': LOGO_SETTINGS,
        'ONE_HEADER': ONE_HEADER,
        'TWO_HEADER': TWO_HEADER,
        'RIGHT_BUTTON_SETTINGS': RIGHT_BUTTON_SETTINGS,
        'PHONE_EMAIL_SETTINGS': PHONE_EMAIL_SETTINGS,

        # Main
    }

    return render(request, 'actions/ish_haqi.html', ctx)



def matematik_s_page(request):
    # Required
    SEO_SETTINGS = SeoSettings.objects.last()
    FOOTER_SETTINGS = FooterSettings.objects.last()
    SOCIAL_SETTINGS = SocialSettings.objects.all()
    LOGO_SETTINGS = LogoSettings.objects.last()
    ONE_HEADER = OneHeader.objects.all()
    TWO_HEADER = TwoHeader.objects.all()
    RIGHT_BUTTON_SETTINGS = RightButtonSettings.objects.last()
    PHONE_EMAIL_SETTINGS = PhoneEmailSettings.objects.last()

    # Main

    ctx = {
        # Required
        'SEO_SETTINGS': SEO_SETTINGS,
        'FOOTER_SETTINGS': FOOTER_SETTINGS,
        'SOCIAL_SETTINGS': SOCIAL_SETTINGS,
        'LOGO_SETTINGS': LOGO_SETTINGS,
        'ONE_HEADER': ONE_HEADER,
        'TWO_HEADER': TWO_HEADER,
        'RIGHT_BUTTON_SETTINGS': RIGHT_BUTTON_SETTINGS,
        'PHONE_EMAIL_SETTINGS': PHONE_EMAIL_SETTINGS,

        # Main
    }

    return render(request, 'actions/matematik_s.html', ctx)

def t_kriteriya_page(request):
    # Required
    SEO_SETTINGS = SeoSettings.objects.last()
    FOOTER_SETTINGS = FooterSettings.objects.last()
    SOCIAL_SETTINGS = SocialSettings.objects.all()
    LOGO_SETTINGS = LogoSettings.objects.last()
    ONE_HEADER = OneHeader.objects.all()
    TWO_HEADER = TwoHeader.objects.all()
    RIGHT_BUTTON_SETTINGS = RightButtonSettings.objects.last()
    PHONE_EMAIL_SETTINGS = PhoneEmailSettings.objects.last()

    # Main

    ctx = {
        # Required
        'SEO_SETTINGS': SEO_SETTINGS,
        'FOOTER_SETTINGS': FOOTER_SETTINGS,
        'SOCIAL_SETTINGS': SOCIAL_SETTINGS,
        'LOGO_SETTINGS': LOGO_SETTINGS,
        'ONE_HEADER': ONE_HEADER,
        'TWO_HEADER': TWO_HEADER,
        'RIGHT_BUTTON_SETTINGS': RIGHT_BUTTON_SETTINGS,
        'PHONE_EMAIL_SETTINGS': PHONE_EMAIL_SETTINGS,

        # Main
    }

    return render(request, 'actions/t_kriteriya.html', ctx)

def xi_kvadrat_page(request):
    # Required
    SEO_SETTINGS = SeoSettings.objects.last()
    FOOTER_SETTINGS = FooterSettings.objects.last()
    SOCIAL_SETTINGS = SocialSettings.objects.all()
    LOGO_SETTINGS = LogoSettings.objects.last()
    ONE_HEADER = OneHeader.objects.all()
    TWO_HEADER = TwoHeader.objects.all()
    RIGHT_BUTTON_SETTINGS = RightButtonSettings.objects.last()
    PHONE_EMAIL_SETTINGS = PhoneEmailSettings.objects.last()

    # Main

    ctx = {
        # Required
        'SEO_SETTINGS': SEO_SETTINGS,
        'FOOTER_SETTINGS': FOOTER_SETTINGS,
        'SOCIAL_SETTINGS': SOCIAL_SETTINGS,
        'LOGO_SETTINGS': LOGO_SETTINGS,
        'ONE_HEADER': ONE_HEADER,
        'TWO_HEADER': TWO_HEADER,
        'RIGHT_BUTTON_SETTINGS': RIGHT_BUTTON_SETTINGS,
        'PHONE_EMAIL_SETTINGS': PHONE_EMAIL_SETTINGS,

        # Main
    }

    return render(request, 'actions/xi_kvadrat_2.html', ctx)


def bugalteriya_new_page(request):
    # Required
    SEO_SETTINGS = SeoSettings.objects.last()
    FOOTER_SETTINGS = FooterSettings.objects.last()
    SOCIAL_SETTINGS = SocialSettings.objects.all()
    LOGO_SETTINGS = LogoSettings.objects.last()
    ONE_HEADER = OneHeader.objects.all()
    TWO_HEADER = TwoHeader.objects.all()
    RIGHT_BUTTON_SETTINGS = RightButtonSettings.objects.last()
    PHONE_EMAIL_SETTINGS = PhoneEmailSettings.objects.last()

    # Main

    ctx = {
        # Required
        'SEO_SETTINGS': SEO_SETTINGS,
        'FOOTER_SETTINGS': FOOTER_SETTINGS,
        'SOCIAL_SETTINGS': SOCIAL_SETTINGS,
        'LOGO_SETTINGS': LOGO_SETTINGS,
        'ONE_HEADER': ONE_HEADER,
        'TWO_HEADER': TWO_HEADER,
        'RIGHT_BUTTON_SETTINGS': RIGHT_BUTTON_SETTINGS,
        'PHONE_EMAIL_SETTINGS': PHONE_EMAIL_SETTINGS,

        # Main
    }

    return render(request, 'actions/bugalteriya.html', ctx)
