from django.shortcuts import render, redirect

# Telegram bot
import requests

from settings_app.models import TelegramBotSettings
from main_app.models import HomeMehnatFaoliyatiDivs, HomeMehnatFaoliyatim
from more_app.models import OqituvchiKategoriyalari

from .models import AboutMe, Message

def contact_page(request):
    TELEGRAM_BOT = TelegramBotSettings.objects.last()

    if request.method == "POST" and TELEGRAM_BOT:
        Message.objects.create(
            name=request.POST['name'],
            phone=request.POST['tg_username'],
            message=request.POST['message'],
        )

        url = f"https://api.telegram.org/bot{TELEGRAM_BOT.token}/sendMessage"

        payload = {
            "text": f"<b>✅ Yangi xabar:</b>\n\n"
                    f"<b>🧍‍♂️ Ism:</b> {request.POST['name']}\n"
                    f"<b>📬 Username:</b> {request.POST['tg_username']}\n"
                    f"<b>◽️ Xabar:</b> {request.POST['message']}",
            "chat_id": TELEGRAM_BOT.user_id,
            "parse_mode": "HTML",
        }
        headers = {
            "accept": "application/json",
            "User-Agent": "Telegram Bot SDK - (https://github.com/irazasyed/telegram-bot-sdk)",
            "content-type": "application/json"
        }

        response = requests.post(url, json=payload, headers=headers)

        return redirect('home_page')

    # Main
    ABOUT_ME = AboutMe.objects.last()

    ctx = {

        # Main
        'ABOUT_ME': ABOUT_ME,

    }
    return render(request, 'contact.html', ctx)

def me_page(request):

    barcha_kategoriyalar = OqituvchiKategoriyalari.objects.all()

    # Main
    ABOUT_ME = AboutMe.objects.last()
    MEHNAT_FAOLIYATI = HomeMehnatFaoliyatim.objects.last()
    MEHNAT_FAOLIYATI_DIVS = HomeMehnatFaoliyatiDivs.objects.all()

    ctx = {
        'FAYLLAR_KATEGORIYASI': barcha_kategoriyalar,

        # Main
        'ABOUT_ME': ABOUT_ME,
        'MEHNAT_FAOLIYATI': MEHNAT_FAOLIYATI,
        'MEHNAT_FAOLIYATI_DIVS': MEHNAT_FAOLIYATI_DIVS,

    }
    return render(request, 'me.html', ctx)

