from django.shortcuts import render
import random

from .models import Quiz
from settings_app.models import *

def quiz(request):
    # Required
    SEO_SETTINGS = SeoSettings.objects.last()
    FOOTER_SETTINGS = FooterSettings.objects.last()
    SOCIAL_SETTINGS = SocialSettings.objects.all()
    LOGO_SETTINGS = LogoSettings.objects.last()
    ONE_HEADER = OneHeader.objects.all()
    TWO_HEADER = TwoHeader.objects.all()
    RIGHT_BUTTON_SETTINGS = RightButtonSettings.objects.last()
    PHONE_EMAIL_SETTINGS = PhoneEmailSettings.objects.last()

    quizes = list(Quiz.objects.all())
    if len(quizes) >= 20:
        random_quizes = random.sample(quizes, 20)
    else:
        random_quizes = random.sample(quizes, len(quizes))

    if request.method == 'POST':
        print(request.POST)
        result = 0
        for i in range(len(random_quizes)):
            if request.POST.get(f'answer_{random_quizes[i].id}'):
                if request.POST.get(f'answer_{random_quizes[i].id}') == random_quizes[i].correct_answer:
                    result += 1
        return render(request, 'quiz/quiz-success.html', {
            'result': result,
            'len_quizes': len(random_quizes),
            'problem_results': len(random_quizes) - result,
        })

    ctx = {
        'quizes': random_quizes,
        # Required
        'SEO_SETTINGS': SEO_SETTINGS,
        'FOOTER_SETTINGS': FOOTER_SETTINGS,
        'SOCIAL_SETTINGS': SOCIAL_SETTINGS,
        'LOGO_SETTINGS': LOGO_SETTINGS,
        'ONE_HEADER': ONE_HEADER,
        'TWO_HEADER': TWO_HEADER,
        'RIGHT_BUTTON_SETTINGS': RIGHT_BUTTON_SETTINGS,
        'PHONE_EMAIL_SETTINGS': PHONE_EMAIL_SETTINGS,
    }

    return render(request, 'quiz/quiz.html', ctx)
