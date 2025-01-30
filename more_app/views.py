import os
from django.http import HttpResponse
from django.conf import settings

from django.shortcuts import render, get_object_or_404

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

    # Main
    barcha_kategoriyalar = OqituvchiKategoriyalari.objects.all()
    kategoriya = get_object_or_404(OqituvchiKategoriyalari, id=category_id)

    fayllar = MeyoriyXujjatlar.objects.filter(kategoriyasi=kategoriya)

    ctx = {

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
    return render(request, 'actions/communal.html')

def gaz_page(request):
    return render(request, 'actions/gaz.html')

def kredit_page(request):
    return render(request, 'actions/kredit.html')

def ish_haqi(request):
    return render(request, 'actions/ish_haqi.html')

def matematik_s_page(request):
    return render(request, 'actions/matematik_s.html')

def t_kriteriya_page(request):
    return render(request, 'actions/t_kriteriya.html')

def xi_kvadrat_page(request):
    return render(request, 'actions/xi_kvadrat.html')


def bugalteriya_new_page(request):
    return render(request, 'actions/bugalteriya.html')

def kompaniya_daromadi_page(request):
    return render(request, 'automation/kompaniya_daromadi.html')

def statistik_kuzatish_va_tahlil_page(request):
    return render(request, 'automation/statistik_kuzatish_va_tahlil.html')

def statistik_grafiklar_page(request):
    return render(request, 'automation/statistik_grafiklar.html')

def dinamikani_organish_va_prognozlash_page(request):
    return render(request, 'automation/dinamikani_organish_va_prognozlash.html')

def ekonometrik_model_page(request):
    return render(request, 'automation/ekonometrik_model.html')

def daromad_ortasidagi_bogliqlik_page(request):
    return render(request, 'automation/daromad_ortasidagi_bogliqlik.html')

def trend_va_prognozlash_page(request):
    return render(request, 'automation/trend_va_prognozlash.html')

def investitsiya_risklarini_baholash_page(request):
    return render(request, 'automation/investitsiya_risklarini_baholash.html')

def automation_home_page(request):
    return render(request, 'automation/home.html')
