# Generated by Django 4.2.19 on 2025-04-08 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=30)),
                ('opis', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Produkt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=100)),
                ('opis', models.TextField(blank=True, null=True)),
                ('cena', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('czy_dostepny', models.BooleanField(default=True)),
                ('kategoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.kategoria')),
            ],
        ),
    ]
