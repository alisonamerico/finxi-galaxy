# Generated by Django 3.0.8 on 2020-08-02 15:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Anunciante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created in')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified in')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Anunciante',
                'verbose_name_plural': 'Anunciantes',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='DemandaDePecas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao_peca', models.CharField(max_length=150)),
                ('endereco_entrega', models.CharField(max_length=150)),
                ('status_finalizacao', models.CharField(choices=[('ABERTA', 'Aberta'), ('FINALIZADA', 'Finalizada')], max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created in')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified in')),
                ('anunciante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Anunciante')),
            ],
            options={
                'verbose_name': 'DemandaDePeca',
                'verbose_name_plural': 'DemandaDePecas',
                'ordering': ['-created'],
            },
        ),
    ]
