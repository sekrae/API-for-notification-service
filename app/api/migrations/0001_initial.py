# Generated by Django 4.2.3 on 2023-07-13 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=7)),
                ('operator_code', models.CharField(max_length=3)),
                ('tag', models.CharField(max_length=150)),
                ('timezone', models.CharField(choices=[('Europe/Kaliningrad', 'Калининград - UTC+2'), ('Europe/Moscow', 'Москва - UTC+3'), ('Europe/Samara', 'Самара - UTC+4'), ('Asia/Yekaterinburg', 'Екатеринбург - UTC+5'), ('Asia/Omsk', 'Омск - UTC+6'), ('Asia/Novosibirsk', 'Новосибирск - UTC+7'), ('Asia/Irkutsk', 'Иркутск - UTC+8'), ('Asia/Yakutsk', 'Якутск - UTC+9'), ('Asia/Vladivostok', 'Владивосток - UTC+10'), ('Asia/Magadan', 'Магадан - UTC+11'), ('Asia/Srednekolymsk', 'Среднеколымск - UTC+11'), ('Asia/Kamchatka', 'Петропавловск-Камчатский - UTC+12')], max_length=100)),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(verbose_name='Дата и Время Запуска')),
                ('text', models.TextField(verbose_name='Текст сообщения')),
                ('operator_code', models.CharField(max_length=10, verbose_name='Код Оператора')),
                ('tag', models.CharField(max_length=150, verbose_name='Теги')),
                ('end_time', models.DateTimeField(verbose_name='Дата и Время Окончания')),
            ],
            options={
                'verbose_name': 'Рассылка',
                'verbose_name_plural': 'Рассылки',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('send_status', models.CharField(choices=[('Не отправлено', 'Не отправлено'), ('В процессе', 'В процессе'), ('Доставлено', 'Доставлено')], default='Не отправлено', max_length=255)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.client')),
                ('mailing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.mailing')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
            },
        ),
    ]
