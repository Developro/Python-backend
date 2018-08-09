# Generated by Django 2.0.7 on 2018-08-02 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=255, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(db_column='password_hash', max_length=64)),
                ('avatar', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=128, null=True)),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
                ('status', models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('DISABLED', 'DISABLED'), ('BANNED', 'BANNED')], default='ACTIVE', max_length=8)),
                ('role', models.CharField(choices=[('USER', 'USER'), ('ADMIN', 'ADMIN')], default='USER', max_length=5)),
                ('access_token_hash', models.CharField(blank=True, max_length=64, null=True)),
                ('acc_action_token_hash', models.CharField(blank=True, max_length=64, null=True)),
                ('refresh_token_hash', models.CharField(blank=True, max_length=64, null=True)),
                ('regstamp', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(db_column='last_visit')),
            ],
            options={
                'managed': False,
                'db_table': 'users',
            },
        ),
    ]
