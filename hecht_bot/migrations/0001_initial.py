# Generated by Django 2.1.3 on 2018-12-07 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Helper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='HelpingEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Datum')),
                ('helper', models.ManyToManyField(related_name='helping_entries', to='hecht_bot.Helper', verbose_name='Helfer')),
            ],
        ),
    ]