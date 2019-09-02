# Generated by Django 2.2.4 on 2019-09-02 04:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('article', '0002_auto_20190901_1654'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeartCheck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articlemodel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.ArticleModel')),
                ('usermodel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.UserModel')),
            ],
            options={
                'db_table': 'Heart',
            },
        ),
    ]
