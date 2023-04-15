# Generated by Django 4.1.5 on 2023-04-08 09:00

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
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Başlık')),
                ('text', models.TextField(verbose_name='Açıklama')),
                ('price', models.FloatField(verbose_name='Fiyat')),
                ('stok', models.IntegerField(verbose_name='Stok')),
                ('stars', models.FloatField(verbose_name='Ürün Puanı')),
                ('date_now', models.DateTimeField(auto_now_add=True, verbose_name='Tarih - Saat')),
            ],
        ),
        migrations.CreateModel(
            name='ProductColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Renk')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(max_length=200, upload_to='product', verbose_name='Ürün Resmi')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appMy.product', verbose_name='Ürün')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='renk',
            field=models.ManyToManyField(to='appMy.productcolor', verbose_name='Ürün Renkleri'),
        ),
        migrations.AddField(
            model_name='product',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Konu')),
                ('text', models.TextField(verbose_name='Yorum')),
                ('date_now', models.DateTimeField(auto_now_add=True, verbose_name='Tarih - Saat')),
                ('star', models.IntegerField(verbose_name='Yıldız')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appMy.product', verbose_name='Ürün')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı')),
            ],
        ),
    ]
