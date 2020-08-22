# Generated by Django 3.0.5 on 2020-08-22 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20200504_2249'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skilltreeskill',
            name='requirements',
        ),
        migrations.AddField(
            model_name='skilltreeskill',
            name='requirements',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.SkillTreeSkill'),
        ),
    ]
