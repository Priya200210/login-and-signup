# Generated by Django 4.1 on 2024-09-05 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_student_delete_student_detials'),
    ]

    operations = [
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('market_type', models.CharField(blank=True, max_length=255, null=True)),
                ('zipcode', models.CharField(default='00000', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='BedroomData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bedroom_count', models.IntegerField(choices=[(1, 'One Bedroom'), (2, 'Two Bedroom'), (3, 'Three Bedroom'), (4, 'Four Bedroom'), (5, 'Five Bedroom'), (6, 'Six Bedroom')])),
                ('average_price', models.FloatField(blank=True, null=True)),
                ('average_rent', models.FloatField(blank=True, null=True)),
                ('average_rent_yield', models.FloatField(blank=True, null=True)),
                ('median_price', models.FloatField(blank=True, null=True)),
                ('median_rent', models.DateField(blank=True, null=True)),
                ('median_rent_yield', models.FloatField(blank=True, null=True)),
                ('listing', models.IntegerField(blank=True, null=True)),
                ('market', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bedroom_data', to='login.market')),
            ],
            options={
                'unique_together': {('market', 'bedroom_count')},
            },
        ),
    ]
