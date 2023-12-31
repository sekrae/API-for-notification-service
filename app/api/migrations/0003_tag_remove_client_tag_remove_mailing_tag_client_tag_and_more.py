# Generated by Django 4.2.3 on 2023-07-13 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_client_operator_code_alter_client_phone_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название Тега')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
        migrations.RemoveField(
            model_name='client',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='mailing',
            name='tag',
        ),
        migrations.AddField(
            model_name='client',
            name='tag',
            field=models.ManyToManyField(to='api.tag', verbose_name='Теги'),
        ),
        migrations.AddField(
            model_name='mailing',
            name='tag',
            field=models.ManyToManyField(to='api.tag', verbose_name='Теги'),
        ),
    ]
