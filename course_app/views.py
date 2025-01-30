import os

from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.http import HttpResponse
from django.conf import settings

from settings_app.models import *
from .models import *
from more_app.models import OqituvchiKategoriyalari


def video_page(request):

    barcha_kategoriyalar = OqituvchiKategoriyalari.objects.all()

    # Main
    VIDEOS = Video.objects.all()
    page_num = request.GET.get('page', 1)
    paginator = Paginator(VIDEOS, 9)

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)

    ctx = {

        'FAYLLAR_KATEGORIYASI': barcha_kategoriyalar,

        # Main
        'VIDEOS': page_obj,
        'page_num': page_num,

    }
    return render(request, 'courses/video.html', ctx)

def slayd_page(request):

    barcha_kategoriyalar = OqituvchiKategoriyalari.objects.all()

    # Main
    SLAYDLAR = Slayd.objects.all()
    page_num = request.GET.get('page', 1)
    paginator = Paginator(SLAYDLAR, 9)

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)

    ctx = {

        'FAYLLAR_KATEGORIYASI': barcha_kategoriyalar,

        # Main
        'SLAYDLAR': page_obj,
        'page_num': page_num,

    }
    return render(request, 'courses/slayd.html', ctx)

def maruza_page(request):

    barcha_kategoriyalar = OqituvchiKategoriyalari.objects.all()

    # Main
    MARUZALAR = Maruza.objects.all()
    page_num = request.GET.get('page', 1)
    paginator = Paginator(MARUZALAR, 9)

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)

    ctx = {

        'FAYLLAR_KATEGORIYASI': barcha_kategoriyalar,

        # Main
        'MARUZALAR': page_obj,
        'page_num': page_num,

    }
    return render(request, 'courses/maruza.html', ctx)

def labaratoriya_page(request):

    barcha_kategoriyalar = OqituvchiKategoriyalari.objects.all()

    # Main
    AMALIYLAR = Labaratoriyalar.objects.all()
    page_num = request.GET.get('page', 1)
    paginator = Paginator(AMALIYLAR, 9)

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)

    ctx = {

        'FAYLLAR_KATEGORIYASI': barcha_kategoriyalar,

        # Main
        'LABARATORIYALAR': page_obj,
        'page_num': page_num,

    }
    return render(request, 'courses/labaratoriya.html', ctx)

def amaliy_page(request):

    barcha_kategoriyalar = OqituvchiKategoriyalari.objects.all()

    # Main
    AMALIYLAR = Amaliy.objects.all()
    page_num = request.GET.get('page', 1)
    paginator = Paginator(AMALIYLAR, 9)

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)

    ctx = {

        'FAYLLAR_KATEGORIYASI': barcha_kategoriyalar,

        # Main
        'AMALIYLAR': page_obj,
        'page_num': page_num,

    }
    return render(request, 'courses/amaliy.html', ctx)

def test_page(request):

    barcha_kategoriyalar = OqituvchiKategoriyalari.objects.all()

    # Main
    TESTLAR = Testlar.objects.all()
    page_num = request.GET.get('page', 1)
    paginator = Paginator(TESTLAR, 9)

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)

    ctx = {

        'FAYLLAR_KATEGORIYASI': barcha_kategoriyalar,

        # Main
        'TESTLAR': page_obj,
        'page_num': page_num,

    }
    return render(request, 'courses/test.html', ctx)


# --------------------------------------------------

def download_maruza(request, pk):
    media_file = get_object_or_404(Maruza, pk=pk)

    # Increment the download count
    media_file.yuklashlar_soni += 1
    media_file.save()

    # Serve the file for download
    file_path = os.path.join(settings.MEDIA_ROOT, str(media_file.maruza_fayl))
    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/force-download')
        response['Content-Disposition'] = 'attachment; filename=%s' % os.path.basename(file_path)
        return response

def download_amaliy(request, pk):
    media_file = get_object_or_404(Amaliy, pk=pk)

    # Increment the download count
    media_file.yuklashlar_soni += 1
    media_file.save()

    # Serve the file for download
    file_path = os.path.join(settings.MEDIA_ROOT, str(media_file.amaliy_fayl))
    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/force-download')
        response['Content-Disposition'] = 'attachment; filename=%s' % os.path.basename(file_path)
        return response

def download_taqdimot(request, pk):
    media_file = get_object_or_404(Slayd, pk=pk)

    # Increment the download count
    media_file.yuklashlar_soni += 1
    media_file.save()

    # Serve the file for download
    file_path = os.path.join(settings.MEDIA_ROOT, str(media_file.slayd_fayl))
    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/force-download')
        response['Content-Disposition'] = 'attachment; filename=%s' % os.path.basename(file_path)
        return response

def download_labaratoriya(request, pk):
    media_file = get_object_or_404(Labaratoriyalar, pk=pk)

    # Increment the download count
    media_file.yuklashlar_soni += 1
    media_file.save()

    # Serve the file for download
    file_path = os.path.join(settings.MEDIA_ROOT, str(media_file.labaratoriya_fayl))
    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/force-download')
        response['Content-Disposition'] = 'attachment; filename=%s' % os.path.basename(file_path)
        return response
