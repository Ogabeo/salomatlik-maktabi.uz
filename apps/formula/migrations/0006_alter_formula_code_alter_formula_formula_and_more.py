# Generated by Django 4.2.13 on 2024-07-06 19:52

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formula', '0005_alter_formula_code_alter_formula_formula'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formula',
            name='code',
            field=models.TextField(default='def solution(a):\n    # Write your formula here\n    result = a ** 2\n    return result\n', verbose_name='Python Code'),
        ),
        migrations.AlterField(
            model_name='formula',
            name='formula',
            field=ckeditor.fields.RichTextField(default='<p>a<sup>2</sup></p>', verbose_name='Math Formula'),
        ),
        migrations.AlterField(
            model_name='formula',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Formula Name'),
        ),
        migrations.AlterField(
            model_name='formula',
            name='variables',
            field=models.JSONField(blank=True, null=True, verbose_name='Used Variables'),
        ),
    ]
