# Generated by Django 4.0.7 on 2022-09-09 18:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('nickname', models.CharField(max_length=30, unique=True)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('password', models.BinaryField(max_length=60)),
                ('salt', models.BinaryField(max_length=29)),
                ('is_active', models.IntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'member',
            },
        ),
    ]
