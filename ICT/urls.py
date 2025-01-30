from django.contrib import admin
from django.urls import path, include

# Static settings
from django.conf import settings
from django.conf.urls.static import static

# Views
from main_app.views import home_page
from contact_app.views import contact_page, me_page
from more_app.views import (communal_page, gaz_page, kredit_page, ish_haqi, matematik_s_page,
                            t_kriteriya_page, generate_pdf, xi_kvadrat_page, bugalteriya_new_page,
                            kompaniya_daromadi_page, statistik_kuzatish_va_tahlil_page,
                            statistik_grafiklar_page, dinamikani_organish_va_prognozlash_page,
                            ekonometrik_model_page, daromad_ortasidagi_bogliqlik_page,
                            trend_va_prognozlash_page, investitsiya_risklarini_baholash_page,
                            automation_home_page
                            )

urlpatterns = [
    path('admin/', admin.site.urls),

    # Views
    path('', home_page, name='home_page'),

    path('courses/', include('course_app.urls')),

    path('contact/', contact_page, name='contact_page'),
    path('me/', me_page, name='me_page'),

    # More
    path('oqituvchi/', include('more_app.urls')),

    path('actions/communal/', communal_page, name='communal_page'),
    path('actions/kredit/', kredit_page, name='kredit_page'),
    path('actions/gaz/', gaz_page, name='gaz_page'),
    path('actions/ish/', ish_haqi, name='ish_haqi'),
    path('actions/buxgalteriya-dasturi/', bugalteriya_new_page, name='bugalteriya_new_page'),
    path('actions/hisoblash/', matematik_s_page, name='hisoblash_page'),
    path('actions/hisoblash/t-kriteriya/', t_kriteriya_page, name='t_kriteriya_page'),
    path('actions/hisoblash/xi-kvadrat/', xi_kvadrat_page, name='xi_kvadrat_page'),
    path('generate-pdf/', generate_pdf, name='generate_pdf'),

    # Automation
    path('automation/kompaniya-daromadi/', kompaniya_daromadi_page, name='kompaniya_daromadi_page'),
    path('automation/statistik-kuzatish-va-tahlil/', statistik_kuzatish_va_tahlil_page, name='statistik_kuzatish_va_tahlil_page'),
    path('automation/statistik-grafiklar/', statistik_grafiklar_page, name='statistik_grafiklar_page'),
    path('automation/dinamikani-organish-va-prognozlash/', dinamikani_organish_va_prognozlash_page, name='dinamikani_organish_va_prognozlash_page'),

    path('automation/ekonometrik-model/', ekonometrik_model_page, name='ekonometrik_model_page'),
    path('automation/daromad-ortasidagi-bogliqlik/', daromad_ortasidagi_bogliqlik_page, name='daromad_ortasidagi_bogliqlik_page'),
    path('automation/trend-va-prognozlash/', trend_va_prognozlash_page, name='trend_va_prognozlash_page'),
    path('automation/investitsiya-risklarini-baholash/', investitsiya_risklarini_baholash_page, name='investitsiya_risklarini_baholash_page'),

    # Home
    path('automation/', automation_home_page, name='automation_home_page'),

    # Quiz
    path('quiz/', include('quiz_app.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
