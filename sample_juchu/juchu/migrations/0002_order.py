# Generated by Django 2.2.3 on 2019-07-18 05:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('juchu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('quantity', models.IntegerField(default=1)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='juchu.Customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='juchu.Product')),
            ],
        ),
    ]
