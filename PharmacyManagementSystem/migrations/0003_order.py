# Generated by Django 4.0.4 on 2022-06-05 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PharmacyManagementSystem', '0002_customers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveBigIntegerField()),
                ('price', models.FloatField()),
                ('total_price', models.FloatField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PharmacyManagementSystem.customers')),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PharmacyManagementSystem.medicine')),
            ],
        ),
    ]