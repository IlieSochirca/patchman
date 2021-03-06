# Generated by Django 3.1.2 on 2020-10-29 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('content', models.CharField(max_length=500, unique=True)),
                ('created_on', models.DateField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='post.post')),
            ],
            options={
                'verbose_name_plural': 'Replies',
                'ordering': ['created_on'],
            },
        ),
    ]
