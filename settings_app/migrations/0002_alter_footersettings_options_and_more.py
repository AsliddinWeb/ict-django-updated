# Generated by Django 4.2.7 on 2023-12-22 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='footersettings',
            options={'ordering': ['id'], 'verbose_name_plural': 'Footer sozlamalari'},
        ),
        migrations.AlterModelOptions(
            name='logosettings',
            options={'ordering': ['id'], 'verbose_name_plural': 'Logo sozlamalari'},
        ),
        migrations.AlterModelOptions(
            name='oneheader',
            options={'ordering': ['id'], 'verbose_name_plural': '1-Darajali menyular'},
        ),
        migrations.AlterModelOptions(
            name='phoneemailsettings',
            options={'ordering': ['id'], 'verbose_name_plural': 'Telefon va email sozlamalari'},
        ),
        migrations.AlterModelOptions(
            name='rightbuttonsettings',
            options={'ordering': ['id'], 'verbose_name_plural': "O'ng tugmacha sozlamalari"},
        ),
        migrations.AlterModelOptions(
            name='seosettings',
            options={'ordering': ['id'], 'verbose_name_plural': 'Seo sozlamalari'},
        ),
        migrations.AlterModelOptions(
            name='socialsettings',
            options={'ordering': ['id'], 'verbose_name_plural': 'Ijtimoiy tarmoqlar'},
        ),
        migrations.AlterModelOptions(
            name='telegrambotsettings',
            options={'ordering': ['id'], 'verbose_name_plural': 'Telegram bot sozlamalari'},
        ),
        migrations.AlterModelOptions(
            name='twoheader',
            options={'ordering': ['id'], 'verbose_name_plural': '2-Darajali menyular'},
        ),
    ]
