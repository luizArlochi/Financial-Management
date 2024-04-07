# Generated by Django 5.0.4 on 2024-04-07 20:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial', '0002_earnings'),
    ]

    operations = [
        migrations.CreateModel(
            name='Earning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Month',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Earnings',
        ),
        migrations.AddField(
            model_name='earning',
            name='month',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financial.month'),
        ),
        migrations.RenameModel(
            old_name='Expense',
            new_name='Label',
        ),
        migrations.AddField(
            model_name='transaction',
            name='label',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financial.label'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='month',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financial.month'),
        ),
    ]
