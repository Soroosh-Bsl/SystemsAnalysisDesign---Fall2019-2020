# Generated by Django 2.2.6 on 2020-02-05 19:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BarberService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='BarberShop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('introduction', models.CharField(default='', max_length=1000)),
                ('address', models.CharField(default='', max_length=200)),
                ('city', models.CharField(default='', max_length=50)),
                ('foundation_year', models.CharField(default='2019', max_length=4)),
                ('phone', models.CharField(default='', max_length=20)),
                ('barber', models.ForeignKey(default=123456, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('duration', models.DurationField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField()),
                ('duration', models.DurationField()),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barber.BarberShop')),
            ],
        ),
        migrations.AddField(
            model_name='barbershop',
            name='service',
            field=models.ManyToManyField(through='barber.BarberService', to='barber.Service'),
        ),
        migrations.AddField(
            model_name='barberservice',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barber.Service'),
        ),
        migrations.AddField(
            model_name='barberservice',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barber.BarberShop'),
        ),
    ]