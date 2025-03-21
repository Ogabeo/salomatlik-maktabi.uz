# Generated by Django 4.2.13 on 2024-07-07 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formula', '0007_formula_latex_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formula',
            name='formula',
        ),
        migrations.AlterField(
            model_name='formula',
            name='code',
            field=models.TextField(default='# Agar qaysidir kutubxonadan foydalansangiz, ularni import qiling\ndef solution(a, b, c):\n    # Siz o\'zingizni formulangizni yozasiz\n    \n    discriminant = b**2 - 4*a*c\n    \n    if discriminant < 0:\n        return "No real roots"\n    \n    x1 = (-b + (discriminant ** (1/2))) / (2*a)\n    x2 = (-b - (discriminant ** (1/2))) / (2*a)\n    \n    return x1, x2\n', verbose_name='Python Code'),
        ),
        migrations.AlterField(
            model_name='formula',
            name='latex_data',
            field=models.TextField(default='x=(-b±√(b^2-4ac))/(2a)', verbose_name='Latex Data'),
        ),
    ]
